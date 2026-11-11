<?php
// Shared code of the remarks server: the PHP implementation, for the live site,
// of the API served in development by src/app/api/ (same URLs, same JSON). See
// docs/DEPLOY.md. Plain PHP 7.4+, no dependencies: it runs on shared hosting.

declare(strict_types=1);

// ---- configuration -------------------------------------------------------------
function cfg(): array {
  static $c = null;
  if ($c !== null) return $c;
  $file = getenv('LEARNING_CONFIG') ?: __DIR__ . '/config.php';
  $c = is_file($file) ? require $file : [];
  $c += [
    'orcid_client_id' => '',
    'orcid_client_secret' => '',
    'orcid_base' => 'https://orcid.org',
    'admin_orcids' => [],
    'admin_token' => '',
    'data_dir' => dirname(__DIR__, 2) . '/learning-data',
    'lessons_json' => __DIR__ . '/lessons.json',
    'site_url' => '',
    'dev_login' => false,
  ];
  return $c;
}
function orcid_configured(): bool {
  return cfg()['orcid_client_id'] !== '' && cfg()['orcid_client_secret'] !== '';
}

// ---- responses -----------------------------------------------------------------
function json_out($data, int $code = 200): void {
  http_response_code($code);
  header('Content-Type: application/json; charset=utf-8');
  header('Cache-Control: no-store');
  echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
  exit;
}
function fail(int $code, string $msg): void { json_out(['error' => $msg], $code); }
function redirect(string $url): void { header('Location: ' . $url, true, 302); exit; }
function body(): ?array {
  $b = json_decode(file_get_contents('php://input') ?: '', true);
  return is_array($b) ? $b : null;
}

// ---- requests ------------------------------------------------------------------
function https(): bool {
  return (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off')
    || (($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https');
}
function site_url(): string {
  $u = cfg()['site_url'];
  if ($u !== '') return rtrim($u, '/');
  return (https() ? 'https' : 'http') . '://' . ($_SERVER['HTTP_HOST'] ?? 'localhost');
}
// Only same-site relative paths as post-login destinations (src/lib/auth.ts safeReturnTo).
function safe_return_to($v): string {
  if (!is_string($v) || $v === '' || $v[0] !== '/' || substr($v, 0, 2) === '//' || strpos($v, '\\') !== false) return '/';
  return $v;
}
// Reject cross-site state-changing requests (src/lib/auth.ts sameOrigin); the
// session cookie is SameSite=Lax as well.
function same_origin(): bool {
  $origin = $_SERVER['HTTP_ORIGIN'] ?? '';
  if ($origin === '') return true;
  $p = parse_url($origin);
  if (!is_array($p) || empty($p['host'])) return false;
  $host = $p['host'] . (isset($p['port']) ? ':' . $p['port'] : '');
  return strtolower($host) === strtolower($_SERVER['HTTP_X_FORWARDED_HOST'] ?? ($_SERVER['HTTP_HOST'] ?? ''));
}
function orcid_valid(string $id): bool { // ISO 7064 11,2 check digit
  if (!preg_match('/^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$/', $id)) return false;
  $d = str_replace('-', '', $id);
  $t = 0;
  for ($i = 0; $i < 15; $i++) $t = ($t + (int) $d[$i]) * 2;
  $r = (12 - $t % 11) % 11;
  return $d[15] === ($r === 10 ? 'X' : (string) $r);
}

// ---- session -------------------------------------------------------------------
function start_session(): void {
  if (session_status() === PHP_SESSION_ACTIVE) return;
  $dir = data_dir() . '/sessions';
  if (!is_dir($dir)) @mkdir($dir, 0700, true);
  if (is_dir($dir)) session_save_path($dir);
  session_name('cl_session');
  session_set_cookie_params(['lifetime' => 60 * 60 * 24 * 30, 'path' => '/', 'secure' => https(), 'httponly' => true, 'samesite' => 'Lax']);
  ini_set('session.gc_maxlifetime', (string) (60 * 60 * 24 * 30));
  session_start();
}
// The signed-in person: {orcid, name, isAdmin}, or null.
function current_user(): ?array {
  start_session();
  $u = $_SESSION['user'] ?? null;
  if (!is_array($u)) return null;
  return ['orcid' => $u['orcid'], 'name' => $u['name'], 'isAdmin' => in_array($u['orcid'], cfg()['admin_orcids'], true)];
}
function sign_in(string $orcid, string $name): void {
  start_session();
  session_regenerate_id(true);
  $_SESSION['user'] = ['orcid' => $orcid, 'name' => $name];
  with_store(function (array $s) use ($orcid, $name) {
    $s['users'][$orcid] = ['name' => $name];
    return $s;
  });
}

// ---- storage -------------------------------------------------------------------
// data_dir/remarks.json  {nextId, users: {orcid: {name}}, comments: [{id, lessonId, parentId,
//                         kind, body, anchor, status, contentHash, createdAt, updatedAt, orcid}]}
// Outside the web root; dates as "YYYY-MM-DD HH:MM:SS" (UTC), as in the SQLite version.
function data_dir(): string {
  $d = cfg()['data_dir'];
  if (!is_dir($d) && !@mkdir($d, 0700, true)) fail(500, 'Cannot create the data directory.');
  return $d;
}
function empty_store(): array { return ['nextId' => 1, 'users' => [], 'comments' => []]; }
function read_store(): array {
  $file = data_dir() . '/remarks.json';
  if (!is_file($file)) return empty_store();
  $s = json_decode((string) file_get_contents($file), true);
  if (!is_array($s)) fail(500, 'Corrupted remarks file.');
  return $s + empty_store();
}
// Run $fn(store) under an exclusive lock; if it returns an array, save it.
function with_store(callable $fn) {
  $dir = data_dir();
  $lock = fopen("$dir/.lock", 'c');
  flock($lock, LOCK_EX);
  try {
    $s = read_store();
    $out = $fn($s);
    if (!is_array($out)) return $out;
    $file = "$dir/remarks.json";
    $out['users'] = (object) $out['users'];
    file_put_contents("$file.tmp", json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    rename("$file.tmp", $file);
    $out['users'] = (array) $out['users'];
    return $out;
  } finally {
    flock($lock, LOCK_UN);
    fclose($lock);
  }
}
function now(): string { return gmdate('Y-m-d H:i:s'); }

// The lessons of the deployed working copy, with the hash of their source
// (written by scripts/build-static.ts): {lessonId: contentHash}.
function lessons(): array {
  static $l = null;
  if ($l === null) {
    $l = json_decode((string) @file_get_contents(cfg()['lessons_json']), true);
    if (!is_array($l)) fail(500, 'Cannot read the list of lessons.');
  }
  return $l;
}

// ---- comments ------------------------------------------------------------------
const COMMENT_KINDS = ['typo', 'unclear', 'error', 'suggestion', 'question'];
const COMMENT_STATUSES = ['open', 'resolved', 'declined'];

function cut($v, int $max): string {
  if (!is_string($v)) return '';
  return function_exists('mb_substr') ? mb_substr($v, 0, $max) : substr($v, 0, $max);
}
function text_length(string $s): int { return function_exists('mb_strlen') ? mb_strlen($s) : strlen($s); }

// src/lib/comments.ts parseAnchor
function parse_anchor($v): ?array {
  if (!is_array($v)) return null;
  $exact = cut($v['exact'] ?? null, 2000);
  if (trim($exact) === '') return null;
  $pos = $v['position'] ?? null;
  return [
    'exact' => $exact,
    'prefix' => cut($v['prefix'] ?? null, 64),
    'suffix' => cut($v['suffix'] ?? null, 64),
    'position' => (is_int($pos) || (is_float($pos) && is_finite($pos))) ? max(0, (int) floor($pos)) : 0,
    'display' => cut($v['display'] ?? null, 2000) ?: $exact,
  ];
}
function find_comment(array $s, int $id): ?array {
  foreach ($s['comments'] as $c) if ($c['id'] === $id) return $c;
  return null;
}
// src/lib/comment-types.ts CommentDTO
function to_dto(array $c, array $s, ?array $me): array {
  return [
    'id' => $c['id'],
    'lessonId' => $c['lessonId'],
    'parentId' => $c['parentId'],
    'kind' => $c['kind'],
    'body' => $c['body'],
    'anchor' => $c['anchor'],
    'status' => $c['status'],
    'contentHash' => $c['contentHash'],
    'createdAt' => $c['createdAt'] . 'Z',
    'updatedAt' => $c['updatedAt'] . 'Z',
    'author' => ['name' => $s['users'][$c['orcid']]['name'] ?? $c['orcid'], 'orcid' => $c['orcid']],
    'mine' => $me !== null && $me['orcid'] === $c['orcid'],
    'replies' => [],
  ];
}
function list_threads(array $s, string $lessonId, ?array $me): array {
  $rows = array_values(array_filter($s['comments'], fn ($c) => $c['lessonId'] === $lessonId));
  usort($rows, fn ($a, $b) => [$a['createdAt'], $a['id']] <=> [$b['createdAt'], $b['id']]);
  $threads = [];
  $index = [];
  foreach ($rows as $c) {
    $d = to_dto($c, $s, $me);
    if ($c['parentId'] === null) { $index[$c['id']] = count($threads); $threads[] = $d; }
    elseif (isset($index[$c['parentId']])) $threads[$index[$c['parentId']]]['replies'][] = $d;
  }
  return $threads;
}

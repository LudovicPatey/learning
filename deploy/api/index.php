<?php
// Remarks server of the live site (docs/DEPLOY.md). Every request under /api/ is
// sent here by api/.htaccess; the routes and the JSON are those of the Next.js
// API used in development (src/app/api/), so the client code is the same.
//
//   GET    /api/auth/me                 {user, orcidConfigured, devLogin}
//   GET    /api/auth/orcid/login?returnTo=/path    redirect to ORCID
//   GET    /api/auth/orcid/callback     ORCID redirects here (the redirect URI registered with ORCID)
//   POST   /api/auth/logout
//   GET    /api/auth/dev-login?returnTo=/path      local development only (config dev_login)
//   GET    /api/comments?lesson=<course/slug>      {threads, me}
//   POST   /api/comments                {lessonId, body, kind?, anchor?, parentId?}
//   PATCH  /api/comments/<id>           {body} (author) or {status} (maintainer)
//   DELETE /api/comments/<id>           author or maintainer
//   GET    /api/admin/export            all remarks (header Authorization: Bearer <admin_token>)

declare(strict_types=1);
require __DIR__ . '/lib.php';

$path = (string) parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);
$route = trim((string) preg_replace('~^.*?/api/~', '', $path), '/');
$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

if ($route === 'auth/me' && $method === 'GET') {
  json_out(['user' => current_user(), 'orcidConfigured' => orcid_configured(), 'devLogin' => dev_login_allowed()]);
}

if ($route === 'auth/logout' && $method === 'POST') {
  if (!same_origin()) fail(403, 'Forbidden');
  start_session();
  $_SESSION = [];
  session_destroy();
  json_out(['ok' => true]);
}

if ($route === 'auth/orcid/login' && $method === 'GET') {
  $returnTo = safe_return_to($_GET['returnTo'] ?? null);
  if (!orcid_configured()) {
    if (dev_login_allowed()) redirect(site_url() . '/api/auth/dev-login?returnTo=' . rawurlencode($returnTo));
    http_response_code(503);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'ORCID sign-in is not configured (see api/config.example.php).';
    exit;
  }
  start_session();
  $_SESSION['oauth'] = ['state' => bin2hex(random_bytes(16)), 'returnTo' => $returnTo];
  redirect(cfg()['orcid_base'] . '/oauth/authorize?' . http_build_query([
    'client_id' => cfg()['orcid_client_id'], 'response_type' => 'code', 'scope' => '/authenticate',
    'redirect_uri' => site_url() . '/api/auth/orcid/callback', 'state' => $_SESSION['oauth']['state'],
  ]));
}

if ($route === 'auth/orcid/callback' && $method === 'GET') {
  start_session();
  $saved = $_SESSION['oauth'] ?? [];
  unset($_SESSION['oauth']);
  $failTo = fn (string $msg) => redirect(site_url() . '/signin-error/?reason=' . rawurlencode($msg));
  if (isset($_GET['error'])) $failTo((string) ($_GET['error_description'] ?? 'ORCID sign-in was cancelled.'));
  $state = (string) ($_GET['state'] ?? '');
  if (!isset($_GET['code']) || $state === '' || !hash_equals((string) ($saved['state'] ?? ''), $state)) {
    $failTo('The sign-in request expired or was tampered with. Please try again.');
  }
  $ch = curl_init(cfg()['orcid_base'] . '/oauth/token');
  curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => 20,
    CURLOPT_HTTPHEADER => ['Accept: application/json'],
    CURLOPT_POSTFIELDS => http_build_query([
      'client_id' => cfg()['orcid_client_id'], 'client_secret' => cfg()['orcid_client_secret'],
      'grant_type' => 'authorization_code', 'code' => (string) $_GET['code'],
      'redirect_uri' => site_url() . '/api/auth/orcid/callback',
    ]),
  ]);
  $res = json_decode((string) curl_exec($ch), true);
  curl_close($ch);
  $orcid = (string) ($res['orcid'] ?? '');
  if (!orcid_valid($orcid)) $failTo('Could not verify your ORCID iD. Please try again.');
  // the name is the one public on the ORCID record (the iD when it is private)
  sign_in($orcid, trim((string) ($res['name'] ?? '')) ?: $orcid);
  redirect(site_url() . safe_return_to($saved['returnTo'] ?? null));
}

if ($route === 'auth/dev-login' && $method === 'GET') {
  if (!dev_login_allowed()) fail(404, 'Not found');
  // ORCID's documented fictitious researcher, as in src/app/api/auth/dev-login
  sign_in('0000-0002-1825-0097', 'Josiah Carberry (dev login)');
  redirect(site_url() . safe_return_to($_GET['returnTo'] ?? null));
}

if ($route === 'comments' && $method === 'GET') {
  $lessonId = (string) ($_GET['lesson'] ?? '');
  if (!array_key_exists($lessonId, lessons())) fail(404, 'Unknown lesson');
  $me = current_user();
  json_out(['threads' => list_threads(read_store(), $lessonId, $me), 'me' => $me]);
}

if ($route === 'comments' && $method === 'POST') {
  if (!same_origin()) fail(403, 'Forbidden');
  $me = current_user();
  if (!$me) fail(401, 'Sign in with ORCID to comment.');
  $b = body();
  if ($b === null) fail(400, 'Invalid JSON');
  $lessonId = (string) ($b['lessonId'] ?? '');
  if (!array_key_exists($lessonId, lessons())) fail(404, 'Unknown lesson');
  $text = is_string($b['body'] ?? null) ? trim($b['body']) : '';
  if ($text === '' || text_length($text) > 5000) fail(400, 'Comment must be between 1 and 5000 characters.');
  $kind = in_array($b['kind'] ?? null, COMMENT_KINDS, true) ? $b['kind'] : 'suggestion';

  $s = with_store(function (array $s) use ($me, $b, $lessonId, $text, $kind) {
    $parentId = null;
    if (isset($b['parentId'])) {
      $parent = is_numeric($b['parentId']) ? find_comment($s, (int) $b['parentId']) : null;
      if (!$parent || $parent['lessonId'] !== $lessonId || $parent['parentId'] !== null) fail(400, 'Invalid parent comment');
      $parentId = $parent['id'];
    }
    $anchor = $parentId === null ? parse_anchor($b['anchor'] ?? null) : null;
    if ($parentId === null && !$anchor) fail(400, 'Select a passage of the lesson to comment on.');
    $t = now();
    $s['comments'][] = [
      'id' => $s['nextId'], 'lessonId' => $lessonId, 'parentId' => $parentId,
      'kind' => $parentId === null ? $kind : 'suggestion', 'body' => $text, 'anchor' => $anchor,
      'status' => 'open', 'contentHash' => $parentId === null ? lessons()[$lessonId] : null,
      'createdAt' => $t, 'updatedAt' => $t, 'orcid' => $me['orcid'],
    ];
    $s['nextId']++;
    $s['users'][$me['orcid']] = ['name' => $me['name']];
    return $s;
  });
  json_out(['comment' => to_dto(end($s['comments']), $s, $me)], 201);
}

if (preg_match('~^comments/(\d+)$~', $route, $m) && in_array($method, ['PATCH', 'DELETE'], true)) {
  if (!same_origin()) fail(403, 'Forbidden');
  $me = current_user();
  if (!$me) fail(401, 'Not signed in');
  $id = (int) $m[1];
  $b = $method === 'PATCH' ? (body() ?? []) : [];

  $s = with_store(function (array $s) use ($me, $id, $b, $method) {
    $i = array_search($id, array_column($s['comments'], 'id'), true);
    if ($i === false) fail(404, 'Not found');
    $c = $s['comments'][$i];
    if ($method === 'DELETE') {
      if ($c['orcid'] !== $me['orcid'] && !$me['isAdmin']) fail(403, 'Forbidden');
      // replies go with their thread, as with ON DELETE CASCADE in the SQLite version
      $s['comments'] = array_values(array_filter($s['comments'], fn ($x) => $x['id'] !== $id && $x['parentId'] !== $id));
      return $s;
    }
    if (array_key_exists('status', $b)) {
      if (!$me['isAdmin']) fail(403, 'Only maintainers can change the status.');
      if (!in_array($b['status'], COMMENT_STATUSES, true) || $c['parentId'] !== null) fail(400, 'Invalid status');
      $c['status'] = $b['status'];
      $c['updatedAt'] = now();
    }
    if (array_key_exists('body', $b)) {
      if ($c['orcid'] !== $me['orcid']) fail(403, 'You can only edit your own comments.');
      $text = is_string($b['body']) ? trim($b['body']) : '';
      if ($text === '' || text_length($text) > 5000) fail(400, 'Comment must be between 1 and 5000 characters.');
      $c['body'] = $text;
      $c['updatedAt'] = now();
    }
    $s['comments'][$i] = $c;
    return $s;
  });
  if ($method === 'DELETE') json_out(['ok' => true]);
  json_out(['comment' => to_dto(find_comment($s, $id), $s, $me)]);
}

if ($route === 'admin/export' && $method === 'GET') {
  $token = cfg()['admin_token'];
  $given = preg_replace('/^Bearer\s+/i', '', (string) ($_SERVER['HTTP_AUTHORIZATION'] ?? $_SERVER['REDIRECT_HTTP_AUTHORIZATION'] ?? ''));
  if ($token === '' || !hash_equals($token, (string) $given)) fail(403, 'Forbidden');
  json_out(read_store());
}

fail(404, 'Not found');

// Local development only: needs the config flag AND a request from this machine.
function dev_login_allowed(): bool {
  return cfg()['dev_login'] === true && in_array($_SERVER['REMOTE_ADDR'] ?? '', ['127.0.0.1', '::1'], true);
}

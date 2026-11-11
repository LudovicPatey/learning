<?php
// Router for `php -S` in tests/php-api.test.ts: plays the role of api/.htaccess,
// which sends every URL under /api/ to the remarks server.
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
if (strpos($path, '/api/') === 0) {
  require __DIR__ . '/../../deploy/api/index.php';
  return true;
}
return false;

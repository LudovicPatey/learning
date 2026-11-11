<?php
// Router for `npm run preview:static`: serves out/ with PHP's built-in server as the
// web hosting does (docs/DEPLOY.md). It plays the role of the .htaccess files: /api/*
// goes to the remarks server, with deploy/preview-config.php (dev login, remarks
// stored in cache/preview-data/); the rest is served from out/.
putenv('LEARNING_CONFIG=' . __DIR__ . '/preview-config.php');
$out = dirname(__DIR__) . '/out';
$path = (string) parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
if (strpos($path, '/api/') === 0) {
  require $out . '/api/index.php';
  return true;
}
if (is_dir($out . $path) && substr($path, -1) !== '/') {
  header('Location: ' . $path . '/', true, 301);
  return true;
}
if (is_file($out . $path) || is_file($out . rtrim($path, '/') . '/index.html')) return false;
http_response_code(404);
readfile($out . '/404.html');
return true;

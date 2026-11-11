<?php
// Configuration of the remarks server for `npm run preview:static` (local only).
return [
  'data_dir' => dirname(__DIR__) . '/cache/preview-data',
  'lessons_json' => dirname(__DIR__) . '/out/api/lessons.json',
  'dev_login' => true,
  'admin_orcids' => ['0000-0002-1825-0097'],
];

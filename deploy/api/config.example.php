<?php
// Configuration of the remarks server. Copy to config.php ON THE SERVER (next to
// this file) and fill in; config.php is never committed nor uploaded by the
// deployment. See docs/DEPLOY.md.
return [
  // ORCID public API client (https://orcid.org/developer-tools), with the
  // redirect URI  https://<site>/api/auth/orcid/callback
  'orcid_client_id' => 'APP-XXXXXXXXXXXXXXXX',
  'orcid_client_secret' => 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
  // 'orcid_base' => 'https://sandbox.orcid.org',   // ORCID's test server

  // ORCID iDs of the maintainers, who can change the status of remarks and delete them.
  'admin_orcids' => [],

  // Long random string, to download all remarks with GET /api/admin/export
  // (php -r 'echo bin2hex(random_bytes(24)), "\n";'). Empty: export disabled.
  'admin_token' => '',

  // Where remarks and sessions are stored: OUTSIDE the web root.
  // Default: two levels above api/, i.e. next to the site's folder on OVH hosting.
  // 'data_dir' => '/home/LOGIN/learning-data',

  // Public address of the site, if it cannot be guessed (proxies…).
  // 'site_url' => 'https://learning.example.org',

  // Local development only: allows /api/auth/dev-login from this machine (never on a server).
  // 'dev_login' => true,
];

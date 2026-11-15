import fs from "node:fs";
import path from "node:path";
import Database from "better-sqlite3";

// Schema migrations, applied in order. Append new ones; never edit old ones.
const MIGRATIONS: string[] = [
  `
  CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    orcid TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    last_login_at TEXT
  );
  CREATE TABLE sessions (
    token_hash TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    expires_at TEXT NOT NULL
  );
  CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    lesson_id TEXT NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(id),
    parent_id INTEGER REFERENCES comments(id) ON DELETE CASCADE,
    kind TEXT NOT NULL DEFAULT 'suggestion',
    body TEXT NOT NULL,
    anchor TEXT,               -- JSON text-quote selector, null for replies
    content_hash TEXT,         -- version of the lesson source when the comment was made
    status TEXT NOT NULL DEFAULT 'open',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
  );
  CREATE INDEX comments_lesson ON comments(lesson_id, created_at);
  CREATE INDEX comments_parent ON comments(parent_id);
  `,
  `
  -- "I have checked this exercise and its solution"; content_hash is the version checked
  CREATE TABLE endorsements (
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    exercise_id TEXT NOT NULL,
    content_hash TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    PRIMARY KEY (user_id, exercise_id)
  );
  CREATE INDEX endorsements_exercise ON endorsements(exercise_id);
  CREATE INDEX comments_user ON comments(user_id, created_at);
  `,
];

function migrate(db: Database.Database) {
  const current = db.pragma("user_version", { simple: true }) as number;
  for (let v = current; v < MIGRATIONS.length; v++) {
    db.transaction(() => {
      db.exec(MIGRATIONS[v]);
      db.pragma(`user_version = ${v + 1}`);
    })();
  }
}

// The connection survives hot reloads of the development server, which may bring new
// migrations: they are applied to the open connection as well.
const g = globalThis as unknown as { __db?: Database.Database; __dbMigrations?: number };

export function db(): Database.Database {
  if (!g.__db) {
    const file = process.env.DATABASE_PATH ?? path.join(process.cwd(), "data", "app.db");
    fs.mkdirSync(path.dirname(file), { recursive: true });
    const conn = new Database(file);
    conn.pragma("journal_mode = WAL");
    conn.pragma("foreign_keys = ON");
    g.__db = conn;
  }
  if (g.__dbMigrations !== MIGRATIONS.length) {
    migrate(g.__db);
    g.__dbMigrations = MIGRATIONS.length;
  }
  return g.__db;
}

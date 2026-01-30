import sqlite3
from typing import List, Dict, Any

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
"""

def get_connection(db_path: str = 'data.db'):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: str = 'data.db'):
    conn = get_connection(db_path)
    with conn:
        conn.executescript(CREATE_USERS_TABLE)
    conn.close()

def insert_user(name: str, email: str, db_path: str = 'data.db') -> int:
    conn = get_connection(db_path)
    with conn:
        cur = conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        return cur.lastrowid

def get_users(db_path: str = 'data.db') -> List[Dict[str, Any]]:
    conn = get_connection(db_path)
    cur = conn.execute("SELECT id, name, email FROM users")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

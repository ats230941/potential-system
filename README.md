# SQLite database (Python)

This workspace contains a minimal example that creates a SQLite database `data.db` and a `users` table.

Quick start

- Initialize the database:

```bash
python create_db.py
```

- Use the helper in `db.py` to insert and query users:

```python
from db import insert_user, get_users

insert_user('Alice', 'alice@example.com')
print(get_users())
```

Next steps

- Add migrations (e.g. Alembic) for schema management.
- Replace SQLite with PostgreSQL for production.
- Wrap DB access with a higher-level ORM like SQLAlchemy if desired.

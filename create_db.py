import os
from db import init_db

def main():
    root = os.path.dirname(__file__)
    db_path = os.path.join(root, 'data.db')
    init_db(db_path)
    print(f"Database created at {db_path}")

if __name__ == '__main__':
    main()

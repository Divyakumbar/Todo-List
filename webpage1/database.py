import sqlite3
conn=sqlite3.connect("todo.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    list TEXT NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
    username TEXT NOT NULL,
    email  TEXT NOT NULL,
    number INTEGER NOT NULL,
    password INTEGER NOT NULL
)
""")
conn.commit()
conn.close()

print("Database created successfully")
               
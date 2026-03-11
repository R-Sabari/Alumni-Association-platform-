import sqlite3

conn = sqlite3.connect("alumni.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE alumni(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
year TEXT,
department TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")
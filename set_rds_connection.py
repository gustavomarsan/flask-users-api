import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host="flask-users-db.co9aem0eaes9.us-east-1.rds.amazonaws.com",
    database="usersdb",
    user="postgres",
    password="Blusi701",
    port=5432
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);
""")

print("✅ Users table created in 'usersdb'!")

cursor.close()
conn.close()
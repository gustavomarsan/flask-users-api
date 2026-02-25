from db import get_connection
from psycopg2.errors import UniqueViolation

def create_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id, name, email;",
            (name, email)
        )

        new_user = cursor.fetchone()
        conn.commit()

        return new_user

    except UniqueViolation:
        conn.rollback()
        return "duplicate" 
    
    finally:
        cursor.close()
        conn.close()

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email FROM users ORDER BY id;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {"id": r[0], "name": r[1], "email": r[2]}
        for r in rows
    ]

def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email FROM users WHERE id = %s;",
        (user_id,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None

    return {"id": row[0], "name": row[1], "email": row[2]}

def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = %s RETURNING id;",
        (user_id,)
    )

    deleted = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if deleted is None:
        return None

    return user_id

def update_user(user_id: int, name: str, email: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING id, name, email;",
            (name, email, user_id)
        )

        updated = cursor.fetchone()
        conn.commit()

        if updated is None:
            return None

        return updated  

    except UniqueViolation:
        conn.rollback()
        return "duplicate"
    
    finally:
        cursor.close()
        conn.close()
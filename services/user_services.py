"""
Docstring for services.services
Todo: Set the business logic here, separate from the route handling and data storage for better organization
"""

from models.user import users, next_id

def get_all_users():
    return users


def get_user_by_id(user_id):
    return next((u for u in users if u["id"] == user_id), None)


def create_user(name):
    global next_id
    new_user = {
        "id": next_id,
        "name": name
    }
    users.append(new_user)
    next_id += 1
    return new_user


def update_user(user_id, name):
    user = get_user_by_id(user_id)
    if not user:
        return None
    user["name"] = name
    return user


def delete_user(user_id):
    global users
    user = get_user_by_id(user_id)
    if not user:
        return False
    users = [u for u in users if u["id"] != user_id]
    return True


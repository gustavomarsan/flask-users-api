from flask import Blueprint, request, jsonify
from email_validator import validate_email, EmailNotValidError
from services.user_services import (
    get_all_users,
    get_user_by_id,
    create_user,
    delete_user,
    update_user,
)

users_bp = Blueprint("users", __name__)


def is_valid_email(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False    

@users_bp.route("/api/users", methods=["GET"])
def route_get_users():
    return jsonify(get_all_users()), 200


@users_bp.route("/api/users/<int:user_id>", methods=["GET"])
def route_get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


@users_bp.route("/api/users", methods=["POST"])
def route_create_user():    
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400
    
    if not is_valid_email(data["email"]):
        return jsonify({"error": "Invalid email format"}), 400
    
    new_user = create_user(data["name"], data["email"])

    if new_user == "duplicate":
        return jsonify({"error": "Email already exists"}), 409 # Conflict
    
    return jsonify(new_user), 201


@users_bp.route("/api/users/<int:user_id>", methods=["PUT"])
def route_update_user(user_id):
    data = request.get_json()


    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400

    updated_user = update_user(user_id, data["name"], data["email"])

    if not updated_user:
        return jsonify({f"error": f"User with ID {user_id} not found"}), 404
    
    if updated_user == "duplicate":
        return jsonify({"error": "Email already exists"}), 409 # Conflict

    return jsonify(updated_user), 200


@users_bp.route("/api/users/<int:user_id>", methods=["DELETE"])
def route_delete_user(user_id):
    deleted = delete_user(user_id)

    if not deleted:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200

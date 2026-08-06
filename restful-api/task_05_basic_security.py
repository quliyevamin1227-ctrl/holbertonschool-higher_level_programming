#!/usr/bin/python3
"""Basic security with Flask"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password."""
    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        return username

    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic auth protected route."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login and return JWT."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if user is None or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)

    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT protected route."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Admin only route."""
    username = get_jwt_identity()

    if users[username]["role"] != "admin":
        return jsonify({
            "error": "Admin access required"
        }), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def unauthorized_callback(error):
    """Handle missing token."""
    return jsonify({
        "error": "Missing or invalid token"
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """Handle invalid token."""
    return jsonify({
        "error": "Invalid token"
    }), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    """Handle expired token."""
    return jsonify({
        "error": "Token has expired"
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    """Handle revoked token."""
    return jsonify({
        "error": "Token has been revoked"
    }), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(jwt_header, jwt_payload):
    """Handle fresh token required."""
    return jsonify({
        "error": "Fresh token required"
    }), 401


if __name__ == "__main__":
    app.run()

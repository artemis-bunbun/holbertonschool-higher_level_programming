#!/usr/bin/python3
"""Flask API with Basic Auth, JWT, and role-based access control."""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials against stored users."""
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Return 401 when no JWT token is provided."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Return 401 when an invalid JWT token is provided."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    """Return 401 when the JWT token has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Return 401 when the JWT token has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Return 401 when a fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message for successfully authenticated Basic Auth users."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Accept JSON credentials and return a JWT token if valid."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if username not in users or not check_password_hash(
        users[username]["password"], password
    ):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(
        identity=username, additional_claims={"role": users[username]["role"]}
    )
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message for successfully authenticated JWT users."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return a message only for admin users, or 403 otherwise."""
    claims = get_jwt_identity()
    role = users.get(claims, {}).get("role")
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'Hola'
jwt = JWTManager(app)

user_password = {
      "user1": {"username": "user1", "password": generate_password_hash("user1password"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in user_password and check_password_hash(user_password[username]['password'], password):
        return username

@app.route('/')
def home():
    return "Hello!"

@app.route('/basic-protected')
@auth.login_required
def basic():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    data_users = request.get_json()
    username = data_users['username']
    password = data_users['password']

    if not user_password or not check_password_hash(user_password[username]['password'], password):
        return {"error": "access denied"}, 401
    token = create_access_token(identity={'username': username, 'role': user_password[username]['role']})
    return {"access_token": token}, 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.route('/admin-only')
@jwt_required()
def admin():
    curren = get_jwt_identity()
    role = curren['role']

    if role != 'admin':
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted", 200

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()

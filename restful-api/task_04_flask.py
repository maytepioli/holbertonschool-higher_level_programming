from flask import Flask, jsonify, request

app = Flask(__name__)

usuario = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    name_user = list(usuario.keys())
    return jsonify(name_user)

@app.route('/status')
def status():
    return 'OK'


@app.route('/users/<username>', methods=["GET"])
def users(username):
    user = usuario.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify('users no fund'), 404

@app.route('/add_user', methods=["POST"])
def add_data():
    data_user = request.get_json()
    username = data_user.get('username')
    name = data_user["name"]
    age = data_user["age"]
    city = data_user["city"]

    if not username:
        return jsonify({"error": "Username is required"}), 400

    usuario[username] = {
        'username': username,
        'name': name,
        'age': age,
        'city': city
    }

    return jsonify({"message": "User added","user": usuario[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)

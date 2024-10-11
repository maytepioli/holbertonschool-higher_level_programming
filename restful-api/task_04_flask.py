from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify(users)

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def users(username):
    user = users.get(username)
    if user:
        return jsonify(users[username]), 200
    else:
        return jsonify('users no fund'), 404
if __name__ == "__main__":
    app.run()





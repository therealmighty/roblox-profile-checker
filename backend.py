from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/userid', methods=['POST'])
def get_user_id():
    data = request.json
    usernames = data.get('usernames', [])
    r = requests.post("https://users.roblox.com/v1/usernames/users", json={"usernames": usernames})
    return jsonify(r.json())

@app.route('/api/user/<int:user_id>')
def get_user_info(user_id):
    r = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
    return jsonify(r.json())

@app.route('/api/groups/<int:user_id>')
def get_user_groups(user_id):
    r = requests.get(f"https://groups.roblox.com/v2/users/{user_id}/groups/roles")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

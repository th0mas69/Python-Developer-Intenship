from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store: {user_id: {name: str, email: str}}
users = {}

# Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Route: Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# Route: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    user_id = data['id']
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 409

    users[user_id] = {'name': data['name'], 'email': data['email']}
    return jsonify({'message': 'User created'}), 201

# Route: Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    users[user_id].update({
        'name': data.get('name', users[user_id]['name']),
        'email': data.get('email', users[user_id]['email'])
    })
    return jsonify({'message': 'User updated'}), 200

# Route: Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

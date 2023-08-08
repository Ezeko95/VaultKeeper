from flask import Flask, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/password-manager"
mongo = PyMongo(app)

@app.route("/user_register", methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    if username and password and email:
        hashed_password = generate_password_hash(password)
        user_id = mongo.db.users.insert_one(
            {'username': username, 'email': email, 'password': hashed_password}
        )
        response = {
            'user_id': str(user_id.inserted_id),
            'username': username,
            'password': hashed_password,
            'email': email
        }
        return jsonify(response)
    else:
        return jsonify({'message': 'fields incomplete'})

@app.route("/user_login", methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']
    if email and password:
        user_data = mongo.db.users.find_one({'email': email})
        if user_data and check_password_hash(user_data['password'], password):
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Login failed'})
    
###################################################################





if __name__ == '__main__':
    app.run(debug=True)


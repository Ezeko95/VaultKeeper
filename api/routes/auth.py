from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify, current_app
from flask_pymongo import PyMongo
import datetime
import jwt


auth = Blueprint('auth', __name__)



@auth.route("/user_register", methods=['POST'])
def create_user():
    with current_app.app_context():
        mongo = PyMongo(current_app)
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    if username and password and email:
        hashed_password = generate_password_hash(password)
        user_id = mongo.db.users.insert_one(
            {'username': username, 'email': email, 'password': hashed_password}
        )
        print(user_id)
        return jsonify({'message': 'Registration succesful!'})
    else:
        return jsonify({'message': 'fields incomplete'})

@auth.route("/user_login", methods=['POST'])
def login_user():
    with current_app.app_context():
        mongo = PyMongo(current_app)
        secret_key = current_app.config.get("SECRET_KEY")
    email = request.json['email']
    password = request.json['password']
    if email and password:
        user_data = mongo.db.users.find_one({'email': email})
        if user_data and check_password_hash(user_data['password'], password):
            token = jwt.encode({'user_id': str(user_data['_id']), 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, secret_key, algorithm='HS256')
            return jsonify({'message': 'Login successful', 'token': token})
        else:
            return jsonify({'message': 'Login failed'})
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from bson import ObjectId
import datetime
import jwt
import os

load_dotenv() # Enviroment variables

app = Flask(__name__)

# Enviroment variables for configuration
secret_key = os.environ.get('SECRET_KEY')
mongo_uri = os.environ.get('MONGO_URI')

# app configuration using enviroment variables
app.config["SECRET_KEY"] = secret_key
app.config["MONGO_URI"] = mongo_uri

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
        print(user_id)
        return jsonify({'message': 'Registration succesful!'})
    else:
        return jsonify({'message': 'fields incomplete'})

@app.route("/user_login", methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']
    if email and password:
        user_data = mongo.db.users.find_one({'email': email})
        if user_data and check_password_hash(user_data['password'], password):
            token = jwt.encode({'user_id': str(user_data['_id']), 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'message': 'Login successful', 'token': token})
        else:
            return jsonify({'message': 'Login failed'})
    

@app.route("/vault", methods=['POST'])
def store_account():
    user_id = request.json['user_id']
    site = request.json['site']
    username = request.json['username']
    password = request.json['password']
    
    if user_id and site and username and password:
        user_id_obj = ObjectId(user_id)  # Convert user_id string to ObjectId
        hashed_password = generate_password_hash(password)
        account_data = {
            "user_id": user_id_obj,  
            "site": site,
            "username": username,
            "password": hashed_password
        }
        mongo.db.account_data.insert_one(account_data)
        return jsonify({'message': 'account stored successfully'})
    else:
        return jsonify({'message': 'Fields incomplete'})

@app.route("/vault/<user_id>", methods=['GET'])
def get_user_accounts(user_id):
    account_data = mongo.db.account_data.find({'user_id': user_id}, {'_id': 0})
    accounts = list(account_data)
    return jsonify(accounts)


if __name__ == '__main__':
    app.run(debug=True)


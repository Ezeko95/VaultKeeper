from flask import Flask, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
import jwt
import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/password-manager"
mongo = PyMongo(app)
app.config["SECRET_KEY"] = "wake-up-Neo"


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
    
###################################################################

@app.route("/vault", methods=['POST'])
def store_password():
    user_id = request.json['user_id']
    site = request.json['site']
    username = request.json['username']
    password = request.json['password']
    
    if user_id and site and username and password:
        account_data = {
            "user_id": user_id,
            "site": site,
            "username": username,
            "password": password
        }
        mongo.db.passwords.insert_one(account_data)
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


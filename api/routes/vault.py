from flask import jsonify, Blueprint, request, current_app, g
from bson import ObjectId
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
import jwt
from functools import wraps


vault = Blueprint('vault', __name__)



def authenticate(func):
    with current_app.app_context():
        secret_key = current_app.config.get("SECRET_KEY")
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token missing'}), 401

        try:
            decoded_token = jwt.decode(token, secret_key, algorithms=['HS256']) 
            g.user_id = decoded_token['user_id']  # Storing user_id in Flask's "g" object!
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 401
        except jwt.DecodeError:
            return jsonify({'message': 'Invalid token'}), 401
    return wrapper

@vault.before_request
def check_authentication():
    with current_app.app_context():
        secret_key = current_app.config.get("SECRET_KEY")
    excluded_endpoints = ['auth.create_user', 'auth.login_user']
    
    if request.endpoint not in excluded_endpoints:
        authenticate_required = True
        try:
            token = request.headers.get('Authorization')
            decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
            g.user_id = decoded_token['user_id']
        except (jwt.ExpiredSignatureError, jwt.DecodeError):
            authenticate_required = False

        if not authenticate_required:
            return jsonify({'message': 'Authentication required'}), 401

@vault.route("/", methods=['POST'])
def store_account():
    with current_app.app_context():
        secret_key = current_app.config.get("SECRET_KEY")
        mongo = PyMongo(current_app)
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
    
@vault.route("/<user_id>", methods=['GET'])
def get_user_accounts(user_id):
    with current_app.app_context():
        mongo = PyMongo(current_app)
    account_data = mongo.db.account_data.find({'user_id': user_id}, {'_id': 0})
    accounts = list(account_data)
    return jsonify(accounts)

@vault.route("/<user_id>/<site>", methods=['PUT'])
def update_account(user_id, site):
    with current_app.app_context():
        mongo = PyMongo(current_app)
    new_site = request.json.get('new_site')
    new_username = request.json.get('new_username')
    new_password = request.json.get('new_password')

    if new_site or new_username or new_password:
        query = {'user_id': user_id, 'site': site}
        updates = {}
        if new_site:
            updates['site'] = new_site
        if new_username:
            updates['username'] = new_username
        if new_password:
            updates['password'] = generate_password_hash(new_password)

        result = mongo.db.account_data.update_one(query, {'$set': updates})
        
        if result.modified_count > 0:
            return jsonify({'message': 'Account updated successfully'})
        else:
            return jsonify({'message': 'No changes made'})
    else:
        return jsonify({'message': 'No valid data provided'})

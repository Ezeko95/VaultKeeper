from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from routes.auth import auth
from routes.vault import vault



load_dotenv() # Enviroment variables

app = Flask(__name__)

# Enviroment variables for configuration
secret_key = os.environ.get('SECRET_KEY')
mongo_uri = os.environ.get('MONGO_URI')

# app configuration using enviroment variables
app.config["SECRET_KEY"] = secret_key
app.config["MONGO_URI"] = mongo_uri

mongo = PyMongo(app)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(vault, url_prefix='/vault')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)


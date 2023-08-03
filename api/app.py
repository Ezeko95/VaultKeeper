from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/vault', methods=['GET'])
def hello():
    message = {'message': 'Hello, this is a Flask route!'}
    return jsonify(message), 200

if __name__ == '__main__':
    app.run(debug=True)

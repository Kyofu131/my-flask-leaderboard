from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from waitress import serve
import os

app = Flask(__name__, static_folder='static')
CORS(app)

leaderboard = []

@app.route('/')
def home():
    return "Welcome to the Flask Leaderboard App!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')
    if name and score is not None:
        leaderboard.append({'name': name, 'score': score})
        return jsonify({'message': 'Score submitted successfully!'}), 200
    return jsonify({'message': 'Invalid data'}), 400

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    return jsonify(sorted_leaderboard)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

leaderboard = []

@app.route('/')
def home():
    app.logger.debug('Home route called')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    app.logger.debug('Favicon route called')
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')
    app.logger.debug(f'Submit score called with name={name} and score={score}')
    if name and score is not None:
        leaderboard.append({'name': name, 'score': score})
        return jsonify({'message': 'Score submitted successfully!'}), 200
    return jsonify({'message': 'Invalid data'}), 400

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    app.logger.debug('Leaderboard route called')
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    return jsonify(sorted_leaderboard)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes

leaderboard = []

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
    # Sort leaderboard by score in descending order
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    return jsonify(sorted_leaderboard)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, jsonify
import json
import random

# Create the Flask App
app = Flask(__name__)

# Load questions from questions.JSON File
def load_questions():
    with open('questions.json', 'r') as f:
        return json.load(f)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to get a random question
@app.route('/api/question')
def get_question():
    questions_data = load_questions()

    # Choose a random category
    categories = list(questions_data['categories'].keys())
    selected_category = random.choice(categories)

    # Choose a random question from that category
    question = random.choice(questions_data['categories'][selected_category])

    # Return as JSON
    return jsonify({
        'category': selected_category,
        'question': question['question'],
        'options': question['options'],
        'difficulty': question['difficulty']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

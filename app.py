from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask!'

@app.route('/api')
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/todo')
def todo():
    return render_template('todo.html')

client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
collection = db['todo_items']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    if not item_name or not item_description:
        return jsonify({'error': 'Both fields required'}), 400
    result = collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })
    return jsonify({'message': 'Item saved', 'id': str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)

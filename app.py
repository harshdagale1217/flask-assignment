from flask import Flask, jsonify, render_template, request
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

if __name__ == '__main__':
    app.run(debug=True)

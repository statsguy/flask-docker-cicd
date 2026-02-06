from flask import Flask, jsonify

import os


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Flask!",
        "environment": os.getenv("ENV", "development"),
        "version": "1.0.0"
    })


@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({
        "operation": "addition",
        "a": a,
        "b": b,
        "result": a + b
    })


@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return jsonify({
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": a - b
    })


@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return jsonify({
        "operation": "multiplication",
        "a": a,
        "b": b,
        "result": a * b
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv("ENV") != "production")

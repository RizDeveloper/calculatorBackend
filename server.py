from flask import Flask, request
from flask_cors import CORS
from calculator import calculate

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/api/calculate', methods=['POST'])
def calculate_route():
    return calculate(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

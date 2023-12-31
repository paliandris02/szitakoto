from flask import Flask, request, jsonify
from src.revel.main import Estimate
from flask_cors import CORS

app: Flask = Flask(__name__)

allowed_origins = ['http://localhost:8080', 'http://andraspali.me']
CORS(app, resources={r"/estimate": {"origins": allowed_origins}})

@app.route("/")
def index():
    return "default page"

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.get_json(force=True)
    calculated_estimation = Estimate(data)
    return jsonify(calculated_estimation)


if __name__ == '__main__':
    app.run(port=5000)

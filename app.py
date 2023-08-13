from datetime import datetime
from flask import Flask, request, jsonify
from revel.main import Estimate

app: Flask = Flask(__name__)

@app.route('/estimate', methods=['POST'])
def estimate():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    calculated_estimation: int = Estimate(data["value"])
    return jsonify(value=calculated_estimation)


if __name__ == '__main__':
    app.run(debug=True)

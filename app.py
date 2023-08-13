from datetime import datetime
from flask import Flask, request, jsonify
from revel.main import Estimate

app: Flask = Flask(__name__)


@app.route('/get_time')
def get_time():
    now = datetime.utcnow()
    return jsonify(time=now)


@app.route('/estimate', methods=['POST'])
def estimate():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    calculatedEstimation = Estimate(data["value"])
    return jsonify(value=calculatedEstimation)


if __name__ == '__main__':
    app.run(debug=True)

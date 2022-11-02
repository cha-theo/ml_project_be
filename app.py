from flask import Flask, jsonify
from flask_cors import CORS
from controllers import ping_controller, stats_controller, models_controller

app = Flask(__name__)
CORS(app)

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Server Error"}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400

app.register_blueprint(ping_controller.api)
app.register_blueprint(stats_controller.api)
app.register_blueprint(models_controller.api)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
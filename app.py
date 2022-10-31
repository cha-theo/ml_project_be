from flask import Flask, jsonify
from flask_cors import CORS
from controllers import ping_controller, stats_controller, models_controller

app = Flask(__name__)
CORS(app)



app.register_blueprint(ping_controller.api)
app.register_blueprint(stats_controller.api)
app.register_blueprint(models_controller.api)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
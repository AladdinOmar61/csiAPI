# Imports
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

# Config
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Routes
@app.route("/")
def root():
    return jsonify("Welcome to the CSI API")

@app.route("/api/generate-plate", methods=["GET"])
def generete():
    Plate = "ABC 3244"

    # Generate a license plate and return it

    # NYC license plate
    # 3 Letters - 4 Numbers
    
    # allow a user to select how many plates they would want to generate

    return jsonify(Plate)

# init
if __name__ == "__main__":
    port = os.getenv("FLASK_APP_PORT")
    host = os.getenv("FLASK_APP_HOST")
    app.run(debug=True, host=host, port=port)

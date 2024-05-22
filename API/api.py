from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os, random, string

load_dotenv() # loads .env file

# Config
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Routes
@app.route("/api")
def root():
    return jsonify("Welcome to the CSI API")


def generate_license_plate():
    letters = "".join(random.choices(string.ascii_uppercase, k=3))
    numbers = "".join(random.choices(string.digits, k=4))
    return f"{letters} {numbers}"


@app.route("/api/generate-license-plate", methods=["GET"])
def generate():
    return jsonify(generate_license_plate())


@app.route("/api/generate-license-plate/<int:numPlates>", methods=["GET"])
def generate_num_plates(numPlates):
    plates = [generate_license_plate() for _ in range(numPlates)]
    return jsonify({"NY License Plates": [{"Plate": plate} for plate in plates]})


# init
if __name__ == "__main__":
    port = os.getenv("FLASK_APP_PORT", 5000)
    host = os.getenv("FLASK_APP_HOST", '0.0.0.0')
    app.run(debug=True, host=host, port=port)

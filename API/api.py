from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os, random, string

load_dotenv() # loads .env file

# Config
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Routes
@app.route("/")
def root():
    return jsonify("Welcome to the CSI API")

def generate_license_plate():
    letters = "".join(random.choices(string.ascii_uppercase, k=3))
    numbers = "".join(random.choices(string.digits, k=4))
    return f"{letters} {numbers}"

@app.route("/api/generate-license-plate", methods=["GET"])
def generate():
    return jsonify(generate_license_plate())


@app.route("/api/generate-license-plates/<int:numPlates>", methods=["GET"])
# def generate_num_plates(numPlates):
#     plates = [generate_license_plates() for _ in range(numPlates)]
#     return jsonify({"NY License Plates": plates})

def generate_license_plates(numPlates):
  counter = 0
  cars = []
  # make a temp array where we store the same car
  temp = []
  while counter < numPlates:
      status = 'A'
      letters = "".join(random.choices(string.ascii_uppercase, k=3))
      numbers = "".join(random.choices(string.digits, k=4))
      plate = f"{letters} {numbers}"
      carData = {
          "Plate": plate,
          "Status": status
      }
      carDataDupe = {
          "Plate": plate,
          "Status": 'D'
      }
      # problem: what if I dont want it to show up immediately after the arrival
      # potential solution: add a delay (random val between curr index and length) between the arrival and departure
      cars.append(carData)
      counter += 1
      temp.append(carDataDupe)
      # generate a random number between len of arr and numPlates
      randomIndex = random.randint(len(cars), numPlates) 
      # when that num is the same as the length of the array, add the cars to the main array
      if len(cars) == randomIndex and len(cars) > 0:
          cars = cars + temp
          counter += len(temp)
          # clear the temp array
          temp.clear()
      # remove extra cars past the length of numplates
      while len(cars) > numPlates:
        cars.pop()
  return cars

# init
if __name__ == "__main__":
    port = os.getenv("FLASK_APP_PORT", 5000)
    host = os.getenv("FLASK_APP_HOST", '0.0.0.0')
    app.run(debug=True, host=host, port=port)
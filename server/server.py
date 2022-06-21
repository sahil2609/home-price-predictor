from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print("hii")
    return response

@app.route('/predict_home_price', methods= ['GET', 'POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bath = request.form['bath']
    bhk = request.form['bhk']

    response = jsonify({
        'predicted_price' : util.predict_price(location, sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
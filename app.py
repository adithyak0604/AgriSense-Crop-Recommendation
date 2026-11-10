from flask import Flask, render_template, request, jsonify
from crop_predict import CropRecommender

app = Flask(__name__)

# Load the trained model once when the application starts
recommender = CropRecommender()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get JSON data from frontend
        data = request.get_json()

        # Extract values
        n = float(data["n"])
        p = float(data["p"])
        k = float(data["k"])
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
        ph = float(data["ph"])
        rainfall = float(data["rainfall"])
        season = data["season"]

        # Make prediction
        result = recommender.predict(
            n=n,
            p=p,
            k=k,
            temp=temperature,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall,
            season=season
        )

        return jsonify({
            "success": True,
            "data": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
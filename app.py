from flask import Flask, render_template, request
import numpy as np
import joblib
import tensorflow as tf

app = Flask(__name__)

# ============================================================
# Load AI Model and Scaler
# ============================================================

model = tf.keras.models.load_model("best_model.keras")
scaler = joblib.load("scaler.pkl")


# ============================================================
# Home Page
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# Prediction
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ----------------------------------------------------
        # Read Inputs
        # ----------------------------------------------------

        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        wind_speed = float(request.form["wind_speed"])
        cloud_cover = float(request.form["cloud_cover"])
        pressure = float(request.form["pressure"])

        # ----------------------------------------------------
        # Prepare Input
        # ----------------------------------------------------

        input_data = np.array([[
            temperature,
            humidity,
            wind_speed,
            cloud_cover,
            pressure
        ]])

        input_scaled = scaler.transform(input_data)

        # ----------------------------------------------------
        # Model Prediction
        # ----------------------------------------------------

        probability = model.predict(input_scaled, verbose=0)[0][0]

        if probability >= 0.5:
            prediction = "Rainy"
            weather_icon = "🌧"
            confidence = probability
        else:
            prediction = "Sunny"
            weather_icon = "☀️"
            confidence = 1 - probability

        confidence = round(confidence * 100, 2)

        # ----------------------------------------------------
        # AI Weather Summary
        # ----------------------------------------------------

        if prediction == "Sunny":

            summary = (
                "The atmospheric conditions indicate clear skies "
                "with a very low probability of rainfall."
            )

            recommendation = [
                "😎 Wear sunglasses",
                "💧 Stay hydrated",
                "🚶 Great day for outdoor activities",
                "☀️ UV level may be high"
            ]

            weather_color = "#FFD54F"

        else:

            summary = (
                "The atmospheric conditions indicate rainy weather "
                "with a high probability of precipitation."
            )

            recommendation = [
                "☔ Carry an umbrella",
                "🚗 Drive carefully",
                "🌧 Roads may be slippery",
                "🧥 Consider wearing a raincoat"
            ]

            weather_color = "#42A5F5"

        # ----------------------------------------------------
        # Weather Probabilities
        # ----------------------------------------------------

        if prediction == "Sunny":
            sunny_probability = confidence
            rainy_probability = round(100 - confidence, 2)
        else:
            rainy_probability = confidence
            sunny_probability = round(100 - confidence, 2)

        # ----------------------------------------------------
        # Render Result Page
        # ----------------------------------------------------

        return render_template(
            "result.html",
            prediction=prediction,
            weather_icon=weather_icon,
            confidence=confidence,
            temperature=temperature,
            humidity=humidity,
            wind_speed=wind_speed,
            cloud_cover=cloud_cover,
            pressure=pressure,
            summary=summary,
            recommendation=recommendation,
            sunny_probability=sunny_probability,
            rainy_probability=rainy_probability,
            weather_color=weather_color
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


# ============================================================
# Predict Again
# ============================================================

@app.route("/home")
def back_home():
    return render_template("index.html")


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
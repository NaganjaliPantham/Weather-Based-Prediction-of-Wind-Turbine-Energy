from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)

API_KEY = "6800ab3d0c54e1a4de15a39e12bb5b37"

CITIES = [
    "Agartala", "Ahmedabad", "Bengaluru", "Bhopal", "Bhubaneswar",
    "Chandigarh", "Chennai", "Coimbatore", "Delhi", "Guwahati",
    "Hyderabad", "Indore", "Jaipur", "Kochi", "Kolkata",
    "Lucknow", "Madurai", "Mumbai", "Nagpur", "Patna",
    "Pune", "Raipur", "Ranchi", "Surat", "Trivandrum",
    "Udaipur", "Vadodara", "Vijayawada", "Visakhapatnam",
    "Rajahmundry"
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict-page')
def predict_page():
    return render_template("predict.html", cities=CITIES)

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return render_template("predict.html",
                               error="City not found",
                               cities=CITIES)

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"]
    }

    return render_template("predict.html",
                           weather=weather_data,
                           cities=CITIES)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        wind_speed = float(request.form['wind_speed'])
        motor_torque = float(request.form['motor_torque'])
        rotor_torque = float(request.form['rotor_torque'])

        air_density = 1.225   # kg/m³
        radius = 20           # meters
        area = math.pi * radius ** 2

        theoretical_power = 0.5 * air_density * area * (wind_speed ** 3)

        predicted_power = theoretical_power + (motor_torque * rotor_torque)

        return render_template("predict.html",
                               predicted_power=round(predicted_power, 2),
                               cities=CITIES)

    except:
        return render_template("predict.html",
                               error="Invalid input values",
                               cities=CITIES)

if __name__ == "__main__":
    app.run(debug=True)

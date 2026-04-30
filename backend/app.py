from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

print("Starting Flask App...")

app = Flask(__name__)
CORS(app)

try:
    data = pd.read_csv("india_housing_prices.csv")
    print("CSV Loaded Successfully")
except Exception as e:
    print("Error loading CSV:", e)
    exit()

data = data.fillna({
    "Furnished_Status": "Unfurnished",
    "Parking_Space": "No",
    "Security": "No",
    "Public_Transport_Accessibility": "Medium",
    "Amenities": ""
})

print("Data shape:", data.shape)

data["Furnished_Status"] = data["Furnished_Status"].map({
    "Furnished": 1,
    "Semi-Furnished": 0.5,
    "Unfurnished": 0
}).fillna(0)

data["Parking_Space"] = data["Parking_Space"].map({
    "Yes": 1,
    "No": 0
}).fillna(0)

data["Security"] = data["Security"].map({
    "Yes": 1,
    "No": 0
}).fillna(0)

data["Public_Transport_Accessibility"] = data["Public_Transport_Accessibility"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
}).fillna(1)

data["Amenities"] = data["Amenities"].fillna("")
data["Amenities_Count"] = data["Amenities"].apply(
    lambda x: len([i for i in str(x).split(",") if i.strip() != ""])
)

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print("Error loading model:", e)
    exit()

def get_area_defaults(city):
    area = data[data["City"] == city]

    if len(area) == 0:
        return {
            "schools": 5,
            "hospitals": 2,
            "transport": 1,
            "amenities": 3
        }

    return {
        "schools": int(area["Nearby_Schools"].mean()),
        "hospitals": int(area["Nearby_Hospitals"].mean()),
        "transport": int(area["Public_Transport_Accessibility"].mean()),
        "amenities": int(area["Amenities_Count"].mean())
    }

def calculate_growth(city, age):
    area = data[data["City"] == city]

    base_growth = 0.07

    if len(area) > 0:
        price_std = area["Price_in_Lakhs"].std()
        base_growth += min(price_std / 100, 0.03)

    age_factor = 0.01 if age < 10 else 0.02

    growth_rate = base_growth - age_factor
    return max(growth_rate, 0.04)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        d = request.json

        city = d.get("city")
        bhk = int(d.get("bhk"))
        size = float(d.get("size"))
        furnished = float(d.get("furnished"))
        age = int(d.get("age"))

        defaults = get_area_defaults(city)

        sample = [[
            bhk,
            size,
            furnished,
            age,
            defaults["schools"],
            defaults["hospitals"],
            defaults["transport"],
            defaults["amenities"]
        ]]

        current_price = model.predict(sample)[0]

        growth = calculate_growth(city, age)

        future_price = current_price * ((1 + growth) ** 10)

        import datetime
        base_year = datetime.datetime.now().year

        years = []
        prices = []

        temp_price = current_price
        for i in range(11):
            year = base_year + i
            years.append(year)

            temp_price = temp_price * (1 + growth)
            prices.append(round(float(temp_price), 2))

        score = 5

        if defaults["transport"] == 2:
            score += 2
        if defaults["schools"] > 5:
            score += 1
        if age < 10:
            score += 2

        verdict = "Good Investment" if score >= 7 else "Average"

        return jsonify({
            "current_price": round(float(current_price), 2),
            "future_price": round(float(future_price), 2),
            "growth_rate": round(growth * 100, 2),
            "investment_score": score,
            "verdict": verdict,
            "years": years,
            "prices": prices
        })

    except Exception as e:
        print("Prediction error:", e)
        return jsonify({"error": str(e)})

@app.route("/")
def home():
    return "Backend is Running"

if __name__ == "__main__":
    app.run(debug=True)
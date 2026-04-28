import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

print("Training model...")

data = pd.read_csv("india_housing_prices.csv")

data = data.fillna({
    "Furnished_Status": "Unfurnished",
    "Parking_Space": "No",
    "Security": "No",
    "Public_Transport_Accessibility": "Medium",
    "Amenities": ""
})

data["Furnished_Status"] = data["Furnished_Status"].map({
    "Furnished": 1,
    "Semi-Furnished": 0.5,
    "Unfurnished": 0
}).fillna(0)

data["Parking_Space"] = data["Parking_Space"].map({"Yes": 1, "No": 0}).fillna(0)
data["Security"] = data["Security"].map({"Yes": 1, "No": 0}).fillna(0)

data["Public_Transport_Accessibility"] = data["Public_Transport_Accessibility"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
}).fillna(1)

data["Amenities"] = data["Amenities"].fillna("")
data["Amenities_Count"] = data["Amenities"].apply(
    lambda x: len([i for i in str(x).split(",") if i.strip() != ""])
)

features = [
    "BHK",
    "Size_in_SqFt",
    "Furnished_Status",
    "Age_of_Property",
    "Nearby_Schools",
    "Nearby_Hospitals",
    "Public_Transport_Accessibility",
    "Amenities_Count"
]

X = data[features]
y = data["Price_in_Lakhs"]

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully ✅")
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import pickle

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
y = np.log1p(data["Price_in_Lakhs"])

print("Training model...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_test_real = np.expm1(y_test)
y_pred_real = np.expm1(y_pred)

r2 = r2_score(y_test_real, y_pred_real)
mae = mean_absolute_error(y_test_real, y_pred_real)

print("\n📊 MODEL PERFORMANCE")
print("----------------------")
print("R² Score:", round(r2, 3))
print("MAE:", round(mae, 3), "Lakhs")

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully ✅")
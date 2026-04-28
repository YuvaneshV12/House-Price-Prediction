# 🏠 Smart House Price Predictor + Investment Advisor

A Machine Learning based web application that predicts house prices and provides investment insights based on location and property features.

---

## 🚀 Features

* 📊 Predict current house price
* 📈 Forecast future price (next 2 years)
* ⭐ Investment score with recommendation
* 🗺️ Location-based prediction (City + Locality)
* 📉 3-year price growth visualization (Graph)
* ⚡ Fast predictions using saved ML model (`.pkl`)

---

## 🧠 Tech Stack

### 🔹 Backend

* Python
* Flask
* Scikit-learn (Random Forest)
* Pandas
* Pickle

### 🔹 Frontend

* React.js
* Chart.js
* React Router

---

## 📂 Project Structure

```
House-Price-Predictor/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── model.pkl
│   ├── india_housing_prices.csv
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── Home.js
│   │   ├── Result.js
│   │   ├── Home.css
│   │   ├── Result.css
│   │
│   ├── package.json
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

---

### 🔹 2. Backend Setup

```bash
cd backend
pip install flask flask-cors pandas scikit-learn
```

---

### 🔹 3. Train Model (Only Once)

```bash
python train_model.py
```

👉 This creates:

```
model.pkl
```

---

### 🔹 4. Run Backend

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 🔹 5. Frontend Setup

```bash
cd frontend
npm install
npm install react-router-dom chart.js react-chartjs-2
```

---

### 🔹 6. Run Frontend

```bash
npm start
```

App runs at:

```
http://localhost:3000
```

---

## 📊 Example Input

```json
{
  "city": "Chennai",
  "locality": "T Nagar",
  "bhk": 2,
  "size": 1200,
  "furnished": 1,
  "age": 5
}
```

---

## 📈 Example Output

```
Current Price: ₹ 254.68 Lakhs
Future Price: ₹ 302.59 Lakhs
Growth Rate: 9%
Investment Score: 7
Verdict: Good Investment
```

---
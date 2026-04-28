import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import { useState } from "react";
import Result from "./Result";

function Home() {
  const navigate = useNavigate();

  const [city, setCity] = useState("");
  const [bhk, setBhk] = useState("");
  const [size, setSize] = useState("");
  const [furnished, setFurnished] = useState("");
  const [age, setAge] = useState("");

  const handlePredict = async () => {
    if (!city || !bhk || !size || !furnished || !age) {
      alert("Please fill all fields");
      return;
    }

    try {
      const res = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          city,
          bhk: parseInt(bhk),
          size: parseFloat(size),
          furnished: parseFloat(furnished),
          age: parseInt(age),
        }),
      });

      const data = await res.json();

      navigate("/result", { state: data });

    } catch (error) {
      console.error(error);
      alert("Error connecting to server");
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🏠 Smart House Price Predictor</h1>

      <div style={styles.card}>
        <input
          style={styles.input}
          placeholder="Enter City (e.g., Chennai)"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />

        <select style={styles.input} value={bhk} onChange={(e) => setBhk(e.target.value)}>
          <option value="">Select BHK</option>
          <option value="1">1 BHK</option>
          <option value="2">2 BHK</option>
          <option value="3">3 BHK</option>
        </select>

        <input
          style={styles.input}
          type="number"
          placeholder="Size (sq ft)"
          value={size}
          onChange={(e) => setSize(e.target.value)}
        />

        <select
          style={styles.input}
          value={furnished}
          onChange={(e) => setFurnished(e.target.value)}
        >
          <option value="">Select Furnished Status</option>
          <option value="1">Furnished</option>
          <option value="0.5">Semi-Furnished</option>
          <option value="0">Unfurnished</option>
        </select>

        <input
          style={styles.input}
          type="number"
          placeholder="Age of Property (years)"
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />

        <button style={styles.button} onClick={handlePredict}>
          Predict
        </button>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </Router>
  );
}

export default App;

const styles = {
  container: {
    fontFamily: "Arial",
    textAlign: "center",
    padding: "30px",
    background: "#f4f6f8",
    minHeight: "100vh",
  },
  title: {
    marginBottom: "20px",
  },
  card: {
    background: "white",
    padding: "20px",
    borderRadius: "10px",
    width: "300px",
    margin: "auto",
    boxShadow: "0px 4px 10px rgba(0,0,0,0.1)",
  },
  input: {
    width: "100%",
    padding: "10px",
    margin: "10px 0",
    borderRadius: "5px",
    border: "1px solid #ccc",
  },
  button: {
    width: "100%",
    padding: "10px",
    background: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
};
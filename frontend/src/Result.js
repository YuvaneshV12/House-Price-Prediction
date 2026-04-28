import { useLocation, useNavigate } from "react-router-dom";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement);

function Result() {
  const location = useLocation();
  const navigate = useNavigate();
  const data = location.state;

  if (!data) return <h2>No Data</h2>;

  const chartData = {
    labels: data.years,
    datasets: [
      {
        label: "House Price Growth (Lakhs)",
        data: data.prices,
        borderColor: "blue",
        fill: false,
      },
    ],
  };

  return (
    <div style={styles.container}>

    <h1 style={styles.title}>🏠 Smart House Price Predictor</h1>

      {/* GRAPH */}
      <div style={styles.graph}>
        <Line data={chartData} />
      </div>

      {/* RESULTS */}
      <div style={styles.card}>
        <h2>📊 Results</h2>

        <p>💰 Current Price: ₹ {data.current_price} Lakhs</p>
        <p>📈 Future Price (10 yrs): ₹ {data.future_price} Lakhs</p>
        <p>📊 Growth Rate: {data.growth_rate}%</p>
        <p>⭐ Investment Score: {data.investment_score}</p>

        <h3 style={{ color: data.verdict === "Good Investment" ? "green" : "orange" }}>
          {data.verdict}
        </h3>

      </div>

      <button onClick={() => navigate("/")} style={styles.backBtn}>
        ⬅ Back to Home
      </button>
    </div>
  );
}

export default Result;

const styles = {
  container: {
    textAlign: "center",
    padding: "30px",
    background: "#f4f6f8",
    minHeight: "100vh",
  },
  title: {
    marginBottom: "20px",
  },
  backBtn: {
    marginTop: "30px",
    padding: "10px",
    cursor: "pointer",
    background: "none",
    border: "none",
    outline: "none",
    color: "#003366",
    fontSize: "16px",
    fontWeight: "600",
  },
  graph: {
    width: "600px",
    margin: "auto",
  },
  card: {
    marginTop: "20px",
    padding: "20px",
    background: "white",
    borderRadius: "10px",
    width: "350px",
    marginLeft: "auto",
    marginRight: "auto",
    boxShadow: "0px 4px 10px rgba(0,0,0,0.1)",
  },

};
# tec-forecast-dashboard

# 🌌 TEC Forecast Dashboard

A real-time Total Electron Content (TEC) forecasting dashboard using LSTM, built with Streamlit. The dashboard allows you to choose between synthetic and real TEC data, simulate solar cycle phases, and forecast upcoming TEC values.

---

## 📦 Features

- Switch between **Synthetic** and **Real** TEC datasets.
- Select **Solar Phases** (Rising, Peak, Declining, Minimum).
- Add Noise to synthetic data.
- Forecast TEC for a custom number of days using an LSTM model.
- Export forecast results as **CSV** or **PNG**.

---

## 🧠 Model Details

- Built with a 2-layer LSTM.
- Trained on synthetic TEC data generated using solar cycles.
- TEC values are scaled using `MinMaxScaler` (stored as `scaler.pkl`).
- Trained model saved as `lstm_model.keras`.

---

## 🛠️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/tec-forecast-dashboard.git
   cd tec-forecast-dashboard
   
2.Install dependencies:
  pip install -r requirements.txt

3.Run the app:
  streamlit run app.py

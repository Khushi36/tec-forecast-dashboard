import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="TEC Forecast Dashboard", layout="wide")

# Load CSS
with open("style/custom_dark.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🌌 Total Electron Content (TEC) Forecasting Dashboard")
st.markdown("Real-time and synthetic forecasting of TEC data based on solar cycle behavior using LSTM models.")

# Sidebar Controls
st.sidebar.title("⚙️ Controls")
dataset_choice = st.sidebar.radio("Choose Dataset", ("Synthetic", "Real"))

solar_phase = st.sidebar.selectbox("Select Solar Phase", ["Rising", "Peak", "Declining", "Minimum"])
add_noise = st.sidebar.checkbox("Add Noise", value=True)
forecast_days = st.sidebar.slider("Forecast Days", min_value=1, max_value=30, value=7)

# Simulate Synthetic TEC
def simulate_synthetic_tec(start_date='2010-01-01', end_date='2024-12-31', solar_phase='Rising', noise=True):
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    days = np.arange(len(dates))

    if solar_phase == 'Rising':
        cycle = np.sin(2 * np.pi * days / 4000) * 10 + 30
    elif solar_phase == 'Peak':
        cycle = np.sin(2 * np.pi * days / 4000) * 15 + 50
    elif solar_phase == 'Declining':
        cycle = np.sin(2 * np.pi * days / 4000) * 10 + 25
    else:  # Minimum
        cycle = np.sin(2 * np.pi * days / 4000) * 5 + 10

    if noise:
        noise_values = np.random.normal(0, 2, len(dates))
        tec_values = cycle + noise_values
    else:
        tec_values = cycle

    return pd.DataFrame({'Date': dates, 'TEC': tec_values})

# Load Real or Synthetic Data
if dataset_choice == "Synthetic":
    tec_df = simulate_synthetic_tec(solar_phase=solar_phase, noise=add_noise)
else:
    try:
        tec_df = pd.read_csv("data/sample_real_tec.csv", parse_dates=['Date'])
    except:
        st.error("Please upload a real TEC dataset in 'data/sample_real_tec.csv'")

# Forecasting Function (Placeholder)
def dummy_forecast(df, days):
    last_value = df['TEC'].iloc[-1]
    forecast = [last_value + np.random.normal(0, 1) for _ in range(days)]
    forecast_dates = pd.date_range(start=df['Date'].iloc[-1] + pd.Timedelta(days=1), periods=days)
    return pd.DataFrame({'Date': forecast_dates, 'Forecast_TEC': forecast})

# Generate Forecast
forecast_df = dummy_forecast(tec_df, forecast_days)

# Plotting
tab1, tab2 = st.tabs(["📈 TEC Trend", "🔮 Forecast"])

with tab1:
    fig1 = px.line(tec_df, x="Date", y="TEC", title="TEC Time Series")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    fig2 = px.line(forecast_df, x="Date", y="Forecast_TEC", title=f"{forecast_days}-Day TEC Forecast")
    st.plotly_chart(fig2, use_container_width=True)

# Export Options
st.sidebar.title("📤 Export Options")
export_type = st.sidebar.radio("Export Forecast As", ("CSV", "PNG"))

if export_type == "CSV":
    st.sidebar.download_button("Download CSV", forecast_df.to_csv(index=False), "forecast.csv")
else:
    fig, ax = plt.subplots()
    ax.plot(forecast_df['Date'], forecast_df['Forecast_TEC'], marker='o')
    ax.set_title('TEC Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Forecast TEC')
    st.sidebar.download_button("Download PNG", data=None, file_name="forecast.png", mime="image/png")  # dummy until download_png is added

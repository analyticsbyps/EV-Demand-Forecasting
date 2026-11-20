import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="EV Demand Forecast",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ EV Charging Demand Forecast")
st.subheader("Demand Forecasting and Analytics Dashboard")

st.markdown("---")
daily_data = pd.read_csv("cleaned_daily_demand.csv")
model_comparison = pd.read_csv("model_comparison.csv")
forecast_summary = pd.read_csv("forecast_summary.csv")
xgb_forecast = pd.read_csv("final_365_day_forecast.csv")
daily_data["date"] = pd.to_datetime(daily_data["date"])
xgb_forecast["date"] = pd.to_datetime(xgb_forecast["date"])

st.success("Datasets loaded successfully!")

st.markdown("### 📊 Key Performance Indicators")

total_demand = daily_data["demand_kwh"].sum()
avg_demand = daily_data["demand_kwh"].mean()
peak_demand = daily_data["demand_kwh"].max()
forecast_30_total = xgb_forecast.head(30)["predicted_demand"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Historical Demand", f"{total_demand:,.0f} kWh")
col2.metric("Average Daily Demand", f"{avg_demand:,.0f} kWh")
col3.metric("Peak Daily Demand", f"{peak_demand:,.0f} kWh")
col4.metric("Next 30 Days Forecast", f"{forecast_30_total:,.0f} kWh")

st.markdown("---")
st.markdown("### 🔮 Demand Forecast")

forecast_period = st.selectbox(
    "Select Forecast Period",
    ["30 Days", "90 Days", "365 Days"]
)

if forecast_period == "30 Days":
    selected_forecast = xgb_forecast.head(30)

elif forecast_period == "90 Days":
    selected_forecast = xgb_forecast.head(90)

else:
    selected_forecast = xgb_forecast.head(365)


fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    selected_forecast["date"],
    selected_forecast["predicted_demand"],
    marker=".",
    label="Predicted Demand"
)

ax.set_title(f"EV Demand Forecast - {forecast_period}")
ax.set_xlabel("Date")
ax.set_ylabel("Demand (kWh)")
ax.grid(True)
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

st.markdown("---")
st.markdown("### 📈 Historical Demand Trend")

fig2, ax2 = plt.subplots(figsize=(12, 5))

ax2.plot(
    daily_data["date"],
    daily_data["demand_kwh"],
    label="Historical Demand"
)

ax2.set_title("Daily EV Charging Demand")
ax2.set_xlabel("Date")
ax2.set_ylabel("Demand (kWh)")
ax2.grid(True)
ax2.legend()

plt.tight_layout()

st.pyplot(fig2)

st.markdown("---")
st.markdown("### 🤖 Forecast Model Comparison")

fig3, ax3 = plt.subplots(figsize=(8, 5))

ax3.bar(
    model_comparison["Model"],
    model_comparison["MAPE (%)"]
)

ax3.set_title("Model Accuracy Comparison (MAPE)")
ax3.set_xlabel("Forecasting Model")
ax3.set_ylabel("MAPE (%)")
ax3.grid(axis="y", alpha=0.3)

plt.tight_layout()

st.pyplot(fig3)

st.markdown("---")
st.markdown("### 💡 Business Insights")

st.markdown("""
**Monthly Patterns**
- May recorded the highest aggregated monthly demand.
- February recorded the lowest aggregated monthly demand.
- Monthly demand was relatively consistent across the observed period.

**Weekly Patterns**
- Tuesday recorded the highest aggregated demand.
- Weekend demand was lower than weekday demand.
- Weekday demand patterns may help operators plan staffing and capacity.

**Hourly Patterns**
- 10 AM recorded the highest aggregated hourly demand.
- Demand was particularly high between 10 AM and 2 PM.
- Evening and nighttime demand was comparatively lower.

**Forecasting**
- XGBoost achieved the lowest RMSE and MAPE among the three evaluated models.
- The forecast can support capacity planning and energy procurement decisions.
""")

st.markdown("---")

st.caption("EV Charging Demand Forecasting | CadetX PowerGrid EV Analytics Programme")
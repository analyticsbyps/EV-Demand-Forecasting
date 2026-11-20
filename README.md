# ⚡ EV Charging Demand Forecasting

## 📌 Project Overview
This project focuses on forecasting electric vehicle (EV) charging demand using historical charging-session data. The objective is to identify demand patterns and predict future energy consumption to support capacity planning, staffing, and energy procurement decisions.

Developed as part of the **CadetX – PowerGrid EV Analytics Programme**.

## 🎯 Objectives
- Analyze historical EV charging demand.
- Identify hourly, weekly, and monthly demand patterns.
- Develop and evaluate forecasting models.
- Forecast demand for the next 30, 90, and 365 days from the dataset's final date.
- Build an interactive dashboard to visualize demand and forecasting results.

## 📂 Dataset
The dataset includes EV charging-session records containing information such as:
- Session timestamps
- Energy consumption (kWh)
- Charger type
- Station region
- Session duration
- Payment information

The data was processed and aggregated into daily energy demand time series.

## 🛠️ Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels (SARIMA)
- Prophet
- XGBoost
- Streamlit
- Jupyter Notebook

## 📊 Exploratory Data Analysis
The project examined:
- Yearly demand trends
- Monthly demand patterns
- Weekday vs. weekend demand
- Hourly charging patterns
- Charger-type demand

## 🤖 Forecasting Models

Three forecasting models were evaluated:

| Model | RMSE | MAPE |
|---|---:|---:|
| SARIMA | 1860.61 | 7.97% |
| Prophet | 1858.55 | 7.75% |
| XGBoost | 1144.51 | 4.16% |

XGBoost achieved the lowest RMSE and MAPE among the evaluated models on the selected test period.

## 📈 Dashboard Features
- Historical demand KPIs
- Average and peak daily demand
- Forecast visualization for 30, 90, and 365 days
- Historical demand trends
- Model accuracy comparison
- Business insights

## 💡 Key Insights
- May recorded the highest aggregated monthly demand.
- February recorded the lowest aggregated monthly demand.
- Weekday demand was higher than weekend demand.
- Tuesday recorded the highest aggregated weekday demand.
- Charging demand was highest around 10 AM.
- Demand was particularly strong between 10 AM and 2 PM.
- XGBoost performed best among the three evaluated models.

## 📁 Project Structure
```text
EV_Demand_Forecasting/
│
├── app.py
├── Untitled1.ipynb
├── ev_charging_dataset.xlsx
├── cleaned_daily_demand.csv
├── daily_demand.csv
├── hourly_demand.csv
├── model_comparison.csv
├── forecast_summary.csv
├── final_365_day_forecast.csv
├── forecast_30_days.csv
├── forecast_90_days.csv
├── forecast_365_days.csv
├── sarima_results.csv
├── prophet_results.csv
└── xgboost_results.csv
```

## 🚀 Running the Dashboard

Install the required libraries:

```bash
pip install pandas numpy matplotlib streamlit xgboost prophet statsmodels
```

Run the dashboard:

```bash
streamlit run app.py
```

## ⚠️ Note
Forecasts represent predictions generated from the historical dataset and its final date. They are not real-time forecasts based on live EV charging data.

## 👩‍💻 Project Author
Developed as a data analytics and forecasting project as part of the CadetX PowerGrid EV Analytics Programme.
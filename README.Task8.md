# ⚡ Dynamic Pricing Recommendation System

## 📌 Project Overview

The Dynamic Pricing Recommendation System is an intelligent pricing solution developed for EV charging stations. It recommends optimal charging prices based on demand patterns, time periods, geographical regions, and charger types.

The objective is to maximise revenue while maintaining reasonable and controlled price adjustments.

## 🎯 Project Objectives

- Analyse EV charging demand patterns.
- Identify peak, off-peak, and normal demand periods.
- Develop a demand-based pricing recommendation model.
- Optimise prices using demand, region, and charger type.
- Simulate potential revenue improvements.
- Develop an interactive pricing dashboard.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

## ⚙️ Methodology

### 1. Demand Analysis
Analysed charging sessions based on:
- Hourly demand
- Time periods
- Station regions
- Charger types

### 2. Demand-Based Pricing Model

Charging demand was classified into three categories:

- Low Demand
- Medium Demand
- High Demand

Demand multipliers were assigned:

| Demand Level | Multiplier |
|---|---:|
| Low | 0.95 |
| Medium | 1.00 |
| High | 1.05 |

Additional adjustments were incorporated for geographical regions and charger types.

### 3. Price Optimisation Engine

The recommended price was calculated using demand, regional, and charger-type multipliers.

Price adjustments were restricted to a range of 90%–110% of the original price to prevent excessive fluctuations.

### 4. Revenue Uplift Simulation

A revenue simulation was performed using an assumed negative price elasticity of -0.164.

The simulation estimated how changes in recommended prices could affect customer demand and revenue.

### 5. Peak and Off-Peak Pricing Strategy

A time-based pricing strategy was implemented:

| Time Period | Pricing Strategy |
|---|---|
| Peak (6 PM–9 PM) | 5% Price Increase |
| Off-Peak (12 AM–5 AM) | 5% Price Reduction |
| Normal Hours | No Price Change |

## 📊 Results

The dynamic pricing simulation produced the following results:

| Metric | Result |
|---|---:|
| Current Revenue | ₹81,71,100.12 |
| Dynamic Revenue | ₹85,33,259.00 |
| Revenue Uplift | 4.43% |

The simulation indicates a potential revenue improvement through demand-based pricing adjustments.

*Note: These figures represent simulated results, not verified real-world revenue.*

## 📈 Interactive Dashboard

A Streamlit dashboard was developed to visualise pricing performance.

### Dashboard Features

- Current Revenue and Dynamic Revenue KPIs
- Revenue Uplift Analysis
- Hourly Charging Demand
- Current vs Recommended Pricing
- Regional Charging Demand
- Charger Type Analysis
- Dynamic Pricing Recommendations
- Region and Charger Type Filters
- Downloadable Pricing Recommendations

## 📁 Project Files

| File Name | Description |
|---|---|
| `dynamic_pricing_app.py` | Streamlit dashboard application |
| `dynamic_pricing_dashboard_data.csv` | Dashboard visualisation data |
| `dynamic_pricing_recommendations.csv` | Pricing recommendation output |

## 🚀 How to Run the Dashboard

### Step 1: Install Required Libraries

```bash
pip install streamlit pandas numpy matplotlib seaborn
```

### Step 2: Navigate to the Project Folder

```bash
cd path/to/your/project
```

### Step 3: Run the Streamlit Application

```bash
streamlit run dynamic_pricing_app.py
```

The dashboard will open in your web browser.

## 💡 Conclusion

This project demonstrates how data analytics and pricing optimisation techniques can support revenue management in EV charging infrastructure.

By combining demand analysis, time-based pricing, regional adjustments, and revenue simulation, the system provides actionable pricing recommendations through an interactive dashboard.

The project highlights the practical application of Python, data analysis, and business intelligence in the electric vehicle industry.


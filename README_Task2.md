# Task 2: Revenue Forecasting & Price Sensitivity Analysis

## Project Overview
This project focuses on analyzing EV charging revenue trends, estimating price sensitivity, and forecasting future revenue using historical electric vehicle charging session data from 2022 to 2024.

The analysis explores revenue patterns, energy demand, the relationship between price and demand, and the potential impact of hypothetical pricing changes on revenue.

## Objectives
- Analyze monthly revenue and energy demand trends.
- Explore the relationship between charging prices and energy demand.
- Estimate price elasticity using regression analysis.
- Forecast revenue for the next six months.
- Simulate the impact of a 5% price increase and a 10% price decrease.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Jupyter Notebook

## Project Workflow
1. Data preparation and datetime conversion.
2. Monthly revenue, demand, price, and session aggregation.
3. Exploratory data analysis and trend visualization.
4. Price-demand correlation analysis.
5. Log-log regression with time trend and monthly seasonal controls.
6. Six-month revenue forecasting using Holt-Winters Exponential Smoothing.
7. Pricing scenario simulation.
8. Interpretation of results and business conclusions.

## Key Results

| Metric | Result |
|---|---:|
| Estimated Price Elasticity | 0.164 |
| Revenue Impact of 5% Price Increase | +5.84% |
| Revenue Impact of 10% Price Decrease | -11.54% |
| Average Baseline Forecast Revenue | 529,924.60 |
| Average Revenue with 5% Price Increase | 560,891.51 |
| Average Revenue with 10% Price Decrease | 468,760.92 |

## Forecasting
A Holt-Winters Exponential Smoothing model with additive trend and seasonality was used to forecast monthly revenue for six months (January–June 2025).

## Pricing Scenario Analysis
Two hypothetical pricing scenarios were evaluated:

- **5% Price Increase:** The simulation projected an estimated revenue increase of 5.84%.
- **10% Price Decrease:** The simulation projected an estimated revenue decrease of 11.54%.

The scenarios were based on the estimated elasticity and should be interpreted as model-based simulations rather than causal predictions.

## Conclusion
The analysis suggests that, under the model's assumptions, a hypothetical 5% price increase could potentially improve revenue. However, the estimated positive price elasticity should be interpreted cautiously because the analysis uses observational data and a relatively small monthly sample.

This project demonstrates the application of exploratory data analysis, regression modeling, time-series forecasting, and scenario analysis to support data-driven business decision-making.

## Disclaimer
The pricing scenarios are illustrative and do not establish causal relationships between price changes and customer demand.

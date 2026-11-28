
# Task 10: Session Duration & Energy Consumption Prediction

## 1. Project Overview
This project develops machine learning models to predict EV charging session duration and energy consumption using historical charging-session data.

The objective is to help EV charging operators improve resource planning, charger allocation and customer experience.

## 2. Dataset
- Total records: 294,024
- Original features used: 10
- Training records: 235,219
- Testing records: 58,805
- Train-test split: 80:20

## 3. Features Used
- Charger Type
- Station Region
- User Type
- Payment Method
- Hour
- Day of Week
- Month
- Weekend Indicator
- Price per kWh
- Year

Categorical variables were converted using One-Hot Encoding.

## 4. Machine Learning Models
Two regression algorithms were implemented:

- Random Forest Regressor
- XGBoost Regressor

Separate models were trained for session duration and energy consumption.

## 5. Model Performance

| Prediction Task | Model | MAE | RMSE | R2 Score |
|---|---|---:|---:|---:|
| Session Duration | Random Forest | 1.9780 | 2.5997 | 0.9645 |
| Session Duration | XGBoost | 1.9757 | 2.5915 | 0.9647 |
| Energy Consumption | Random Forest | 3.2472 | 4.1421 | 0.9383 |
| Energy Consumption | XGBoost | 3.2305 | 4.1220 | 0.9389 |

XGBoost achieved the best overall results, although its improvement over Random Forest was small.

## 6. Feature Importance Analysis
Feature importance analysis showed that charger type was the most influential feature in both prediction tasks.

- DC_50kW was the leading feature for session duration.
- DC_300kW was the leading feature for energy consumption.

These are model-based importance scores and do not establish causal relationships.

## 7. Prediction API Mockup
A Python prediction function was developed to simulate a real-time prediction API.

It accepts charging-session details and returns:
- Predicted session duration in minutes.
- Predicted energy consumption in kWh.

### Sample Prediction
- Predicted Duration: 24.34 minutes
- Predicted Energy: 48.57 kWh
- Actual Duration: 26 minutes
- Actual Energy: 56.9 kWh

This is a local API-style function mockup, not a deployed online API.

## 8. Operational Use Cases
1. Charging Time Estimation
2. Energy Demand Planning
3. Charger Allocation
4. Fleet Scheduling
5. Customer Experience Improvement

## 9. Saved Deliverables
- task10_model_comparison.csv
- task10_model_accuracy_comparison.png
- task10_duration_feature_importance.csv
- task10_energy_feature_importance.csv
- task10_duration_feature_importance.png
- task10_energy_feature_importance.png
- task10_xgb_duration_model.pkl
- task10_xgb_energy_model.pkl
- task10_feature_columns.pkl
- task10_operational_use_cases.csv

## 10. Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook

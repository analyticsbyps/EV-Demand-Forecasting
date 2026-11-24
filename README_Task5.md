# Task 5: Predictive Maintenance for EV Chargers

## Project Overview
This project focuses on identifying EV chargers that may require maintenance by analysing charging utilisation, energy consumption, session duration, and idle-time patterns.

A proxy-based risk assessment framework was developed to identify chargers requiring further investigation and prioritise preventive maintenance.

## Objectives
- Develop charger health indicators.
- Identify unusual energy and session-duration patterns.
- Analyse charger utilisation and idle time.
- Calculate maintenance risk scores.
- Classify chargers into Low, Medium, and High risk categories.
- Generate a maintenance priority list.
- Recommend preventive maintenance actions.

## Dataset
The analysis used the EV charging session dataset containing 294,024 charging records and 199 unique chargers.

Key features included:
- Charger ID and charger type
- Total charging sessions
- Energy consumption
- Average session duration
- Energy and duration variability
- Total charging hours
- Average idle time
- Estimated utilisation rate

## Methodology

### 1. Data Preparation
- Checked missing values and duplicate records.
- Reviewed timestamp columns.
- Aggregated session-level information by charger.

### 2. Charger Health Indicators
Four indicators were developed:

1. Low Utilisation
2. High Idle Time
3. High Energy Variability
4. High Duration Variability

Quartile-based thresholds were used to identify unusual usage patterns.

### 3. Maintenance Risk Scoring
Each charger received one point for every triggered risk indicator.

| Risk Score | Risk Category |
|---|---|
| 0 | Low |
| 1–2 | Medium |
| 3–4 | High |

### 4. Maintenance Risk Distribution

Analysis of 199 chargers produced the following results:

| Risk Category | Number of Chargers |
|---|---:|
| High | 22 |
| Medium | 98 |
| Low | 79 |
| **Total** | **199** |

### 5. Health Indicator Analysis

Each of the four health indicators was triggered for 50 chargers (25.13%).

The indicators were:
- Low utilisation
- High idle time
- High energy variability
- High duration variability

### 6. Maintenance Priority List
Chargers were ranked using their risk scores and utilisation rates.

High-risk chargers were prioritised for further technical investigation.

### 7. Preventive Maintenance Recommendations
Recommendations were generated based on the identified risk indicators:

- Investigate low charger utilisation and demand patterns.
- Inspect extended idle periods and charger availability.
- Check energy delivery consistency.
- Investigate variations in charging duration.
- Schedule priority technical inspections for high-risk chargers.
- Continue routine monitoring for low-risk chargers.

## Deliverables

The following output files were generated:

1. `charger_health_indicators.csv`
2. `maintenance_priority_list.csv`
3. `health_indicator_report.csv`

## Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Important Limitation
The dataset does not contain actual charger failure records, fault logs, or maintenance history.

Therefore, this project uses a proxy-based maintenance risk scoring framework rather than a trained and validated machine-learning failure-prediction model.

The risk scores indicate unusual operational patterns and should be used to prioritise further investigation, not as confirmed evidence of charger failure.

## Conclusion
This project demonstrates

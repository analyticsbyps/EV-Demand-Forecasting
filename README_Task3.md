# Task 3: Charger Utilisation & Efficiency Analysis

## Project Overview
This project analyses EV charging station and charger utilisation to understand usage patterns, idle intervals, peak demand periods and differences in charger performance. The objective is to support data-driven capacity planning and operational optimisation.

## Objectives
- Analyse charger utilisation rates.
- Compare utilisation across charging stations.
- Examine idle intervals between charging sessions.
- Identify peak charging hours and energy demand patterns.
- Rank high- and low-utilisation chargers.
- Develop capacity optimisation recommendations.

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Analysis Performed

### 1. Data Cleaning
- Converted timestamps into datetime format.
- Checked missing values.
- Checked negative and zero session durations.
- Checked duplicate session IDs.

### 2. Charger Utilisation Analysis
Calculated:
- Total charging hours
- Total charging sessions
- Total energy delivered
- Average session duration
- Utilisation rate

### 3. Station-Level Analysis
Compared station utilisation rates to identify stations with relatively higher and lower charging activity.

### 4. Idle-Time Analysis
Calculated recorded time gaps between consecutive charging sessions on the same charger.

### 5. Peak-Load Analysis
Analysed charging activity and energy consumption by hour of the day to identify demand patterns.

### 6. Charger Performance Ranking
Identified the chargers with the highest and lowest utilisation rates.

### 7. Station-Wise Energy Analysis
Compared total energy delivered across charging stations.

## Key Findings
- STN_007 recorded the highest station-level utilisation rate among the stations analysed, at approximately 40.38%.
- STN_001_CH_04 was the highest-utilisation charger, at approximately 12.07%.
- STN_025_CH_02 recorded the lowest utilisation rate among the chargers analysed, at approximately 0.73%.
- Charging activity varied across stations and hours of the day.
- Recorded idle intervals provided additional insight into charging-session patterns.

## Capacity Optimisation Recommendations
- Monitor stations with comparatively higher utilisation.
- Investigate low-utilisation chargers before making relocation or investment decisions.
- Use hourly demand patterns to support scheduling and energy planning.
- Consider demand-based charger allocation.
- Monitor charger performance regularly to support operational planning.

## Limitations
Utilisation was calculated using recorded charging duration over the overall observation period. The dataset does not provide real-time charger availability, downtime records or queueing information. Therefore, recorded idle intervals may include periods when chargers were unavailable, and low utilisation does not necessarily indicate poor performance.

## Conclusion
The analysis provides insights into EV charging infrastructure utilisation, station-level activity, idle intervals, peak demand and charger performance. These insights can support improved capacity planning, operational monitoring and evidence-based infrastructure decisions.

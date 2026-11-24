# Task 7: Time-of-Day & Day-of-Week Pattern Analysis

## Project Overview
This task analyses EV charging behaviour across different hours, days of the week, months, regions, and charger types using Python.

The objective is to identify peak and off-peak demand periods, understand customer charging patterns, and develop operational recommendations for better resource allocation, pricing, and infrastructure planning.

## Dataset
- **Dataset:** EV Charging Dataset
- **Total Records:** 294,024 charging sessions
- **Time Period:** 2022–2024
- **Tools:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook

## Analysis Performed

### 1. Hourly Demand Analysis
- Identified hourly charging sessions and energy consumption.
- Peak demand occurred at **10 AM**, with 24,214 sessions and 1,134,524 kWh.
- Lowest demand occurred at **3 AM**, with 2,633 sessions and 124,141.6 kWh.
- Demand increased during the morning and remained high throughout daytime hours.

### 2. Day-of-Week Analysis
- Tuesday recorded the highest energy consumption at approximately 2,150,639 kWh.
- Saturday recorded the lowest energy consumption at approximately 1,564,654.5 kWh.
- Sunday recorded the fewest sessions.

### 3. Weekday vs Weekend Comparison
- Weekday average daily energy consumption: approximately 2,134,980 kWh.
- Weekend average daily energy consumption: approximately 1,566,922 kWh.
- Weekday daily demand was approximately 36% higher than weekend demand.

### 4. Peak and Off-Peak Analysis
- Peak hour: 10 AM.
- Off-peak hour: 3 AM.
- Overnight hours showed considerably lower charging activity.

### 5. Seasonal Trend Analysis
- May recorded the highest aggregate monthly energy demand at approximately 1,181,017.5 kWh.
- February recorded the lowest at approximately 1,089,574.6 kWh.
- Year-wise monthly comparisons were also performed to distinguish recurring monthly patterns from overall growth in charging activity.

### 6. Regional Hourly Analysis
- Compared hourly energy consumption across station regions.
- North West showed particularly high absolute demand, followed by Midlands.
- Most regions experienced increased charging activity during daytime hours.

### 7. Charger-Type Analysis

Three charger types were compared:

| Charger Type | Total Sessions | Average Energy per Session | Average Duration |
|---|---:|---:|---:|
| DC_150kW | 96,977 | 48.96 kWh | 24.50 min |
| DC_300kW | 60,226 | 75.54 kWh | 19.49 min |
| DC_50kW | 136,821 | 32.97 kWh | 49.48 min |

Key observations:
- DC_50kW recorded the highest number of charging sessions.
- DC_300kW delivered the highest average energy per session.
- DC_50kW had the longest average charging duration.
- All three charger types showed stronger daytime demand.

## Visualisations

The following charts were generated:

1. `hourly_demand.png`
2. `weekly_demand.png`
3. `monthly_seasonal_demand.png`
4. `yearly_seasonal_comparison.png`
5. `regional_hourly_heatmap.png`
6. `charger_type_hourly_heatmap.png`

## Exported Analysis Files

- `hourly_demand_summary.csv`
- `weekly_demand_summary.csv`
- `weekday_weekend_comparison.csv`
- `monthly_seasonal_summary.csv`
- `yearly_monthly_demand.csv`
- `regional_hourly_demand.csv`
- `charger_type_hourly_demand.csv`
- `charger_type_summary.csv`

## Operational Recommendations

1. **Peak-hour staffing:** Increase operational support and charger availability between 9 AM and 3 PM.
2. **Weekday resource allocation:** Allocate more operational resources during weekdays because average daily demand is considerably higher.
3. **Off-peak pricing:** Consider incentives and lower tariffs during overnight hours to encourage flexible charging.
4. **Maintenance scheduling:** Schedule routine maintenance during lower-demand overnight periods.
5. **Regional infrastructure:** Investigate high-demand regions such as North West and Midlands for potential capacity expansion.
6. **Charger-type planning:** Consider the higher session volume and longer occupancy of DC_50kW chargers when planning capacity.
7. **Seasonal planning:** Use monthly demand trends to support resource planning while monitoring year-wise changes.

## Limitations

- Regional total demand does not account for differences in the number of stations or chargers in each region.
- Monthly demand totals are aggregated across multiple years, so they should not be interpreted as proof of seasonal causation.
- Charger-type comparisons are based on observed sessions and do not independently measure charger efficiency or technical performance.
- Pricing recommendations require further testing before implementation.

## Conclusion

The analysis identifies clear daily, weekly, regional, and charger-type differences in EV charging behaviour.

Charging demand is strongest during daytime hours, particularly around 10 AM, and weekday demand is substantially higher than weekend demand.

These findings can help EV charging operators improve staffing, plan maintenance, explore time-based pricing strategies, and make more informed infrastructure decisions.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook
- GitHub

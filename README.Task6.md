# Task 6: Optimal Location Planning for New EV Charging Stations

## Project Overview

This project analyses regional EV charging demand, existing charging infrastructure and customer concentration to identify potential locations for new EV charging stations.

The objective is to identify regions where infrastructure expansion could help meet demand and improve charging network coverage.

## Objectives

- Analyse regional EV charging demand.
- Compare demand with existing station supply.
- Identify potential infrastructure gaps.
- Develop a weighted location scoring model.
- Create regional demand heatmaps.
- Build an interactive UK expansion priority map.
- Recommend regions for further investigation.

## Dataset Overview

The analysis uses an EV charging sessions dataset containing:

- 294,024 charging sessions.
- 9 geographical regions.
- 33 existing charging stations.
- 8,000 unique customers across the dataset.

Important variables include:
- station_region
- station_id
- charger_id
- session_id
- energy_kwh
- total_cost
- customer_id

## 1. Regional Demand Analysis

Regional demand was evaluated using:
- Total charging sessions.
- Total energy consumption.
- Total revenue.
- Regional unique customer counts.
- Average energy consumed per session.

### Key Findings

- North West recorded the highest demand, with 65,789 sessions and 3,005,135.1 kWh of energy consumption.
- Midlands ranked second in total energy demand, with 2,576,709.8 kWh.
- London ranked third, with 1,978,090.6 kWh.
- Wales recorded the lowest energy demand.

## 2. Regional Supply Analysis

Existing infrastructure was evaluated using:
- Number of charging stations.
- Number of chargers.
- Energy consumption per station.
- Charging sessions per station.

### Key Finding

South West recorded the highest energy consumption per station, at approximately 526,832 kWh.

This indicates relatively high demand per existing station and makes the region a potential expansion candidate.

## 3. Demand vs Supply Gap Analysis

Demand share was compared with existing station supply share.

**Formula:**

Demand–Supply Gap = Demand Share (%) − Station Supply Share (%)

A positive value indicates that a region's share of energy demand exceeds its share of existing stations.

### Results

| Region | Demand–Supply Gap |
|---|---:|
| Midlands | +3.51% |
| South West | +2.35% |
| North East | +1.03% |
| North West | +0.55% |
| Yorkshire & Humber | +0.46% |
| Wales | -0.60% |
| London | -0.83% |
| Scotland | -2.23% |
| South East | -4.24% |

### Interpretation

Midlands recorded the largest positive demand–supply gap, followed by South West and North East.

These regions may require further investigation to determine whether additional charging infrastructure is justified.

## 4. Location Scoring Model

A weighted scoring model was developed to rank regions according to their expansion potential.

### Scoring Criteria

| Indicator | Weight |
|---|---:|
| Regional Energy Demand | 40% |
| Customer Concentration | 30% |
| Demand–Supply Gap | 30% |

All three indicators were normalized to a 0–100 scale.

**Location Score Formula:**

Location Score = (0.40 × Demand Score) + (0.30 × Customer Score) + (0.30 × Gap Score)

### Expansion Ranking

| Rank | Region | Location Score |
|---:|---|---:|
| 1 | Midlands | 92.96 |
| 2 | North West | 88.55 |
| 3 | South West | 72.11 |
| 4 | London | 66.27 |
| 5 | North East | 64.43 |
| 6 | Yorkshire & Humber | 52.09 |
| 7 | Scotland | 42.38 |
| 8 | South East | 37.71 |
| 9 | Wales | 35.28 |

## 5. Visualisations

### Regional Demand Heatmap

A heatmap was created using normalized regional indicators to compare:
- Energy consumption.
- Charging sessions.
- Customer counts.
- Existing station counts.
- Demand–supply gaps.

### Interactive UK Expansion Map

An interactive map was developed using Folium.

The map displays:
- Regional expansion priority.
- Location scores.
- Expansion rankings.
- Interactive regional markers.

The marker positions represent approximate regional centres, not actual charging station locations.

## 6. Expansion Strategy and Recommendations

Based on the scoring model and regional analysis, three regions are recommended for further investigation.

### Priority 1: Midlands

- Highest location score: 92.96.
- Largest positive demand–supply gap: +3.51%.
- Strong regional customer concentration.

**Recommendation:** Investigate additional charging infrastructure in high-demand areas of the Midlands.

### Priority 2: North West

- Highest total energy demand: 3,005,135.1 kWh.
- Highest regional customer count in the analysis.
- Second-highest location score: 88.55.

**Recommendation:** Evaluate additional charging capacity in areas experiencing consistently high charging demand.

### Priority 3: South West

- Highest energy consumption per existing station.
- Second-largest positive demand–supply gap: +2.35%.
- Location score: 72.11.

**Recommendation:** Investigate station capacity and potential expansion in high-utilisation areas.

## 7. Conclusion

The analysis identifies Midlands, North West and South West as the three leading candidates for further EV charging infrastructure expansion.

Midlands ranks first because of its strong demand–supply gap and overall location score. North West leads in total energy demand, while South West has the highest energy consumption per existing station.

The results provide a data-driven starting point for infrastructure planning and investment decisions.

## 8. Limitations

- The dataset does not contain actual station coordinates or customer addresses.
- The map uses approximate regional centre coordinates.
- Customer counts are used as a proxy for customer concentration, not population density.
- Station counts do not capture charger capacity, availability or real-time congestion.
- The scoring weights are project assumptions and can be adjusted.
- The analysis identifies potential expansion regions but does not establish exact construction sites.

Further analysis using geographic data, population statistics, traffic patterns, grid capacity and land availability would be necessary before making actual investment decisions.

## 9. Project Deliverables

The following files were generated:

1. `regional_demand_analysis.csv`
2. `regional_gap_analysis.csv`
3. `location_scoring_model.csv`
4. `uk_expansion_priority_map.html`
5. `regional_demand_heatmap.png`
6. `README6.md`

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Folium
- Jupyter Notebook

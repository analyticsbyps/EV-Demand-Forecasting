# Task 4: Customer Behaviour Segmentation

## Objective
The objective of this task was to segment EV charging customers based on their charging behaviour, energy consumption, revenue generation and usage patterns using Machine Learning.

## Dataset
The original EV charging sessions dataset was used to analyse customer-level behaviour. Customer data was aggregated to create behavioural features for clustering.

## Feature Engineering
The following features were created at customer level:

- Total charging sessions
- Total energy consumption
- Total revenue generated
- Average session duration
- Average energy per session
- Average cost per session
- Unique stations visited
- Unique chargers used
- Average charging hour
- Average charging weekday
- Active months

Additional categorical features included preferred station and customer type.

## Methodology

1. Aggregated charging session data at customer level.
2. Created behavioural and temporal features.
3. Standardized numerical features using StandardScaler.
4. Used the Elbow Method to determine an appropriate number of clusters.
5. Applied K-Means clustering with 4 clusters.
6. Analysed customer segments and developed customer personas.

## Customer Personas

- **Regular Chargers:** Customers exhibiting relatively consistent charging behaviour.
- **Occasional Users:** Customers with very limited charging activity.
- **Power Users:** Customers with significantly higher charging frequency, energy consumption and revenue contribution.
- **Low-Usage Customers:** Customers with comparatively low charging activity and usage.

## Visualizations

- Elbow Method for optimal cluster selection
- Customer distribution by cluster
- Average revenue by persona
- Average energy consumption by persona
- Average charging sessions by persona
- Total revenue contribution by persona
- Customer segmentation dashboard

## Business Insights

- Regular Chargers represent the largest customer segment.
- Power Users generate the highest average revenue and energy consumption per customer.
- Occasional Users represent an opportunity for customer engagement and retention campaigns.
- Low-Usage Customers may benefit from targeted incentives to encourage repeat charging.

## Files Generated

- `customer_behaviour_features.csv`
- `customer_segmentation_final.csv`
- `customer_segment_summary.csv`

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- K-Means Clustering

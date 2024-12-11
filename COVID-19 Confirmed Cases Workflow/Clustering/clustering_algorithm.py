import pandas as pd
import numpy as np  # For logarithmic transformation
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the datasets
gov_response = pd.read_csv("monthly_gov_response.csv")
confirmed_cases = pd.read_csv("monthly_confirmed_cases.csv")

# Merge the datasets on country_code and country_name
merged_data = pd.merge(gov_response, confirmed_cases, on=["country_code", "country_name"], suffixes=('_gov', '_cases'))

# Select a specific month's data (e.g., March 2021)
selected_month = "2021-06"
clustering_data = merged_data[[
    "country_name", "country_code", f"{selected_month}_gov", f"{selected_month}_cases"
]].dropna()

# Log transform confirmed cases to reduce the impact of outliers
clustering_data[f"{selected_month}_cases"] = clustering_data[f"{selected_month}_cases"].apply(lambda x: np.log1p(x))

# Normalize both columns using StandardScaler
scaler = StandardScaler()
clustering_data_scaled = scaler.fit_transform(clustering_data[[f"{selected_month}_gov", f"{selected_month}_cases"]])

#Determine the optimal number of clusters using the Elbow method
inertia = []
for k in range(2, 13):  # Test for clusters between 2 and 10
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(clustering_data_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(2, 13), inertia, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.xticks(range(2, 13))
plt.show()

# #Apply K-Means with the chosen number of clusters
# optimal_clusters = 4
# kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
# clustering_data['Cluster'] = kmeans.fit_predict(clustering_data_scaled)

# # Save the clustered data for Tableau visualization
# output_file = "./clustering_data_tableau_normalized_2021-10.csv"
# clustering_data.to_csv(output_file, index=False)

# print(f"Clustered data saved to {output_file}")

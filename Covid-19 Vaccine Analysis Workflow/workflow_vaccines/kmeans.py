# kmeans
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt



def calculate_vaccination_score():
  
    df=pd.read_csv("../COVID19_DATA/OxCGRT_vaccines_full.csv")
    df.fillna(0,inplace=True)
    df["Date"]=pd.to_datetime(df["Date"],format="%Y%m%d")
    # select dates after January 1, 2021
    df=df[df["Date"]>="2021-01-01"]
    weights = {
      
        "Healthcare workers/carers (excluding care home staff)": 5,
        "Frontline/essential workers (when subcategories not specified)": 4,
        "Police/ first responders": 4,
        
    
        "At Risk 80+ yrs": 5,
        "Clinically vulnerable/chronic illness/significant underlying health condition (excluding elderly and disabled)": 4, 
        "Pregnant people": 3,
        
        
        "General 80+ yrs": 3,
        "General 70-74 yrs": 2,
        "General 60-64 yrs": 2,
        "General 50-54 yrs": 1,
        "General 40-44 yrs": 1,
        "General 30-34 yrs": 1,
        "General 20-24 yrs": 1,
        "General 16-19 yrs": 1,

    }
    # Calculate vaccination score for each vaccine
    df['V1_Score'] = 0
    df['V2_Score'] = 0
    df['V3_Score'] = 0
    for i in weights:
        df[f"V1_Score"]+=df[f"V1_{i}"]*weights[i]
        df[f"V2_Score"]+=df[f"V2_{i}"]*weights[i]
        df[f"V3_Score"]+=df[f"V3_{i}"]*weights[i]
    
    
    # Calculate overall vaccination score
    df['Vaccination_score'] = (
        df['V1_Score'] + 
        df['V2_Score'] + 
        df['V3_Score']
    ) / 3

    df=df.groupby("CountryName")[["Vaccination_score","V1_Score","V2_Score","V3_Score"]].mean().reset_index()
    return df

def kmeans(df):
    inertia=[]
    for i in range(2,11):
        kmeans = KMeans(n_clusters=i, random_state=42).fit(df["Vaccination_score"].values.reshape(-1, 1))
        ssi=kmeans.inertia_
        inertia.append(ssi)
    plt.figure(figsize=(12, 10))
    plt.plot(range(2,11),inertia,marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.title('Inertia vs Number of clusters')
    plt.savefig("./plots/Inertia vs Number of clusters.png")

    kmeans = KMeans(n_clusters=5, random_state=42).fit(df["Vaccination_score"].values.reshape(-1, 1))
    df["Cluster"] = kmeans.labels_
    return df

df=kmeans(calculate_vaccination_score())
cluster_counts = df["Cluster"].value_counts()
mean_scores = df.groupby("Cluster")["Vaccination_score"].mean()
    
# Pie chart
cluster_counts.sort_index(inplace=True)
plt.pie(
        cluster_counts,
        autopct="%.1f%%", 
        startangle=90, 
        labels=[f"Cluster {i} (Mean: {round(mean)})" for i, mean in mean_scores.items()],
    )
plt.title("Cluster Distribution with Mean Vaccination Policy Scores")
plt.ylabel("")  # Remove default ylabel
plt.xlabel("")  # Remove default xlabel
plt.savefig("./plots/Clusters.png")

#print elements in clusters

print(cluster_counts)
print(df.loc[df["CountryName"].isin(["United States","India","United Kingdom","Belgium","Angola"])])
for i in range(5):
    print(f"Cluster {i}:\n")
    print(df.loc[df["Cluster"]==i]["CountryName"].values)
    print("\n")

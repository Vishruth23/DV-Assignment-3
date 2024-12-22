import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def preprocess_data_for_vaccine_policy_and_hospitalizations():
    df=pd.read_csv('../COVID19_DATA/OxCGRT_latest.csv')  
    df1=pd.read_csv("../Google_data/hospitalizations.csv")

    
    df1=df1.loc[df1["location_key"]=="US"]
    df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
    df1=df1.drop(columns=["location_key"])
    df1=df1.rename(columns={"date":"Date"})

    df = df[df['CountryCode'] == 'USA']  
    df = df[['Date','H7_Vaccination policy']]
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
    df=df[df["Date"]>=pd.to_datetime("2021-01-01")]
    df["H7_Vaccination policy"] = df["H7_Vaccination policy"].fillna(0)

    df=pd.merge(df,df1,on="Date")
    return df

def plot_vaccine_policy_and_hospitalizations(df):
   
    plt.figure(figsize=(12, 10))
    df["new_hospitalized_patients"]=df["new_hospitalized_patients"].clip(lower=0)

    df["H7_Vaccination policy"]=df["H7_Vaccination policy"].astype(int)
    df["H7_Vaccination policy"]=df["H7_Vaccination policy"].map({1:"One Vulnerable group",2:"Few Vulnerable Groups",3:"All vulnerable \ngroups",4:"Additional\n+All Vulnerable Groups",5:"Universal Availability"})

    custom_palette = ["#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF"]
    sns.violinplot(x="H7_Vaccination policy", y="new_hospitalized_patients", data=df,hue="H7_Vaccination policy",legend=True,palette=custom_palette)
    plt.title("Vaccine Policy vs Hospitalizations")
    plt.savefig("./plots/Vaccine Policy vs Hospitalizations.png")

if __name__ == "__main__":
    df=preprocess_data_for_vaccine_policy_and_hospitalizations()
    plot_vaccine_policy_and_hospitalizations(df)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

region_names = {
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DC": "District of Columbia",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MP": "Northern Mariana Islands",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VI": "U.S. Virgin Islands",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming"
}
def process_google_vaccination_data():
    df=pd.read_csv("../Google_data/vaccinations.csv")
    df1=pd.read_csv("../COVID19_DATA/OxCGRT_latest.csv")
    df2=pd.read_csv("../Google_data/demographics.csv")

    df1=df1.loc[df1["CountryCode"]=="USA"]
    df1.drop(columns=["CountryCode","CountryName"],inplace=True)
    df1["Date"]=pd.to_datetime(df1["Date"],format="%Y%m%d")
    df1=df1[["Date","RegionCode","H7_Vaccination policy"]]
    
    # drop rows where location_key is NA
    df=df.dropna(subset=["location_key"])
    df=df.loc[df["location_key"].str.contains("US")]
    df["date"]=pd.to_datetime(df["date"])
    df=df.rename(columns={"date":"Date"})
    df["Date"]=pd.to_datetime(df["Date"],format="%Y-%m-%d")
    df=df.rename(columns={"location_key":"RegionCode"})

    df2=df2.dropna(subset=["location_key"])
    df2=df2.loc[df2["location_key"].str.contains("US")]
    df2=df2.rename(columns={"date":"Date"})
    df2=df2.rename(columns={"location_key":"RegionCode"})
    df2=df2[["RegionCode","population"]]
    
    df=pd.merge(df,df1,on=["Date","RegionCode"])
    df=pd.merge(df,df2,on=["RegionCode"])
    df["vaccinations_per_100"]=df["new_persons_vaccinated"]/df["population"]*100
    df["RegionCode"]=df["RegionCode"].str.replace("US_","")
    df["RegionCode"]=df["RegionCode"].map(region_names)
    df.to_csv("./transformed_data/vaccination_policy.csv",index=False)

if __name__=="__main__":
    process_google_vaccination_data()
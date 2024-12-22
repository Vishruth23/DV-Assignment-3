import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

def preprocess_data_for_gplom():
    df=pd.read_csv('../COVID19_DATA/OxCGRT_latest.csv')  
    df = df[df['CountryCode'] == 'USA']  
    df = df[['Date','H7_Vaccination policy','ConfirmedCases','ConfirmedDeaths',"StringencyIndex"]]
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
    df=df[df["Date"]>=pd.to_datetime("2021-01-01")]
    df["H7_Vaccination policy"] = df["H7_Vaccination policy"].fillna(0)
    df['ConfirmedCases'] = df['ConfirmedCases'].diff()
    df['ConfirmedDeaths'] = df['ConfirmedDeaths'].diff()
    df.drop(['Date'], axis=1, inplace=True)
    return df

def plot_gplom(df):
    plt.figure()
    """
    Creates a lower triangular Generalized Pair Plot Matrix.
    - Categorical vs. Numerical: Bar plot
    - Numerical vs. Numerical: Scatter plot
    """
    # Define categorical and numerical variables
    categorical_column = "H7_Vaccination policy"  # Adjusted for this dataset
    numerical_columns = ["ConfirmedCases", "ConfirmedDeaths","StringencyIndex"]
    
    fig, axes = plt.subplots(len(df.columns), len(df.columns), figsize=(10, 10), constrained_layout=True)
    for i, col1 in enumerate(df.columns):
        for j, col2 in enumerate(df.columns):
            ax = axes[i, j]
            
            # Clear upper triangular cells
            if i < j:
                ax.axis('off')  
                continue
            
            if col1 == categorical_column and col2 in numerical_columns:
                sns.barplot(x=col1, y=col2, data=df.groupby(categorical_column).max().reset_index(), ax=ax)
            elif col1 in numerical_columns and col2 in numerical_columns:
                sns.scatterplot(x=col2, y=col1, data=df, ax=ax, alpha=0.7)
                
            elif col1 == categorical_column and col2 == categorical_column:
                sns.heatmap(pd.crosstab(df[col1], df[col2]), annot=True, fmt='d', ax=ax)
            elif col1 in numerical_columns and col2 == categorical_column:
                sns.barplot(x=col2, y=col1, data=df.groupby(categorical_column).max().reset_index(), ax=ax)
            
            if i < len(df.columns) - 1:
                ax.set_xticks([])
                ax.set_xlabel('')
            if j > 0:
                ax.set_yticks([])
                ax.set_ylabel('')
            if i == len(df.columns) - 1:
                ax.set_xlabel(col2)
            if j == 0:
                ax.set_ylabel(col1)
            
    
  
    fig.suptitle("GPLOM", fontsize=14)
    plt.savefig("./plots/GPLOM.png")


if __name__ == "__main__":
    df=preprocess_data_for_gplom()
    plot_gplom(df)


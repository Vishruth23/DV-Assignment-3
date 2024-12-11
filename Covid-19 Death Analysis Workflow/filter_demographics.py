# %%
import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sns

# %%
df = pd.read_csv('demographics.csv')

# %%
df['location_key'].isna().sum()
df.dropna(subset=['location_key'], inplace=True)

# %%
#Only extracting the rows whose 'location_key' starts with 'US_'
us_df = df[df['location_key'].str.startswith('US_')]

# %%
us_df.to_csv('us_demographics.csv', index=False)

# %%
state_data = us_df[us_df['location_key'].str.match(r'US_[A-Z]{2}$', na=False)]

# %%
state_data.location_key.unique()

# %%
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

# Expand the values into the 4 desired columns
def expand_location_key(location_key):
    country_code = "US"  # Fixed for this dataset
    country_name = "United States"
    region_code = location_key.split("_")[-1]
    region_name = region_names.get(region_code, "Unknown")  # Map region code to full name
    return country_name, "USA", region_name, location_key

# Apply the function to create new columns
state_data_expanded = state_data.copy()
state_data_expanded[['CountryName', 'CountryCode', 'RegionName', 'RegionCode']] = state_data_expanded[
    'location_key'].apply(lambda x: pd.Series(expand_location_key(x)))

# Display the updated dataframe
state_data_expanded.head()


# %%
# Specify the desired column order
new_order = ['CountryName', 'CountryCode', 'RegionName', 'RegionCode'] + \
            [col for col in state_data_expanded.columns if col not in ['CountryName', 'CountryCode', 'RegionName', 'RegionCode']]

# Reorder the DataFrame columns
state_data_expanded = state_data_expanded[new_order]

# Display the updated DataFrame
state_data_expanded.head()


# %%
state_data_expanded.drop(columns=['location_key'], inplace=True)

# %%
state_data_expanded.to_csv('us_states_demographics.csv', index=False)



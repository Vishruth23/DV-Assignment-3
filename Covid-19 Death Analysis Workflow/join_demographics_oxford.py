# %%
import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sns

# %%
oxford_data = pd.read_csv('us_state_oxford.csv')
demographics_data = pd.read_csv('us_states_demographics.csv')

# %%
oxford_data.head()

# %%
demographics_data.head()

# %%
# Merge the two dataframes if it's not there in the oxford data then it will not be included in the final dataframe
merged_data = pd.merge(oxford_data, demographics_data, on='RegionName', how='inner')
merged_data.head()


# %%
merged_data.columns

# %%
merged_data

# %%
#the Date column is in string format 'YYYYMMDD', so we need to convert it to datetime format
merged_data['Date'] = pd.to_datetime(merged_data['Date'], format='%Y%m%d')

#Take the maximum value of ConfirmedCases and ConfirmedDeaths for each state and per month and make a new column called ConfirmedCasesAtEOM and ConfirmedDeathsAtEOM
merged_data['ConfirmedCasesAtEOM'] = merged_data.groupby(['RegionName', merged_data['Date'].dt.to_period('M')])['ConfirmedCases'].transform('max')

# %%
merged_data['ConfirmedDeathsAtEOM'] = merged_data.groupby(['RegionName', merged_data['Date'].dt.to_period('M')])['ConfirmedDeaths'].transform('max')

# %%
merged_data.to_csv('us_states_oxford_demographics.csv', index=False)

# %%
#Take the month of december 2020 and make a new dataframe
december_data = merged_data[merged_data['Date'].dt.to_period('M') == '2020-12']

# %%
december_data.to_csv('us_states_oxford_demographics_december.csv', index=False)



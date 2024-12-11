# %%
import pandas as pd
import numpy as np

# %%
df =  pd.read_csv('us_states_oxford_demographics.csv')

# %%
# Ensure the 'Date' column is a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by 'Date' to ensure chronological order
df = df.sort_values(by='Date')

# Group by 'RegionName' and year-month, then get the last entry of each month
last_entries = df.groupby(
    ['RegionName', df['Date'].dt.to_period('M')]
).apply(lambda group: group.loc[group['Date'].idxmax()])

# Reset index to turn the grouped columns back into normal columns
last_entries = last_entries.reset_index(drop=True)

# Save the DataFrame to a new CSV file
last_entries.to_csv('monthly_usa_data.csv', index=False)




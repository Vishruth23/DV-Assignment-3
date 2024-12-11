import pandas as pd

# Load the CSV file
df = pd.read_csv('./OxCGRT_latest_combined.csv', low_memory=False)

# Filter the dataframe for the required conditions
filtered_df = df.loc[(df['CountryCode'] == 'NOR') & (df['Jurisdiction'] == 'NAT_TOTAL')]

# Select only the required columns
filtered_df = filtered_df[['CountryCode', 'ConfirmedCases', 'Date']]

# Convert 'Date' to datetime format, specifying the format as 'yyyymmdd'
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], format='%Y%m%d', errors='coerce')

# Check for rows where the 'Date' is NaT (i.e., failed conversion)
if filtered_df['Date'].isna().any():
    print("Warning: Some dates could not be parsed correctly.")

# Sort by Date to ensure the data is in chronological order
filtered_df = filtered_df.sort_values('Date')

# Calculate the daily confirmed cases by finding the difference between consecutive days
filtered_df['DailyConfirmedCases'] = filtered_df['ConfirmedCases'].diff().fillna(0).clip(lower=0).astype(int)

# Convert 'Date' to the desired format (e.g., '1/3/2012')
filtered_df['Date'] = filtered_df['Date'].dt.strftime('%-m/%-d/%Y')

# Export the filtered dataframe with daily confirmed cases to a new CSV file
filtered_df = filtered_df[['CountryCode', 'DailyConfirmedCases', 'Date']]  # Keep only the relevant columns
filtered_df.to_csv('./NZ_confirmed_cases.csv', index=False)

print("Daily confirmed cases have been saved to NOR_confirmed_cases.csv")

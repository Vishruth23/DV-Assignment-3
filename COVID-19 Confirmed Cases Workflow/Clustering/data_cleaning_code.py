import pandas as pd

# Load the data
gov_response = pd.read_csv("government_response_index.csv")

# Remove any unnamed columns
gov_response = gov_response.loc[:, ~gov_response.columns.str.contains('^Unnamed')]

# Reshape the data into long format
gov_response_long = pd.melt(
    gov_response, 
    id_vars=["country_code", "country_name"], 
    var_name="Date", 
    value_name="GovernmentResponseIndex"
)

# Convert to datetime format
gov_response_long['Date'] = pd.to_datetime(
    gov_response_long['Date'], 
    format='%d%b%Y', 
    errors='coerce'
)

# Drop invalid dates
gov_response_long = gov_response_long.dropna(subset=['Date'])

# Extract month-year and calculate monthly averages
gov_response_long['Month-Year'] = gov_response_long['Date'].dt.to_period('M')
gov_response_monthly = gov_response_long.groupby(
    ['country_code', 'country_name', 'Month-Year']
)['GovernmentResponseIndex'].mean().reset_index()

# Pivot back to wide format
gov_response_pivot = gov_response_monthly.pivot(
    index=['country_code', 'country_name'], 
    columns='Month-Year', 
    values='GovernmentResponseIndex'
).reset_index()

gov_response_pivot = gov_response_pivot.round(2)

# Save the transformed data with rounded values
gov_response_pivot.to_csv("monthly_gov_response.csv", index=False)


# Load the confirmed cases data
confirmed_cases = pd.read_csv("confirmed_cases.csv")

# Reshape the data into long format
confirmed_cases_long = pd.melt(
    confirmed_cases, 
    id_vars=["country_code", "country_name"], 
    var_name="Date", 
    value_name="ConfirmedCases"
)

# Convert to datetime format
confirmed_cases_long['Date'] = pd.to_datetime(
    confirmed_cases_long['Date'], 
    format='%b%Y', 
    errors='coerce'
)

# Drop invalid dates
confirmed_cases_long = confirmed_cases_long.dropna(subset=['Date'])

# Extract month-year
confirmed_cases_long['Month-Year'] = confirmed_cases_long['Date'].dt.to_period('M')

# Calculate monthly new cases (non-cumulative)
confirmed_cases_long = confirmed_cases_long.sort_values(by=['country_code', 'Date'])
confirmed_cases_long['NewCases'] = confirmed_cases_long.groupby(['country_code'])['ConfirmedCases'].diff().fillna(confirmed_cases_long['ConfirmedCases'])

# Group by month-year and calculate the sum of new cases
confirmed_cases_monthly = confirmed_cases_long.groupby(
    ['country_code', 'country_name', 'Month-Year']
)['NewCases'].sum().reset_index()

# Pivot back to wide format
confirmed_cases_pivot = confirmed_cases_monthly.pivot(
    index=['country_code', 'country_name'], 
    columns='Month-Year', 
    values='NewCases'
).reset_index()

confirmed_cases_pivot = confirmed_cases_pivot.round(2)

# Save the transformed data with rounded values
confirmed_cases_pivot.to_csv("monthly_confirmed_cases.csv", index=False)
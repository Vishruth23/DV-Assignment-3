# %%
import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sns

# %%
df = pd.read_csv('OxCGRT_latest.csv')

# %%
us_state_df = df[df['CountryName'] == 'United States']

# %%
us_state_df = us_state_df[us_state_df['Jurisdiction'] == 'STATE_TOTAL']

# %%
us_state_df.columns



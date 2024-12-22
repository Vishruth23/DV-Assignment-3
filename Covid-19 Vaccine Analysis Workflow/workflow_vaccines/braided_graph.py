import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_smoothed_braided_subplots():
    df = pd.read_csv("./transformed_data/hospitalizations_and_vaccinations.csv")
    
    df = df.loc[df["RegionName"].isin(["Washington", "Kentucky", "Oklahoma", "Alaska"])]
    
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date")
    
    # Smoothing function using a rolling average
    def smooth_series(series, window=7):
        return series.rolling(window=window, min_periods=1, center=True).mean()
    
    # Create a 2x2 grid of subplots for the regions
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
    regions = df["RegionName"].unique()
    
    for idx, region in enumerate(regions):
        row, col = divmod(idx, 2)  # Determine subplot row and column
        ax = axes[row, col]
        
        df_region = df[df["RegionName"] == region]
        
        x = df_region["Date"]
        y1 = df_region["vaccinations_per_population"].fillna(0)
        y2 = df_region["hospitalizations_per_100"].fillna(0)
        
        # Smooth the data
        y1_smooth = smooth_series(y1)
        y2_smooth = smooth_series(y2)
        
        # Calculate intersections
        intersections = np.where(np.diff(np.sign(y1_smooth - y2_smooth)))[0]
        
        start = 0
        
        for i in intersections:
            end = i + 1
            
            if y1_smooth.iloc[start] > y2_smooth.iloc[start]:
                ax.fill_between(x.iloc[start:end], y2_smooth.iloc[start:end], 0, color="orange", alpha=0.6, label="Hospitalizations" if start == 0 else "")
                ax.fill_between(x.iloc[start:end], y1_smooth.iloc[start:end], y2_smooth.iloc[start:end], color="blue", alpha=0.6, label="Vaccinations" if start == 0 else "")
            else:
                ax.fill_between(x.iloc[start:end], y1_smooth.iloc[start:end], 0, color="blue", alpha=0.6, label="Vaccinations" if start == 0 else "")
                ax.fill_between(x.iloc[start:end], y2_smooth.iloc[start:end], y1_smooth.iloc[start:end], color="orange", alpha=0.6, label="Hospitalizations")
            
            start = end
        
        if y1_smooth.iloc[start] > y2_smooth.iloc[start]:
            ax.fill_between(x.iloc[start:], y2_smooth.iloc[start:], 0, color="orange", alpha=0.6, label="Hospitalizations" if start == 0 else "")
            ax.fill_between(x.iloc[start:], y1_smooth.iloc[start:], y2_smooth.iloc[start:], color="blue", alpha=0.6, label="Vaccinations" if start == 0 else "")
        else:
            ax.fill_between(x.iloc[start:], y1_smooth.iloc[start:], 0, color="blue", alpha=0.6, label="Vaccinations" if start == 0 else "")
            ax.fill_between(x.iloc[start:], y2_smooth.iloc[start:], y1_smooth.iloc[start:], color="orange", alpha=0.6, label="Hospitalizations")
        
        ax.set_title(region)
        ax.legend(["Cumulative Vaccinations\nper population","Normalized Hospitalizations\nper 100" ], loc="upper left")        
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.grid(True)
        ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig("./plots/braided_subplots.png")

plot_smoothed_braided_subplots()


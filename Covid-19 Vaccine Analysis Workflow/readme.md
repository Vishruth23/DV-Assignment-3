# Analysis of COVID-19 Vaccination in the United States

This project focuses on analyzing COVID-19 vaccination and hospitalization data, providing scripts for data preprocessing, analysis, and visualization. This guide outlines the project structure, how to install the necessary requirements, and instructions for running each Python script.

## Project Structure

```
COVID19_DATA/
    Cleaned_data/
    OxCGRT_latest_allchanges.csv
    OxCGRT_latest_combined.csv
    OxCGRT_latest_responses.csv
    OxCGRT_latest_withnotes.csv
    OxCGRT_latest.csv
    OxCGRT_vaccines_full.csv
    OxCGRT_withnotes_2020.csv
    OxCGRT_withnotes_2021.csv
    timeseries/
Google_data/
    demographics.csv
    hospitalizations.csv
    vaccinations.csv
readme.md
requirements.txt
workflow_vaccines/
    braided_graph.py
    gplom.py
    hospitalizations.py
    kmeans.py
    plots/
    preprocess_for_tableau.py
    transformed_data/
    workbooks/
```



COVID19_DATA([OxCGRT Data](https://www.kaggle.com/datasets/ruchi798/oxford-covid19-government-response-tracker))

Contains COVID-19 datasets, including various versions of the Oxford COVID-19 Government Response Tracker (OxCGRT) data and time series data. 


Google_data

Includes demographic data and datasets on hospitalizations and vaccinations.
- **`requirements.txt`**: Lists the Python packages required to run the scripts.


workflow_vaccines

Contains Python scripts for data preprocessing, analysis, and visualization related to vaccination data.

```braided_graph.py``` -> To plot fig 20

```gplom.py``` -> To plot fig 16

```hospitalization.py``` -> To plot fig 17

```preprocess_for_tableau``` -> for tableau plots

```kmeans.py``` -> For clustering plot

## Installing Requirements

**Install the required Python packages:**

   ```sh
   pip install -r requirements.txt
   ```

## Running Each Script

All scripts are located in the workflow_vaccines directory.

To run them:

- Make sure your CWD is ```workflow_vaccines```
- To run any file:
```bash
python3 <filename>.py 
```



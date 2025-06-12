# Covid-19 Visual Analytics Workflow

This repository contains various workflows and scripts for analyzing and visualizing COVID-19 data, including confirmed cases, deaths, and vaccinations. The project is organized into multiple workflows, each focusing on a specific aspect of the COVID-19 pandemic.

## Project structure

```
COVID-19 Confirmed Cases Workflow/
    Calendar Chart/
        daily_filtered_data.csv
        data_cleaning.py
        epi.py
        monthly_gov_response.csv
    Clustering/
        clustering_algorithm.py
        clustering_data_tableau_normalized_2020-06.csv
        clustering_data_tableau_normalized_2020-12.csv
        confirmed_cases.csv
        COVID-19-Cases-workbook.twb
        data_cleaning_code.py
        government_response_index.csv
        monthly_confirmed_cases.csv
        monthly_gov_response.csv
Covid-19 Death Analysis Workflow/
    ~PopulationDensity_ConfirmedDeaths__21180.twbr
    demographics.csv
    filter_demographics.py
    filter_oxc19.py
    join_demographics_oxford.py
    monthly_usa_data.csv
    OxCGRT_latest.csv
    PopulationDensity_ConfirmedDeaths.twb
    treemap.html
    treemap.py
    us_demographics.csv
    us_state_oxford.csv
    us_states_demographics.csv
    us_states_oxford_demographics_december.csv
    us_states_oxford_demographics.csv
Covid-19 Vaccine Analysis Workflow/
    COVID19_DATA/
        OxCGRT_latest.csv
        OxCGRT_vaccines_full.csv
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
        preprocess_for_tableau.py
        transformed_data/
            hospitalizations_and_vaccinations.csv
            vaccination_policy.csv
        workbooks/
            books.twb
            hospitalization_per_100.twb
README.md
```

## Workflows

### COVID-19 Confirmed Cases Workflow

This workflow focuses on analyzing and visualizing confirmed COVID-19 cases. It includes scripts for data cleaning, clustering, and generating visualizations.

* `Calendar Chart/`
  - `COVID-19 Confirmed Cases Workflow/Calendar Chart/data_cleaning.py`: Script for cleaning and filtering COVID-19 confirmed cases data.
  - `COVID-19 Confirmed Cases Workflow/Calendar Chart/epi.py`: Script for epidemiological analysis.
  - `COVID-19 Confirmed Cases Workflow/Calendar Chart/monthly_gov_response.csv`: Monthly government response data.

* `Clustering/`
  - `COVID-19 Confirmed Cases Workflow/Clustering/clustering_algorithm.py`: Script for clustering countries based on government response and confirmed cases.
  - `COVID-19 Confirmed Cases Workflow/Clustering/data_cleaning_code.py`: Script for cleaning and transforming government response and confirmed cases data.
  - `COVID-19 Confirmed Cases Workflow/Clustering/confirmed_cases.csv`: Confirmed cases data.
  - `COVID-19 Confirmed Cases Workflow/Clustering/government_response_index.csv`: Government response index data.
  - `COVID-19 Confirmed Cases Workflow/Clustering/monthly_confirmed_cases.csv`: Monthly confirmed cases data.
  - `COVID-19 Confirmed Cases Workflow/Clustering/monthly_gov_response.csv`: Monthly government response data.

### Covid-19 Death Analysis Workflow

This workflow focuses on analyzing and visualizing COVID-19 death data. It includes scripts for filtering, joining, and visualizing demographic and Oxford data.

* `Covid-19 Death Analysis Workflow/filter_demographics.py`: Script for filtering US demographics data.
* `Covid-19 Death Analysis Workflow/filter_oxc19.py`: Script for filtering Oxford COVID-19 data.
* `Covid-19 Death Analysis Workflow/join_demographics_oxford.py`: Script for joining US demographics and Oxford data.
* `Covid-19 Death Analysis Workflow/treemap.py`: Script for generating a treemap visualization of COVID-19 deaths.

### Covid-19 Vaccine Analysis Workflow

This workflow focuses on analyzing and visualizing COVID-19 vaccination data. It includes scripts for data preprocessing, analysis, and visualization.

* `COVID19_DATA/`
  - `Covid-19 Vaccine Analysis Workflow/COVID19_DATA/OxCGRT_latest.csv`: Latest Oxford COVID-19 Government Response Tracker data.
  - `Covid-19 Vaccine Analysis Workflow/COVID19_DATA/OxCGRT_vaccines_full.csv`: Full vaccination data from Oxford.

* `Google_data/`
  - `Covid-19 Vaccine Analysis Workflow/Google_data/demographics.csv`: Demographic data.
  - `Covid-19 Vaccine Analysis Workflow/Google_data/hospitalizations.csv`: Hospitalization data.
  - `Covid-19 Vaccine Analysis Workflow/Google_data/vaccinations.csv`: Vaccination data.

* `workflow_vaccines/`
  - `braided_graph.py` (F2b): Script for plotting braided graphs of hospitalizations and vaccinations.
  - `Covid-19 Vaccine Analysis Workflow/workflow_vaccines/gplom.py`: Script for generating a Generalized Pair Plot Matrix (GPLOM).
  - `Covid-19 Vaccine Analysis Workflow/workflow_vaccines/hospitalizations.py`: Script for analyzing vaccine policy and hospitalizations.
  - `Covid-19 Vaccine Analysis Workflow/workflow_vaccines/kmeans.py`: Script for clustering countries based on vaccination scores.
  - `Covid-19 Vaccine Analysis Workflow/workflow_vaccines/preprocess_for_tableau.py`: Script for preprocessing data for Tableau visualizations.

## Requirements

The project requires the following Python packages:

* numpy
* matplotlib
* seaborn
* pandas

To install the required packages, run:

```sh
pip install -r requirements.txt
```

## Running the scripts

To run the scripts, navigate to the appropriate workflow directory and execute the desired script. For example, to run the `braided_graph.py` script in the `workflow_vaccines` directory:

```sh
cd Covid-19\ Vaccine\ Analysis\ Workflow/workflow_vaccines
python3 braided_graph.py
```

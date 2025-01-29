# Master-thesis

Repository for my master thesis project: 

<b><i>"How much to pay for a night? Determinants of Airbnb housing prices with Deep Learning"</i></b>

## Introduction

Airbnb is a global platform offering short-term rental services, with over 7 million listings in 81,000 cities across 191 countries. Pricing rental properties remains a challenge for hosts, as it significantly influences customer demand. 

Identifying the factors that affect rental prices is crucial for effective accommodation management, helping hosts address service gaps and set competitive prices.

This project focuses on analyzing key pricing determinants for Airbnb listings and leveraging machine learning techniques to predict rental prices.

## Project structure

The project is structured as follows:

📦Project <br>
 ┣ :file_folder: Data <br>
 ┣ :file_folder: Location <br>
 ┣ :file_folder: Metadata <br>
 ┣ :file_folder: saved_models <br>
 ┣ :notebook: 1. Merge_listings.ipynb <br>
 ┣ :notebook: 2. EDA.ipynb <br>
 ┣ :notebook: 3. OLS.ipynb <br>
 ┣ :notebook: 4. XGBoost.ipynb <br>
 ┣ :notebook: 5. Neural Network.ipynb <br>
 ┗ :notebook: 6. Ensemble.ipynb 

## Data

📦Data <br>
 ┣ :file_folder: Location <br>
 ┃ ┣ :green_book: bus_stops.csv <br>
 ┃ ┣ :green_book: crimes.csv <br>
 ┃ ┣ :green_book: cultural.csv <br>
 ┃ ┣ :green_book: education.csv <br>
 ┃ ┣ :green_book: health.csv <br>
 ┃ ┣ :green_book: main_attractions.csv <br>
 ┃ ┣ :green_book: recreation.csv <br>
 ┃ ┣ :green_book: religious.csv
 ┃ ┣ :green_book: restaurants.csv
 ┃ ┗ :green_book: subway_stations.csv
 ┣ :green_book: listings.csv
 ┣ :green_book: listings_cleaned.csv
 ┣ :green_book: listings_eda.csv
 ┣ :green_book: location_features.csv
 ┗ :green_book: airbnb_data.csv

The data folder contains:
- :file_folder: Location folder with information about geographical location of Points of Interest in New York City (each csv file was limited to 100 rows for GitHub upload).
- :green_book: listings.csv: raw dataset containing information about Airbnb listings in New York City (limited to 100 rows for GitHub upload).
- :green_book: listings_cleaned.csv: dataset after initial data cleaning (limited to 100 rows for GitHub upload).
- :green_book: listings_eda.csv: dataset after exploratory data analysis and feature engineering (limited to 100 rows for GitHub upload).
- :green_book: location_features.csv: dataset containing location features for Airbnb listings in New York City (limited to 100 rows for GitHub upload).
- :green_book: **airbnb_data.csv**: dataset after combining listings_eda.csv and location_features.csv. Final dataset used for model training and evaluation.

## Location

📦Location
 ┣ :file_folder: Data
 ┃ ┣ :green_book: bus_stops.csv
 ┃ ┣ :green_book: neighbourhoods.geojson
 ┃ ┣ :green_book: NYPD_crimes.csv
 ┃ ┣ :green_book: Points_of_Interest.csv
 ┃ ┣ :green_book: Point_Of_Interest_dictionary.pdf
 ┃ ┣ :green_book: restaurants.csv
 ┃ ┗ :green_book: subway_stations.csv
 ┣ :notebook: 1. Location_Processing.ipynb
 ┗ :notebook: 2. Location_EDA.ipynb

The Location folder contains:
- :file_folder: Data folder with information about geographical location of Points of Interest in New York City (each csv file was limited to 100 rows for GitHub upload).
- :notebook: 1. Location_Processing.ipynb: Jupyter notebook for processing location data.
- :notebook: 2. Location_EDA.ipynb: Jupyter notebook for exploratory data analysis of location data and feature engineering (mostly creating distance features).

## Metadata

📦Metadata
 ┣ :notebook: 1. Metadata_Processing.ipynb
 ┗ :notebook: 2. Metadata_EDA.ipynb

The Metadata folder contains:
- :notebook: 1. Metadata_Processing.ipynb: Jupyter notebook for processing metadata.
- :notebook: 2. Metadata_EDA.ipynb: Jupyter notebook for exploratory data analysis of metadata and feature engineering.

## saved_models

📦saved_models
 ┣ :page_with_curl: model_LR.pkl
 ┣ :page_with_curl: model_NN.pkl
 ┗ :page_with_curl: model_XGB.pkl

The saved_models folder contains:
- :page_with_curl: model_LR.pkl: saved Linear Regression model.
- :page_with_curl: model_NN.pkl: saved Neural Network model.
- :page_with_curl: model_XGB.pkl: saved XGBoost model.

## Notebooks

📦Notebooks
 ┣ :notebook: 1. Merge_listings.ipynb
 ┣ :notebook: 2. EDA.ipynb
 ┣ :notebook: 3. OLS.ipynb
 ┣ :notebook: 4. XGBoost.ipynb
 ┣ :notebook: 5. Neural Network.ipynb
 ┗ :notebook: 6. Ensemble.ipynb

The Notebooks folder contains:
- :notebook: 1. Merge_listings.ipynb: Jupyter notebook for merging multiple listings datasets from Inside Airbnb and different months.
- :notebook: 2. EDA.ipynb: Jupyter notebook for exploratory data analysis and feature engineering.
- :notebook: 3. OLS.ipynb: Jupyter notebook for Ordinary Least Squares regression (benchmark model).
- :notebook: 4. XGBoost.ipynb: Jupyter notebook for XGBoost regression.
- :notebook: 5. Neural Network.ipynb: Jupyter notebook for Neural Network regression.
- :notebook: 6. Ensemble.ipynb: Jupyter notebook for Ensemble model combining XGBoost and Neural Network predictions.
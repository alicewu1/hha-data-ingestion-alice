# hha-data-ingestion-alice

HHA507 Data Science / Assignment 1


## This repo aims to:
# 1. Find or create an excel (.xls) file that contains at least two tabs. Bring in the first tab as a data frame; label that dataset as ‘tab1’, and a second data frame that represents the 2nd tab of the excel file, name this 'tab2'   
- https://github.com/alicewu1/hha-data-ingestion-alice/blob/1e29573f4e4e4b8f57070983a726233c37d4e1fb/ingestion.py#L10-L21

# 2. Find 1 open source json API via CMS, and retrieve it using **requests** package ; call the dataset ‘apiDataset’ 
-     data = requests.get('https://data.cms.gov/data-api/v1/dataset/ad73e4d3-925b-4055-ad9b-7f0015e906c8/data&#39;)
      data = data.json() 

- https://github.com/alicewu1/hha-data-ingestion-alice/blob/1e29573f4e4e4b8f57070983a726233c37d4e1fb/ingestion.py#L24-L31

# 3. Brings in 2 open source bigquery datasets
- Limit your query to get the first 100 rows from each, as either a dataframe or dictionary; please call the first dataset ‘bigquery1’ and the second dataset ‘bigquery2’;  
- https://github.com/alicewu1/hha-data-ingestion-alice/blob/1e29573f4e4e4b8f57070983a726233c37d4e1fb/ingestion.py#L34-L46

# Packages Used:
-     import requests 
      import json
      import pandas as pd ## import pandas for general file types 
      from google.cloud import bigquery ## import bigquery for bigquery files
      import xlrd ## import xlrd for excel files, tab names 
      import openpyxl ## import openpyxl to read Excel 2010 .xlsx files
      import db_dtypes #import db_btypes to resolve section3 compatibility issues


# Resources:
- [Kaggle](https://www.kaggle.com/datasets)
- [Healthdata.gov](healthdata.gov)
- [CMS](https://data.cms.gov/)
- [Instructions for connecting to bigquery via a client (e.g., python)](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries)
- [Helper YouTube Video](https://www.youtube.com/watch?v=iolQX4XJN2A) that walks through how to create the special .json file to connect

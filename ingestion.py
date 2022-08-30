##import libraries
import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import requests ## import requests for web requests
from google.cloud import bigquery ## import bigquery for bigquery files
import xlrd ## import xlrd for excel files, tab names 
import openpyxl ## import openpyxl to read Excel 2010 .xlsx files
import db_dtypes #import db_btypes to resolve section3 compatibility issues

## SECTION 1: Reading Excel Datasets from Kaggle using pandas
## consolidated 2 kaggle datasets into 1 excel file

## defining variables
## fixed unicode error in path using r and double quotes
xls = xlrd.open_workbook(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls", on_demand=True)
xls = pd.ExcelFile(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls") ##to read multiple excel sheets
##defining dataframes for visualization
tab1 = pd.read_excel(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls", sheet_name='tab1') #for sheet1
print (tab1) ##view output
tab2 = pd.read_excel(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls", sheet_name='tab2') #for sheet2
print (tab2) ##view output


## SECTION 2: Retrieve open source json API from CMS website
## use requests to retrieve json API from CMS
apiDataset=requests.get('https://data.cms.gov/data-api/v1/dataset/b35c77ac-26e2-4320-91e1-ba71c4d7ff2c/data')
## load as json
apiDataset=apiDataset.json()
## load into dataframe for visualization
df = pd.DataFrame.from_records(apiDataset)
print(df) ## view output


## SECTION 3: GCP BigQuery using google-cloud-bigquery
## create json key on GCP service account 
## add json key to .gitignore

## connect to  big query
client = bigquery.Client.from_service_account_json(r"C:\Users\Lcw62\hha-data-ingestion-alice\big query\section-3-360719-c5f4ca6c60ec.json") 
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100") ## query public dataset
## get results
results = query_job.result()
## put results into dataframe for visualization
bigquery1 = pd.DataFrame(results.to_dataframe())
print(bigquery1) ## view output

## SECOND BIGQUERY
client = bigquery.Client.from_service_account_json(r"C:\Users\Lcw62\hha-data-ingestion-alice\big query\section-3-360719-c5f4ca6c60ec.json") 
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.covid19_public_forecasts.japan_prefecture_28d` LIMIT 100") ## query public dataset
## get results
results = query_job.result()
## put results into dataframe for visualization
bigquery2 = pd.DataFrame(results.to_dataframe())
print(bigquery2) ##view output
## add venv to .gitignore
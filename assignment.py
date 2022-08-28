##import libraries
import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import sqlalchemy ## import sqlalchemy for sql queries
from PIL import Image  ## import pillow for image files
import pydub ## import pydub for audio files
from pydub.playback import play
import playsound ## import playsound for audio files
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 
import PyPDF2 ## import PyPDF2 for pdf files
import openpyxl
import db_dtypes

##SECTION 1: Kaggle Consolidated Datasets (2)
##defining variables
##fixed unicode error using r and double quotes
xls = xlrd.open_workbook(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls", on_demand=True)
xls = pd.ExcelFile(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls") ##to read multiple excel sheets
##defining dataframes
tab1 = pd.read_excel(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls", sheet_name='tab1')
print (tab1) ##view output
tab2 = pd.read_excel(r"C:\Users\Lcw62\hha-data-ingestion-alice\data\kaggle_data.xls", sheet_name='tab2')
print (tab2) ##view output


##SECTION 2: Retrieve open source json API from CMS website
##get request
apiDataset=requests.get('https://data.cms.gov/data-api/v1/dataset/b35c77ac-26e2-4320-91e1-ba71c4d7ff2c/data')
##load as json
apiDataset=apiDataset.json()
##load intro dataframe
apiDataset = pd.read_json(apiDataset)
print (apiDataset) ##view output


##SECTION 3: GCP BigQuery
##create json key on GCP service account 
##.gitignore json key 

##connect to  big query
client = bigquery.Client.from_service_account_json(r"C:\Users\Lcw62\hha-data-ingestion-alice\big query\section-3-360719-c5f4ca6c60ec.json") 
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100") ## query public dataset
##get results
results = query_job.result()
## put results into dataframe
bigquery1 = pd.DataFrame(results.to_dataframe())
print(bigquery1) ## view output

## SECOND BIGQUERY
client = bigquery.Client.from_service_account_json(r"C:\Users\Lcw62\hha-data-ingestion-alice\big query\section-3-360719-c5f4ca6c60ec.json") 
##query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.covid19_public_forecasts.japan_prefecture_28d` LIMIT 100") ## query public dataset
##get results
results = query_job.result()
## put results into dataframe
bigquery2 = pd.DataFrame(results.to_dataframe())
print(bigquery2) ##view output
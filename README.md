# hha-data-ingestion-alice

HHA507 Data Science
Assignment 1

Instructions: 
Create a Github repo called ‘hha-data-ingestion’ in your account and write a python script (.py file) that does the following below (Section 1, Section 2, Section 2). 
Please include a folder in the repo called 'data',  that contains the excel files that you use for Section 1. 
Please provide PUBLIC repo,  GitHub URL when submitting this assignment. 
Please use comments (# or """) in your .py script to let me know what you are doing. 
If you run into any errors that you can't solve, please take screen shots of those errors, and put them into a 'error' folder inside of your github repo so I can see what they were. 

Deliverables: 
 
- Section 1: Find or create 1 excel (.xls) file that contains at least two tabs. Bring in the first tab as a data frame; label that dataset as ‘tab1’, and a second data frame that represents the 2nd tab of the excel file, name this 'tab2'   
            Resource: creating via your local computer, Kaggle (https://www.kaggle.com/datasets), healthdata.gov, etc.... 

- Section 2: Find 1 open source json API via CMS, and bring it in using the 'requests' package ; call the dataset ‘apiDataset’ 

Resource: https://data.cms.gov/
import requests 
import json
data = requests.get('https://data.cms.gov/data-api/v1/dataset/ad73e4d3-925b-4055-ad9b-7f0015e906c8/data&#39;)
data = data.json() 
- Section 3 (TRY YOUR BEST): Brings in 2 open source bigquery datasets; limit your query to get the first 100 rows from each, as either a dataframe or dictionary; please call the first dataset ‘bigquery1’ and the second dataset ‘bigquery2’;  
Instructions for connecting to bigquery via a client (e.g., python): https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries 
Helper youtube video - If you have trouble, I would recommend watching the first couple minutes that walks through how to create the special .json file to connect: https://www.youtube.com/watch?v=iolQX4XJN2A
# IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os         
import pandas as pd
import mysql.connector
import module1_features as m1
import module2_scraper as m2
import csv

# MYSQL CONNECTOR
mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'ccirelli2',
        passwd= 'Work4starr', 
	database = 'JUSTIA'
        )


# TEST URL
file_name = 'b2r_justia_urls.txt'
pwd = r'/home/ccirelli2/Desktop/Repositories/justia_scraper/' 

# DEFINE BY ROW CSV READER
'''note that we should probably revised the csv file to get rid of this delimiter
 as it may create issues with a different file'''
with open(pwd+file_name, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='"')
	for row in reader:
		url = row[0]
		
		



















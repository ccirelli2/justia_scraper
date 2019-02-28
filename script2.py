from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import pandas as pd
import mysql.connector

def write_to_excel(dataframe, filename, target_dir, add_datetime):
    '''Inputs:  dataframe, filename, target_dir'''
    os.chdir(target_dir)

    # Add datetime to filename or not
    if add_datetime == True:
        filename = filename + '_' + str(datetime.today())
    else:
        filename = filename

    writer = pd.ExcelWriter(filename+'.xlsx')
    dataframe.to_excel(writer, 'Data')
    print('Dataframe {} has been written to {}'.format(filename, target_dir))
    writer.save()



mydb = mysql.connector.connect(
	host = 'localhost', 
	user = 'ccirelli2', 
	passwd= 'Work4starr'
        )

# Import File With URLs
url = 'https://dockets.justia.com/docket/california/cacdce/2:2019cv01408/738046'


# Define Driver Scraper Function:
def justia_scraper(url):

	# Create HTML object
	html 			= urlopen(url)
	# Create Beautiful Soup Object
	bsObj 			= BeautifulSoup(html.read(), 'lxml')
	# Create Page Cotent Object (Where Content We are Looking to Scrape is located)
	content 		= bsObj.find('div', {'class':'primary-content'})
	# Scrape Features
	heading 		= content.find('h1', {'class':'heading-1'})
	plaintiff 		= content.find('td', {'data-th':'Plaintiff'})
	defendant 		= content.find('td', {'data-th':'Defendant'})
	Case_number 		= content.find('td', {'data-th':'Case Number'})
	Filed 			= content.find('td', {'data-th':'Filed'})
	Court 			= content.find('td', {'data-th':'Court'})
	Presiding_judge 	= content.find('td', {'data-th':'Presiding Judge'})
	judge_0                 = content.find('td', {'data-th':'0 Judge'})
	judge_1                 = content.find('td', {'data-th':'1 Judge'})
	Nature_of_suit 		= content.find('td', {'data-th':'Nature of Suit'})
	Cause_of_action 	= content.find('td', {'data-th':'Cause of Action'})
	Jury_demanded_by 	= content.find('td', {'data-th':'Jury Demanded By'})

	print(Jury_demanded_by.text)

justia_scraper(url)










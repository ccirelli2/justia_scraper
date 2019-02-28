from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import pandas as pd
import mysql.connector
import module1_features as m1




def justia_scraper(url):

        # Create HTML object
        html                    = urlopen(url)
        # Create Beautiful Soup Object
        bsObj                   = BeautifulSoup(html.read(), 'lxml')
        # Create Page Cotent Object (Where Content We are Looking to Scrape is located)
        content                 = bsObj.find('div', {'class':'primary-content'})
        # Scrape Features
        heading                 = m1.get_heading(content)
        plaintiff               = m1.get_plaintiff(content)
        defendant               = m1.get_defendant(content)
        case_number             = m1.get_case_number(content)
        filed                   = m1.get_filed(content)
        court                   = m1.get_court(content)
        presiding_judge         = m1.get_presiding_judge(content)
        judge_0                 = m1.get_judge0(content)
        judge_1                 = m1.get_judge1(content)
        nature_of_suit          = m1.get_nature_of_suit(content)
        cause_of_action         = m1.get_cause_of_action(content)
        jury_demanded_by        = m1.get_jury_demanded_by(content)

        # Insert Statement
        mycursor = mydb.cursor()
        sql = '''INSERT INTO justia_data (
                                        url, 
                                        heading, 
                                        plaintiff, 
                                        defendant, 
                                        case_number, 
                                        filed, 
                                        court, 
                                        presiding_judge, 
                                        judge_0, 
                                        judge_1, 
                                        nature_of_suit, 
                                        cause_of_action, 
                                        jury_demanded_by)       
                 VALUES (%s, %s, %s, %s, 
                         %s, %s, %s, %s, 
                         %s, %s ,%s, %s, %s)
              '''
        val = (url, heading, plaintiff, defendant, case_number,
               filed, court, presiding_judge, judge_0, judge_1,
               nature_of_suit, cause_of_action, jury_demanded_by)

        mycursor.execute(sql, val)
        mydb.commit()






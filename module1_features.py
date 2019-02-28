# IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import pandas as pd
import mysql.connector
import module1_features as m1



def get_heading(content):
	try:
		heading = content.find('h1', {'class':'heading-1'}).text
		return heading
	except AttributeError:
		return None

def get_plaintiff(content):
	try:
		plaintiff = content.find('td', {'data-th':'Plaintiff'}).text
		return plaintiff
	except AttributeError:
		return None


def get_defendant(content):
	try:
		defendant = content.find('td', {'data-th':'Defendant'}).text
		return defendant
	except AttributeError:
		return None

def get_case_number(content):
	try:
		case_num = content.find('td', {'data-th':'Case Number'}).text
		return case_num
	except AttributeError:
		return None

def get_filed(content):
	try:
		filed = content.find('td', {'data-th':'Filed'}).text
		return filed
	except AttributeError:
		return None

def get_court(content):
	try:
		court =	content.find('td', {'data-th':'Court'}).text
		return court
	except AttributeError:
		return None

def get_presiding_judge(content):
	try:
		judge = content.find('td', {'data-th':'Presiding Judge'}).text
		return judge
	except AttributeError:
		return None

def get_judge0(content):
	try:
		judge0 = content.find('td', {'data-th':'0 Judge'}).text
		return judge0
	except AttributeError:
		return None
		
def get_judge1(content):
	try:
		judge1 = content.find('td', {'data-th':'1 Judge'}).text
		return judge1
	except AttributeError:
		return None

def get_nature_of_suit(content):
	try:
		nature_of_suit = content.find('td', {'data-th':'Nature of Suit'}).text
		return nature_of_suit
	except AttributeError:
		return None

def get_cause_of_action(content):
	try:
		cause_of_action  = content.find('td', {'data-th':'Cause of Action'}).text
		return cause_of_action
	except AttributeError:
		return None

def get_jury_demanded_by(content):
	try:
		jury_demanded_by =  content.find('td', {'data-th':'Jury Demanded By'}).text
		return jury_demanded_by
	except AttributeError:
		return None












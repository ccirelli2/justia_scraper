import os

def get_password(choice):
	if choice == 'mysql':
		os.chdir(r'/home/ccirelli2/Desktop/password')
		psswd = open('mysql.txt').read()
		return psswd


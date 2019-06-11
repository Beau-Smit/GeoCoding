'''
Beau Smit
Date:

Notes:

'''

from time import process_time, asctime
start_time = process_time()

import pd_rds
import pandas as pd
import numpy as np
import os
import re
from bs4 import BeautifulSoup
import urllib.request as url

def main():
	print('Started')

	addressD3 = r"https://en.wikipedia.org/wiki/List_of_NCAA_Division_III_institutions"
	webpage = url.urlopen(addressD3)

	soup = BeautifulSoup(webpage.read(), "lxml")
	# print(soup.prettify())
	big_table = soup.find('tbody')
	header = big_table.find('tr')
	
	header = [col.string.strip() for col in header.children]
	header[:] = [item for item in header if item != '']

	row_list = []
	for tag in big_table.find('tr').find_all_next('tr'):
		if tag.find('th').a == None:
			break
		school_name = tag.find('th').a.string.strip()
		# for item in tag.find_all('td'):
		# 	print(item)
		nickname = tag.find('td').string.strip()
		city = tag.find('td').find_next('td').a.string.strip()
		state = tag.find('td').find_next('td').find_next('td').a.string.strip()
		conference = tag.find('td').find_next('td').find_next('td').find_next('td').a.string.strip()
		tup = (school_name, nickname, city, state, conference)
		row_list.append(tup)

	df = pd.DataFrame(row_list, columns = header)
	# pd_rds.pd_to_rds(df, "D3_schools.Rds")

	
	print('\nFinished\nRun time: ' + str(process_time() - start_time) + ' sec')
	print(asctime())

main()


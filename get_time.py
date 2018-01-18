'''Changelog 1/18/2018: 
	This program now does the job of the initial parser file as well,
	and supplies get_relevant_csv.py with the necessary list of 
	files according to the schedules present in the Bi-Co Blue Bus Schedule'''

#Imports CSV writer
import csv

#BeautifulSoup for HTML reading
from bs4 import BeautifulSoup

#URLLib to store a webpage for BeautifulSoup to read
import urllib2

#The following function parses the latest blue bus schedules into CSV files based on the day of the week.
def get_time():

	#Link to the bus page for use by URL Lib
	bus_page = 'http://www.brynmawr.edu/transportation/bico.shtml'

	#Load page as a urllib object, this makes the page readable by beautifulsoup
	page = urllib2.urlopen(bus_page)

	#Using HTML5Lib parser with BeautifulSoup to open the Bi-Co Blue Bus page
	soup = BeautifulSoup(page, 'html5lib')

	#Initiates a list of soup tables in the page
	tables = soup.find_all('table')

	#This list will contain the filenames of each day.
	day_list = []

	#Iterates through every soup table
	for table in tables:

		#This parses the table headers
		headers = [header.text.encode('utf8') for header in table.find_all('th')]
		'''The first element of the table headers is always the day.
		   We will use the day's name as the name of the CSV file'''
		filename = headers.pop(0) + '.csv'

		#This gets rid of spaces to make every filename uniform
		filename = filename.replace(' ', '')
		day_list.append(filename)

		#The following two if blocks get rid of newlines and spaces in the schedule headers
		#Sample output row: ['LeaveBrynMawr', 'ArriveHaverford', 'LeaveHaverford', 'ArriveBrynMawr']
		for index, value in enumerate(headers):
			headers[index] = value.replace('\n', '')
		for index, value in enumerate(headers):
			headers[index] = value.replace(' ', '')
		#print headers

		#initiate list for each row in each day's soup table
		rows = []
		'''"tr" is the row in the table
		and "td" is each element in each row'''
		for row in table.find_all('tr'):
			rows.append([val.text.encode('utf8') 
				for val in row.find_all('td')])

		'''This deletes empty lists generated at the start of every day's rows.
		This results from parsing the web page and so is unavoidable.'''
		rows = [row for row in rows if row != []]

		'''This writes every header and rows for an individual day
		in the file labeled with that day's name.'''
		with open(filename, 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(headers)
			writer.writerows(row for row in rows if row)
	return day_list

#Call function when the file is run.
if __name__ == '__main__':
	print get_time()
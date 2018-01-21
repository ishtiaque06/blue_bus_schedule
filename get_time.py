
#import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
import os.path

"""
Function parses through the Blue_Bus website and retrives all Bus times in a CSV file
"""
def get_time():
    #specify the url
    bus_page = 'http://www.brynmawr.edu/transportation/bico.shtml'

    #query website and return the html

    page = urllib2.urlopen(bus_page)

    #parse the html using BeautifulSoup as a string
    soup = BeautifulSoup(page, 'html5lib') 
    
    tables= soup.find_all('table') #finds all the tables with bus times

    subdir = "csv_schedules"
    try:
            os.mkdir(subdir)
    except:
            pass
    
    #This makes the new file which has all the csv times
    filename = os.path.join(subdir, "bluebus_schedules.csv")
    create_file = open(filename, 'w')
    create_file.close()

    #Iterates through every soup tables
    for table in tables:

            #This parses the table headers
            headers = [header.text.encode('utf8') for header in table.find_all('th')]
            '''The first element of the table headers is always the day.
               We will use the day's name as the name of the CSV file'''
            day = headers.pop(0)

            #This gets rid of spaces to make every filename uniform
            day = day.replace(' ', '')

            #The following two if blocks get rid of newlines and the above character in the headers
            for index, value in enumerate(headers):
                    headers[index] = value.replace(' ', '')
            for index, value in enumerate(headers):
                    headers[index] = value.replace('\n', '')

            #initiate list for each row in each day's soup table
            rows = []
            '''"tr" is the row in the table
            and "td" is each element in each row'''
            for row in table.find_all('tr'):
                    rows.append([val.text.encode('utf8') 
                            for val in row.find_all('td')])
                    #print rows

            '''This deletes empty lists generated at the start of every day's rows.
            This results from parsing the web page and so is unavoidable.'''
            rows = [row for row in rows if row != []]
            
            #This appends each day's name, the table headers and the times in one csv file to be accessed later.
            with open(filename, 'a') as f:
                    f.write(day + '\n')
                    writer = csv.writer(f)
                    writer.writerow(headers)
                    writer.writerows(row for row in rows if row)

#Call function when the file is run.
if __name__ == '__main__':
	get_time()

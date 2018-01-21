
# coding: utf-8

# In[ ]:

#import libraries
import urllib2
from bs4 import BeautifulSoup
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
    soup = BeautifulSoup(page, 'lxml') 
    
    tables= soup.find_all('table') #finds all the tables with bus times
    
    #The following block prepares a file to write in the csv subdirectory
    subdir = "csv_schedules"
    try:
        os.mkdir(subdir)
    except:
        pass

    f = open(os.path.join(subdir, 'bluebus_schedules.csv'),'w')
    
    #The following block writes tables down in CSV form.
    for table in tables:
        for row in table.find_all("tr"):
            row = row.get_text(", ", strip=True) # removes white spaces and tabs between rows in text

            row = row.encode('ascii', 'ignore') # removes symbols in Unicode and keeps strings
            row =  ("".join(row.split()))  #removes all whitespaces before, after and inbetween strings
            f.write(row+"\n")
            
    f.close()

if __name__ == '__main__':
    get_time()


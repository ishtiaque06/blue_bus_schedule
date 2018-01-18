'''Changelog 1/18/2018:
    The csv_parser file is not going to be used anymore. This is because get_time 
    will now return a list of days that is compatible with the code below
    in the form ['Monday.csv', 'Tuesday.csv', 'Wednesday.csv', 'Thursday.csv',
     'Friday.csv', 'SaturdayDaytime.csv', 'SaturdayNight.csv', 'Sunday.csv']'''

from get_csv_data import get_data

from get_time import get_time

import datetime, timestring

"""
Function retrieves the day's relevant csv file and returns a list of dictionaries of time
"""
def relevant_csv():
    csv_list = get_time() #makes list of csvs parsed from the BlueBus Website
    today = (datetime.datetime.now()).strftime('%A')  #gives the name of the day
    time_now =  datetime.datetime.now()
    
    """
    Get relevant day's csv
    """
    for csv in csv_list:
        if today in csv:
            relevant_csv = csv
            
        #since there are 2 different CSVs for Saturday: Daytime and Nighttime
        elif (today == "Saturday") and ("Daytime" in csv) and (time_now < timestring.Date('4:45PM')) : 
                relevant_csv = csv
        
        elif (today == "Saturday") and ("Night" in csv) and (time_now > timestring.Date('4:45PM')):
            relevant_csv = csv
                              
    time_dict_list = get_data(relevant_csv)  #a list of dictionaries with relevant time for the current day
    
    return time_dict_list


if __name__ == '__main__':
    relevant_csv()


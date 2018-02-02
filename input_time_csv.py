from csv_parser import parser
from get_csv_data import get_data

import datetime

"""
Function takes a user's input time, date and gives relevant
bus times as a list of dictionaries.

"""
def input_time_function(string):
    string = string.split(",")
    csv_list = parser() #list of parsed csvs from BlueBus 
    time_now =  datetime.datetime.now()
    day_selected = string[1]
    relevant_csv = ""
    for csv in csv_list:
        if day_selected in csv:
            relevant_csv = csv
            
        #since there are 2 different CSVs for Saturday: Daytime and Nighttime
        elif (day_selected == "Saturday") and ("Daytime" in csv) and (time_now < timestring.Date('4:45PM')):
            relevant_csv = csv
            
        elif (day_selected == "Saturday") and ("Night" in csv) and (time_now > timestring.Date('4:45PM')):
            relevant_csv = csv
    timeDict = get_data(relevant_csv)
    
    return timeDict


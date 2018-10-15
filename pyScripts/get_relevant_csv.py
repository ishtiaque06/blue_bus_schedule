from csv_parser import parser
import format_times
from get_csv_data import get_data

import datetime, timestring

"""
Function retrieves the day's relevant csv file and returns a list of dictionaries of time
"""
def relevant_csv():
    today = (datetime.datetime.now()).strftime('%A')  #gives the name of the day
    time_now =  datetime.datetime.now()
    
    """
    Get relevant day's csv
    """
    if today == "Saturday":
        if time_now > timestring.Date('4:45PM'):
            day = "SaturdayNight"
        else: 
            day = "SaturdayDaytime"
    else:
        day = today
    filename = day + ".csv"
                              
    time_dict_list = get_data(filename)  #a list of dictionaries with relevant time for the current day

    return time_dict_list


if __name__ == '__main__':
    relevant_csv()


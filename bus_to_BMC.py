from get_relevant_csv import relevant_csv

import datetime
import calendar, timestring

"""
Function gives the time for the next bus to Bryn Mawr
"""
def bus_to_BMC():
    """
    Gets relevant bus times according to the current time
    """
    time_dict_list = relevant_csv()
    today = (datetime.datetime.now()).strftime('%A')
    next_buses = "Bus from Haverford:\n"
   
    for time_dict in  time_dict_list:
        time_now =  datetime.datetime.now()  #current time
        time_in_2hrs = datetime.datetime.now() + datetime.timedelta(hours=2.0) #the point after the next 3 buses
        
        bus_time = str(timestring.Date(time_dict['LeaveHaverford'])) #formats to today's time as a string
        bus_time = datetime.datetime.strptime(bus_time, '%Y-%m-%d %H:%M:%S') #converts the time string into a datetime object for comparison

        if time_now <= bus_time and time_in_2hrs >= bus_time:
            next_buses += str(time_dict['LeaveHaverford']) + "\n"
    
    if next_buses != "":
        return next_buses
    
    else:
        return "Sorry! There are no buses at this time. Please check back later!"

if __name__ == '__main__':
    bus_to_BMC()

from input_time_csv import input_time_function

import datetime
import calendar, timestring

"""
Gets relevant bus times to BMC according to a user's input time
in a string in the format "__:__AM/PM,<weekday>"
"""
def input_bus_to_BMC(string):
    
    time_dict_list = input_time_function(string) 
    
    input_time = str(timestring.Date((string.split(","))[0]))
    input_time = datetime.datetime.strptime(input_time, '%Y-%m-%d %H:%M:%S')
    
    next_buses = "Buses to Bryn Mawr before and after %s:\n"%(string)
   
    for time_dict in time_dict_list:
        time_before_2hrs = input_time - datetime.timedelta(hours=1.5) #the point before the next 3 buses
        time_in_2hrs = input_time + datetime.timedelta(hours=1.5) #the point after the next 3 buses
        
        bus_time = str(timestring.Date(time_dict['LeaveHaverford'])) #formats to today's time as a string
        bus_time = datetime.datetime.strptime(bus_time, '%Y-%m-%d %H:%M:%S') #converts the time string into a datetime object for comparison

        if time_before_2hrs <= bus_time and time_in_2hrs >= bus_time:
            next_buses += str(time_dict['LeaveHaverford']) + "\n"
            
    
    if next_buses != "":
        return next_buses
    
    else:
        return "Sorry! There are no buses at this time. Please check back later!"

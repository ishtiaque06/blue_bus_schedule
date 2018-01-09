"""
Takes a csv filename and returns data as a list of dictionaries
"""
def get_data(filename):
    f = open(filename, "r")
    line = f.readline() #reads line in the file
    location = line.strip().split(",")  # gets the location, either leaving or arriving HC or BMC
    
    data = [] 

    for line in f:
        bus_times = line.strip().split(",") #gives a list of time from each row
        
        """
        Checks to ensure that data fields are uniform
        """
        if (len(bus_times) == len(location)): #ensures that the data fields are uniform
            row = {}
            for exact_location in range(len(bus_times)):
                row[location[exact_location]] = bus_times[exact_location]
                
            data.append(row)
        
        else:
            row = {}

            for exact_location in range(len(bus_times)):
                row[location[exact_location]] = bus_times[exact_location]
            
            data.append(row)
            
            
            
    f.close()
    
    return data


def parser():
    initial = open('bluebus_schedules.csv', 'r')
    csv_list = []
    for line in initial:
        if ',' not in line:
            filename = line[:-1] + '.csv'
            new_file = open(filename, 'w')
            new_file.close()
            csv_list.append(filename)
        else:
            new_file = open(filename, 'a')
            new_file.write(line[:-1] + "\n")
            new_file.close()
    initial.seek(0)

    initial.close()
    
    return csv_list


import datetime
import calendar, timestring
"""
Function gives the time for the next bus, prompted the destination, assuming it is either from Haverford 
or BrynMawr to either locations
"""
def next_bus():
    destination = raw_input("Where are you going? Bryn Mawr or Haverford:  ")
    csv_list = parser() #makes list of csvs parsed from the BlueBus Website
     
    today = (datetime.datetime.now()).strftime('%A')  #gives the name of the day   
    print today
    
    for csv in csv_list:
        if today in csv:
            relevant_csv = csv
    
    """
    Get relevant bus times according to the current time
    """
    time_dict_list = get_data(relevant_csv)  #a list of dictionaries with relevant time for the current day
    for time_dict in  time_dict_list:
        time_now =  datetime.datetime.now()  #time now
        time_in_2hrs = datetime.datetime.now() + datetime.timedelta(hours=2.75)      
        
        if destination in ["Haverford", "HC","haverford"]:
            bus_time = time_dict['LeaveBrynMawr']
            bus_time = str(timestring.Date(bus_time)) #formats to today's time as a string
            bus_time = datetime.datetime.strptime(bus_time, '%Y-%m-%d %H:%M:%S') #converts the time string into a datetime object for comparison
            
            if time_now <= bus_time and time_in_2hrs >= bus_time:
                print time_dict['LeaveBrynMawr'] + " -> " +str(time_dict['ArriveHaverford'])
            
        elif destination in ["BrynMawr", "BMC", "brynmawr", "bryn mawr"]:
            bus_time = time_dict['LeaveHaverford']
            bus_time = str(timestring.Date(bus_time)) 
            bus_time = datetime.datetime.strptime(bus_time, '%Y-%m-%d %H:%M:%S') #converts the time string into a datetime object for comparison
            
            if time_now <= bus_time and time_in_2hrs >= bus_time:
                print time_dict['LeaveHaverford'] + " -> " +str(time_dict['ArriveHaverford'])
                
        else:
            
            print str("Error: \nPlease input correct destination")
            break
next_bus()
            
         


    
    


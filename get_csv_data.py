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
#This file parses a csv file which has multiple titles without commas followed by
#multiple lines of comma-separated values and outputs them into separate csv files

import os.path
import csv

def parser():
    current_dir = os.path.dirname(__file__)
    #Open the input file as read-only
    initial = open(os.path.join(current_dir, 
        'csv_schedules', 'bluebus_schedules.csv'), 
    'r')
    csv_list = []
    #loops through the input file
    for line in initial:
        #This block fixes the headings for Saturday night and Sunday.
        if line == "BrynMawrtoHaverford,HaverfordtoBrynMawr\n":
            line = "LeaveBrynMawr,LeaveHaverford\n"
        if line == "LeavesBMC,LeavesSuburbanSquare,LeavesHCSouthLotBusStop,LeavesStokes,LeavesSuburbanSquare\n":
            line = "LeaveBrynMawr,LeaveSuburbanSquare,LeaveHCSouthLotBusStop,LeaveHaverford,LeaveSuburbanSquare\n"
            
        if ',' not in line: #If the line doesn't contain a comma, it's a title
            filename = line[:-1] + '.csv' #the title is used to make the filename.csv
            new_file = open((os.path.join(current_dir,
            'csv_schedules/', filename)), 'w') #new file opened to write to
            new_file.close() #new file is closed
            csv_list.append(filename)

        else: #Else, the csv line belongs to the title that was found in a previous line
            new_file = open((os.path.join(current_dir,
            'csv_schedules/', filename)), 'a') #appends the csv to the new file
            new_file.write(line[:-1] + '\n')
            new_file.close()

    initial.close()

    return csv_list


if __name__ == '__main__':
    parser()


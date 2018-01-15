#This file parses a csv file which has multiple titles without commas followed by
#multiple lines of comma-separated values and outputs them into separate csv files

def parser():
    #Open the input file as read-only
    initial = open('bluebus_schedules.csv', 'r')
    csv_list = []
    #loops through the input file
    for line in initial:

        if ',' not in line: #If the line doesn't contain a comma, it's a title
            filename = line[:-1] + '.csv' #the title is used to make the filename.csv
            new_file = open(filename, 'w') #new file opened to write to
            new_file.close() #new file is closed
            csv_list.append(filename)

        else: #Else, the csv line belongs to the title that was found in a previous line
            new_file = open(filename, 'a') #appends the csv to the new file
            new_file.write(line[:-1] + "\n")
            new_file.close()

    initial.close()
    """
    
    #Makes all the CSV headers uniform except SaturdayDaytime.csv
    
    for csv in csv_list:
        with open(csv, "r") as f:
            lines = f.readlines()        
            column_headers = (lines[0].split(","))
            new_header = ""
            
            for header in column_headers:
                header = header.replace(" ", "")
                
                if header == "BrynMawrtoHaverford":
                    header = "LeaveBrynMawr"
                    new_header += header + ","

                elif header == "HaverfordtoBrynMawr":
                    header = "LeaveHaverford"
                    new_header += header + ","
                    
            if new_header != "":
                lines[0] = new_header
                
                with open(csv,"w") as new_csv:
                    for line in lines:
                        new_csv.write(line)
    """                   
    return csv_list


if __name__ == '__main__':
    parser()


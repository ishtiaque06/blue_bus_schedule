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
    
    return csv_list


if __name__ == '__main__':
    parser()

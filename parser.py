initial = open('bluebus_schedules.csv', 'r')
for line in initial:
    if ',' not in line:
        filename = line[:-1] + '.csv'
        new_file = open(filename, 'w')
        new_file.close()
    else:
        new_file = open(filename, 'a')
        new_file.write(line[:-1] + "\n")
        new_file.close()
initial.seek(0)

initial.close()

'''
	Each CSV for each day has times that belong to the next day
	This file goes through all those files and moves these times
	to the appropriate next day's file. 
'''
import os, sys

current_dir = os.path.dirname(__file__)
csv_dir = os.path.join(current_dir, 'csv_schedules')

'''
	Some AM times are shown as PM times and this fixes that issue.
'''
def fix_Monday():
	lines = []
	with open(os.path.join(csv_dir,'Monday.csv')) as file:
		lines = file.readlines()
	lines[-1] = lines[-1].replace('P', 'A')
	with open(os.path.join(csv_dir,'Monday.csv'), 'w') as file:
		file.writelines(lines)
	return 0

def fix_Monday_post():
	lines = []
	with open(os.path.join(csv_dir,'Monday.csv')) as file:
		lines = file.readlines()
	line_to_modify = lines[1].split(',')
	line_to_modify.insert(1,'')
	line_to_modify[2]='12:15AM'
	line_to_modify.append('\n')
	lines[1] = ','.join(line_to_modify)
	with open(os.path.join(csv_dir,'Monday.csv'), 'w') as file:
		file.writelines(lines)
	return 0

'''
	The last-column times from Friday are not formatted according
	to Saturday's columns. This takes care of that.
'''
def fix_SaturdayDayTime():
	with open(os.path.join(csv_dir,'SaturdayDaytime.csv')) as file:
		lines = file.readlines()
	i=1
	while i<5:
		line_to_modify=lines[i]
		line_to_modify=line_to_modify.split(',')
		line_to_modify.insert(2, '')
		if i==1:
			line_to_modify[0] = '12:00 AM'
		lines[i]=','.join(line_to_modify)
		i+=1
	with open(os.path.join(csv_dir,'SaturdayDaytime.csv'), 'w') as file:
		file.writelines(lines)
	return 0

'''
	This transfers the last few elements of each day that actually fall
	into the next day into the next day's CSV file.
'''
def transfer_times(today, tomorrow):
	with open(os.path.join(csv_dir,(today+'.csv'))) as file1:
		lines_today = file1.readlines()
	with open(os.path.join(csv_dir,(tomorrow+'.csv'))) as file2:
		lines = file2.readlines()
		lines_tomorrow = lines[1:]
		title = lines[0]
	i = len(lines_today) - 1
	while i >= 0:
		if 'AM' in lines_today[i]:
			if 'PM' in lines_today[i]:
				list_times = lines_today[i].split(',')
				j=0
				while j<len(list_times):
					if 'PM' in list_times[j]:
						list_times[j] = '12:00 AM'
					j+=1
				lines_today[i]=','.join(list_times)

			lines_tomorrow.insert(0, lines_today[i])
			lines_today.pop()
			i-=1
		else:
			break
	lines_tomorrow.insert(0, title)
	with open(os.path.join(csv_dir,(tomorrow+'.csv')), 'w') as file:
		file.writelines(lines_tomorrow)
	with open(os.path.join(csv_dir,(today+'.csv')),'w') as file2:
		file2.writelines(lines_today)
	return 0

'''
	This starts off with the list of days available and transfers the times into
	appropriate days.
'''
def insert_times_to_next_day():
	days = ['Friday','SaturdayDaytime','SaturdayNight','Sunday','Monday','Tuesday',
			'Wednesday','Thursday']
	i=0
	while i<len(days):
		tomorrow=''
		if days[i]==days[-1]:
			tomorrow=days[0]
		else:
			tomorrow=days[i+1]
		transfer_times(days[i], tomorrow)
		i+=1
	return 0

if __name__=="__main__":
	fix_Monday()
	insert_times_to_next_day()
	fix_SaturdayDayTime()
	fix_Monday_post()
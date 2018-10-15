#import libraries needed to show the page
from flask import Flask, render_template, jsonify, request
import json
import os, sys

current_dir = os.path.dirname(__file__)
csv_dir = os.path.join(current_dir, 'csv_schedules')

#load bus schedule scripts
script_dir = os.path.join(current_dir, 'pyScripts')

sys.path.append(script_dir)
sys.path.append(csv_dir)

from bus_to_HC import *
from bus_to_BMC import *
from input_bus_to_HC import *
from input_bus_to_BMC import *

import format_times
import csv_parser

csv_parser.parser()
format_times.fix_Monday()
format_times.insert_times_to_next_day()
format_times.fix_SaturdayDayTime()

#initialize flask instance
app = Flask(__name__)

#Route Flask to start the index file
@app.route('/')
def index():
	return render_template('index.html')

#This sends next bus times from Bryn Mawr to Haverford
@app.route('/to_Haverford')
def to_Haverford():
	times = bus_to_HC()
	return json.dumps(times)

#This sends the next bus times from Haverford to Bryn Mawr
@app.route('/to_Bryn_Mawr')
def to_Bryn_Mawr():
	times = bus_to_BMC()
	return json.dumps(times)

'''
The following two functions' dumps for some reason get treated as
plain texts including quotes and '\n' characters by the 
AJAX POST request so after the js file receives the response
further string trimming has to be done to make it look good for 
the website.
'''
#This sends the bus times based on a certain time of the week from HC to BMC
@app.route('/time_to_Haverford', methods = ["POST"])
def time_to_Haverford():
	if request.method == 'POST':
		time = request.data.decode('utf-8')
		result = input_bus_to_HC(time)
		return json.dumps(result)

#This sends the bus times based on a certain time of the week from HC to BMC
@app.route('/time_to_BrynMawr', methods = ["POST"])
def time_to_BrynMawr():
	if request.method == 'POST':
		time = request.data.decode('utf-8')
		result = input_bus_to_BMC(time)
		return json.dumps(result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#call run function to start the server
if __name__ == '__main__':
	app.run(debug=False)

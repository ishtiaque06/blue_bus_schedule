#import libraries needed to show the page
from flask import Flask, render_template, jsonify, request
import json
#load bus schedule scripts
from bus_to_HC import *
from bus_to_BMC import *
from input_bus_to_HC import *
from input_bus_to_BMC import *

#initialize flask instance
app = Flask(__name__)

#Route Flask to start the index file
@app.route('/')
def index():
	return render_template('index.html')

#This sends next bus times from Bryn Mawr to Haverford
@app.route('/to_Haverford')
def to_Haverford():
	print "Debugging at Haverford"
	times = bus_to_HC()
	print times
	return json.dumps(times)

#This sends the next bus times from Haverford to Bryn Mawr
@app.route('/to_Bryn_Mawr')
def to_Bryn_Mawr():
	print "Debugging at Bryn Mawr"
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
	print "Debugging future time from Bryn Mawr to Haverford"
	if request.method == 'POST':
		print "Here I am with POST!"
		time = request.data.replace('"', '')
		result = input_bus_to_HC(time)
		return json.dumps(result)

#This sends the bus times based on a certain time of the week from HC to BMC
@app.route('/time_to_BrynMawr', methods = ["POST"])
def time_to_BrynMawr():
	print "Debugging future time from Haverford to Bryn Mawr"
	if request.method == 'POST':
		print "Here I am with POST!"
		time = request.data.replace('"', '')
		result = input_bus_to_BMC(time)
		return json.dumps(result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#call run function to start the server
if __name__ == '__main__':
	app.run(debug=True)

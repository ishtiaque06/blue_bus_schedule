#import libraries needed to show the page
from flask import Flask, render_template, jsonify, request
import json
#load bus schedule scripts
from bus_to_HC import *
from bus_to_BMC import *

#initialize flask instance
app = Flask(__name__)

#Route Flask to start the index file
@app.route('/')
def index():
	return render_template('index.html')

#Pushes bus times to site
@app.route('/to_Haverford')
def to_Haverford():
	print "Debugging at Haverford"
	times = bus_to_HC()
	
	return json.dumps(times)

@app.route('/to_Bryn_Mawr')
def to_Bryn_Mawr():
	print "Debugging at Bryn Mawr"
	times = bus_to_BMC()
	
	return json.dumps(times)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#call run function to start the server
if __name__ == '__main__':
	app.run(debug=True)

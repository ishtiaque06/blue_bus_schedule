#import libraries needed to show the page
from flask import Flask, render_template

#initialize flask instance
launch = Flask(__name__)

#Route Flask to start the index file
@launch.route('/')
def start():
	return render_template('index.html')

#call run function to start the server
if __name__ == '__main__':
	launch.run(debug=True)
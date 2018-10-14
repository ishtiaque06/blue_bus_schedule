# Next Blue Bus

Welcome to the source code for Next Blue Bus: A single-page web application 
that tells you when to rush to the bus stops at Haverford or Bryn Mawr! 

### Goals

There's a good volume of students who use the college shuttle bus between 
Haverford and Bryn Mawr (also known as the Blue Bus). 

The schedule for this bus service is posted online as a table, but its formatting
is, to put simply, an annoying nightmare. 
* Going to the [Blue Bus page](https://www.brynmawr.edu/transportation/blue-bus-bi-co) 
	with all the departure times, you will find that it takes a good amount of time 
	to scroll through the whole table to find that one cell that tells you the time you 
	wish to know.

So, we decided to make things simpler by making this web app that does the scrolling
for us and gives us the time(s) that the next bus leaves at. 

### Features

This web app has two features:
* If you want to know the immediate next time when buses leave from Haverford/Bryn Mawr,
	you can get that detail in a press of a button.
* If you feel like planning a trip to your destination college ahead of time, you can select
	your departure times and get a list of departure times +/- 2 hours around that time you
	selected.

### Dependencies

* This Python3-based web app is based on [Flask, a Python microframework](http://flask.pocoo.org).
* For scraping through the Blue Bus page, we used [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/),
	which is indeed a beautiful Python library that helps programmers like us scrape through HTML pages
	and extract meaningful data out of them (in this context, bus times on set days between 
	Haverford and Bryn Mawr.)
* Finally, we used jQuery on the webpage to get the correct times from the server to 
	display to the users.

### For development:

1. Clone the repository: `git clone https://github.com/ishtiaque06/next_blue_bus`
2. cd into the directory and install dependencies: `pip install -r requirements.txt`
3. Run the development server: `python3 launch_server.py`

### Feedback

We're open to feedback! You can get in touch with us via E-mail:

* [Ken](mailto:kruto@haverford.edu)
* [Ahmed](mailto:ahmedishti27@gmail.com)
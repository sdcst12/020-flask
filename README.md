## SDSS Computing Studies Python Assignment
### Flask!

Objectives:
* To create a basic flask server
* To create an endpoint for an API
* Add file data to a sqlite database

A lot of the behind the scenes work on the Internet is handled by API requests and access to things that are not normally accessible to the WWW side.  One way of accessing server side data is the use of an API endpoint, and Flask is a python module that allows us to create a flask server.

This is an example of a server side application, where all of the programming happens in a way that the user can't see any of the source code. This is different from the way that html files work, where all of the javascript is publicly viewable in your browser.

We set up a Flask server in a way that is different from setting up an html server, but the end result can look largely the same.

You will need to install 2 modules today:
flask : py -m pip install flask
    This allows you to run a flask server
flask-cors : py -m pip install flask-cors
    This allows your flask server to serve cross domain requests

We will only be looking at the first part of the flaskServer.py file today, and serve a basic api endpoint that is accessible from within a web browser.  Later, more advanced applications can deny access to web browsers and only serve data to applications or webforms.




##### Assignment
Create an API endpoint that serves GET requests to its root endpoint with a random quote, joke, fact or other piece of text information.  Your application will retrieve the contents of an sqlite database and then choose one random entry to display.
You have some choices:
    * retrieve all of the entries into memory and then choose 1 at random
    * retrieve all of the entry id's and choose one at random, and then retrieve the entry that corresponds to that id

You will also need the following programs:
1. A program that lets you retrieve all of the entries and view them (for server admin maintenance)
2. A program that will read a text file for new entries to the database, and enter them if they do not already exist.  Remember to search for your entry first before you add it to ensure that there are no duplicates
3. The flask server program

Extra:
Make an endpoint that creates a "joke/quote/fact of the day" where it will only serve the same joke all day long.  You could make use of the time module and the time.time() command (which retrieves epoch time) but there other ways of doing this.



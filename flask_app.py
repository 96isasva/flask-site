"""Author: Isak Svalling, 2015"""

from flask import Flask, render_template, flash

app = Flask(__name__)


@app.route('/')
@app.route('/startpage/')

def startpage():
	flash("This site uses cookies")
	return render_template("startpage.html")

if (__name__) == "__main__":
	app.run()

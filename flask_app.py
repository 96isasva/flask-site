"""Author: Isak Svalling, 2015"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/startpage/')

def startpage():
	return render_template("startpage.html")

if (__name__) == "__main__":
	app.run()

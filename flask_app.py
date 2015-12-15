"""Author: Isak Svalling, 2015"""

from flask import Flask, render_template, flash
from flask_wtf import Form
from wtforms import Form, StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
import sqlite3 as lite

DATABASE = 'flask-site/database/testdb.db'
DEBUG = True
SECRET_KEY = "1337"
USERNAME = "admin"
PASSWORD = "default"

app = Flask(__name__)

def initdb():
	try:
		con = lite.connect(app config["DATABASE"])
		cur.con.cursor()
		cur.execute("""CREATE TABLE users(
		uid INTEGER PRIMARY KEY NOT NULL,
		username VARCHAR(10),
		email VARCHAR(30),
		password VARCHAR(10)
		role VARCHAR(10)
		con.commit()
		con.close()
		con.close()

		)""")
	except Exception  as e:
		return e


@app.route('/')
@app.route('/startpage/')


def startpage():
	flash("This site uses cookies")
	return render_template("startpage.html")



@app.route('/register/', methods = ['GET', 'POST'])
def register():
	try:
		form = RegistrationForm(request.form)
	except Exception as e:
		raise

if (__name__) == "__main__":
	app.run()

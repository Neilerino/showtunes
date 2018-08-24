from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/home')
def home():
	return render_template("home.html")

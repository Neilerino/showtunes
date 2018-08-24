from flask import render_template, flash, redirect
from app import app

@app.route('/home')
def home():
	return render_template("home.html")

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.forms import LoginForm, RegisterForm
from app import app, db


@app.route('/')
@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect('/home')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('home'))
	return render_template('login.html', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for(home))
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Thank you for registering')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/user')
def user():
	return render_template('user.html', title=current_user.username)
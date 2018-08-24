from app import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}'.format(self.username)


class Set(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Set {}'.format(self.name)

class Song(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	number = db.Column(db.Integer, index=True, unique=True)
	name = db.Column(db.String(64), index=True, unique=True)
	artist = db.Column(db.String(64), index=True)
	album = db.Column(db.String(64), index=True)
	set_id = db.Column(db.Integer, db.ForeignKey('set.id'))


	def __repr__(self):
		return '<Song {}'.format(self.name)

class Sheet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	path = db.Column(db.String(128), unique=True)
	song_id = db.Column(db.Integer, db.ForeignKey('song.id')) 


class Session(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	start_time = db.Column(db.DateTime, default=datetime.utcnow)
	end_time = db.Column(db.DateTime)
	practice_time = db.Column(db.DateTime, index=True)
	song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
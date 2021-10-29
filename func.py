from flask import Blueprint, current_app, g, render_template, request

import sqlite3


message_bp = Blueprint('message', __name__, url_prefix='/message')

def get_message_db():
	# If there is no database called "message_db", create one
	if 'message_db' not in g:
		g.message_db = sqlite3.connect('message_db.sqlite')
	# Check if a table called "messages" exists in the database or not. If not, create one. 
	g.message_db.execute(
		'CREATE TABLE IF NOT EXISTS messages (ID integer, name varchar, message varchar);')

	return g.message_db

def insert_message(request):
	message = request.form['message']
	name = request.form['name']
	db = get_message_db()
	ID = db.execute('SELECT COUNT(*) FROM messages;').fetchone()[0]+1
	db.execute(
		'INSERT INTO messages (ID, name, message) VALUES (?, ?, ?);',
		(ID, name, message))
	db.commit()
	db.close()

def random_messages(n):
	db = get_message_db()
	entries = db.execute('SELECT name, message FROM messages ORDER BY RANDOM() LIMIT ?;', [n]).fetchall()
	db.close()
	return entries







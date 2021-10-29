from flask import Flask, render_template, request
from func import insert_message, random_messages

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def submit():
	if request.method == "GET":
		return render_template('submit.html')
	if request.method == "POST":
		insert_message(request=request)
		return render_template('submit.html', thanks = True)

# @app.route("/submit/", methods = ['POST', 'GET'])
# def submit():
# 	if request.method == "GET":
# 		return render_template('submit.html')
# 	if request.method == "POST":
# 		insert_message(request=request)
# 		return render_template('submit.html', thanks = True)

@app.route("/view/", methods = ['POST', 'GET'])
def view():
	entries = random_messages(5)
	return render_template("view.html", entries = entries)


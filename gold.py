from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "baloney"

@app.route("/")
def index():
	if "Gold" not in session:
		session["Gold"] = 100
	if "logger" not in session:
		session["logger"] = []
	if "count" not in session:
		session["count"] = 0
	if "gameOver" not in session:
		session["gameOver"] = "False"
	if session["count"] > 14:
		session["gameOver"] = "True"
	return render_template("indexGold.html", currency = session["Gold"], logger = session["logger"], gameOver= session["gameOver"])
	

@app.route("/process",methods=["post"])
def process():
	print(request.form)
	earned = 0
	if request.form["form"]=="farm":
		earned = random.randint(10,20)
		session["Gold"] += earned
	elif request.form["form"]=="cave":
		earned = random.randint(5,10)
		session["Gold"] += earned
	elif request.form["form"]=="house":
		earned = random.randint(2,5)
		session["Gold"] += earned
	elif request.form["form"]=="casino":
		earned = random.randint(0,50) * random.choice([1,-1])
		session["Gold"] += earned
	logger = ""
	if earned < 0:
		logger += "lost " + str(earned * -1) + " Gold in the " + request.form["form"]
	else: logger += "Earned " + str(earned) + " Gold in the " + request.form["form"]
	session["logger"].append(logger)
	session["count"] += 1
	print(session["count"])

	return redirect("/")

@app.route("/reset")
def reset():
	session.clear()
	return redirect("/")


if __name__=="__main__":
	app.run(debug=True)

# I just need to add this here for a bit! :D

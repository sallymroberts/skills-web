from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/application-form")
def index_page():
	first_name = request.args.get("firstname")
	last_name = request.args.get("lastname")
	salary_req = request.args.get("salary")

	thank_string = ["Thank you, %s, for applying to be a %s. Your minumum salary request is %s dollars."] 
	thank_string = thank_string % (first_name, last_name, salary_req)
	# Return this as a string
	return "<html><body>thank_string</body></html>"

	# Alternately, we could make this a Jinja template in `templates/`
	# and return that result of rendering this, like:
	#
	# return render_template("application.html", text=thank_string)

@app.route("/application")
def thank_page():
	return "On application page"

if __name__ == "__main__":
	app.run(debug=True)
	# app.run(debug=True)
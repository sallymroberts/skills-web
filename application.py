from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def start_app():
	return render_template('application-form.html')

@app.route("/application", methods=["POST"]) 
def index_page():
	first_name_py = request.form.get("firstname")
	job_title_py = request.form.get("jobtitle")
	salary_req_py = request.form.get("salary")
	
	# Return this as a string
	# return "<html><body>thank_string</body></html>"

	# Alternately, we could make this a Jinja template in `templates/`
	# and return that result of rendering this, like:
	#
	return render_template("confirmation.html", first_name = first_name_py, job_title = job_title_py, salary_req=salary_req_py)


if __name__ == "__main__":
	app.run(debug=True)
	# app.run(debug=True)
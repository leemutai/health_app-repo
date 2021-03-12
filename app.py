from flask import Flask
from flask import render_template
from flask import request

#creating instance of flask app
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/viewbooking", methods =["POST", "GET"])
def view_booking():
    if request.method =="POST":
        #get data from the form
        fullname = request.form["fullname"]
        email = request.form["email"]
        age = request.form["age"]
        #return  ("the details provided were {} {} {}".format(email, age, fullname) )
        return render_template("viewbooking.html",
                               fullname=fullname, age=age, email=email)

    else:
        return render_template("viewbooking.html")

@app.route("/bmi", methods=["POST", "GET"])
def calculate_bmi():
    if request.method == "POST":
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        bmi = weight/ (height * height)
        return render_template("homepage.html", bmi=bmi)

@app.route('/covid-guidelines')
def covid_guidelines():
    guidelines = ["wear face mask", "social distancing","sanitising"]
    return  render_template("guidelines.html", guidelines =guidelines)

if __name__ == "__main__":
app.run()
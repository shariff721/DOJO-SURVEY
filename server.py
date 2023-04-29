from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "riffdini"


@app.route('/')
def Survey():
    return render_template("index.html")


@app.route('/formprocess', methods = ["POST"])
def myForm():
    print(request.form)
    session["name"] = request.form["namein"]
    session["location"] = request.form["selectoptions"]
    session["language"] = request.form["codlanguage"]
    session["comments"] = request.form["commentsin"]
    return redirect('/results')


@app.route('/results')
def showResults():
    return render_template("results.html")


if __name__ == '__main__':
    app.run(debug=True, port = 5001)
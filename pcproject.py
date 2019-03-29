from flask import Flask, render_template, request

app = Flask("pcprojectApp")

@app.route("/")
def hello():
    return "Hello Clare & Paola"

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

app.run(debug=True)

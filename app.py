#!/usr/local/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/concept")
def concept():
   return render_template("concept.html")

@app.route("/process")
def process():
  return render_template("process.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/warning")
def warning():
  return render_template("warning.html")

if __name__ == "__main__":
  app.run(debug=True)
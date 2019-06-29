from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config[ 'DEBUG' ] = True

@app.route('/', methods=["Get"])
def index():
    return render_template("index.html")

@app.route('/', methods=["Get", "Post"])
def validation():
    


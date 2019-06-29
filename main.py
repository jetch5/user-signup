from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config[ 'DEBUG' ] = True

@app.route('/', methods=["Get"])
def index():
    return render_template("index.html")

@app.route('/', methods=["Get", "Post"])
def validation():
    username = request.form ["username"]
    username_error = ""

    if " " in username:
        username_error = "Spaces are not permitted"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Length is not valid"
    elif not username:
        username_error = "Username is required"
    else:
        pass 

    password = request.form["password"]
    password_error=""

    if not password:
        password_error = "Password is required"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password length is not valid"
    elif " " in password:
        password_error = "Spaces are not permitted"
    else:
        pass

    verify = request.form["verify"]
    verify_error = ""

    if verify != password:
        verify_error = "Does not match password"
    else:
        pass
    
    email = request.form["email"]
    email_error = ""

    if "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$" not in email:
        email_error = "Email is option, but this is not a valid email"
    elif len(email) < 3 or len(email) > 20:
        email_error = "Email length is not valid, please remove if you do not have a valid email."
    else:
        pass

    if not _error:
        return render_template("welcome.html", username=username)
    else:
        return render_template("index.html", _error = _error)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username=username)

app.run
    


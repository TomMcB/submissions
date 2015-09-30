from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/about")
def home():
    return """<center>
<h1>HELLO</h1>
<br>
<a href="http://localhost:8000/login">LOGIN</a>
</center>"""

@app.route("/login",methods=["GET","POST"])
def login():
    if (('n' not in session) or (session['n'] != 1)) and (request.method == "GET"):
        session['n'] = 0;
        return render_template("login.html")
    else:
        return redirect(url_for('secret'))

@app.route("/secret")
def secret():
    session['n'] == 1
    return render_template("secret.html")

@app.route("/out")
def out():
    session['n'] == 0
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.debug = True
    app.secret_key="hi"
    app.run(host="0.0.0.0",port=8000)
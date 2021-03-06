from flask import Flask, render_template, request, session, redirect, url_for
import authen2

app = Flask(__name__)

@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        session["login"]=False
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        button = request.form["button"]
        if button=="cancel":
            return render_template("login.html")
        if authen2.authen(username,password):
            session["login"] = True
            return redirect(url_for("secret"))
        else:
            error = "username and password are incorrect"
            return render_template("login.html",error=error)

@app.route("/secret")
def secret():
    if ("login" not in session) or session["login"] == False:
        return "<h1>You aren't logged in!!</h1>"
    else:
        return render_template("secret.html")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Don't store this on github"
    app.run(host="0.0.0.0", port=8000)    

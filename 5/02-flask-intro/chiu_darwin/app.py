from flask import Flask, render_template,request,session,redirect,url_for
import utils

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dancers")
def dancers():
    import random
    r = random.randrange(1,4)
    f = {'name':"Franklin Yu",
         'team':"ACA",
         'piece':"Tennis Court",
         'pic':"/static/fy.jpg"}

    b = {'name':"Bam Martin",
         'team':"GRV",
         'piece':"OOH KILL'EM",
         'pic':"/static/Bam.jpg"}

    m = {'name':"Markus Pe Benito",
         'team':"GRV",
         'piece':"Powerful",
         'pic':"/static/markus.png"}

    if r==1:
        return render_template("dancers.html",d=f)
    elif r==2:
        return render_template("dancers.html",d=b)
    else:
        return render_template("dancers.html",d=m)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        button = request.form['button']
        uname=request.form['username']
        pword=request.form['password']
        if button=="cancel":
            return render_template("login.html")
        # if we're here we should have
        # a username and password
        session['uname'] = uname
        session['pword'] = pword
        if utils.authenticate(uname,pword):
            return redirect(url_for("hidden"))
        else:
            session['uname']=''
            session['pword']=''
            return render_template("login.html",error="INVALID USERNAME OR PASSWORD")

@app.route("/hidden")
def hidden():
    if 'uname' and 'pword' not in session:
        return redirect(url_for("login"))
    elif utils.authenticate(session['uname'],session['pword']):

        return render_template("hidden.html")
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if 'uname' and 'pword' not in session:
        return redirect(url_for("login",error="YOU ARENT EVEN LOGGED IN!"))
    elif utils.authenticate(session['uname'],session['pword']):
        session['uname']=''
        session['pword']=''
        return render_template("logout.html")
    else:
        return redirect(url_for("login",error="YOU ARENT EVNE LOGGED IN!"))
        
    

if __name__ == "__main__":
    app.debug = True
    app.secret_key="hetoihrtjoir"
    app.run(host='0.0.0.0', port=8000)
    

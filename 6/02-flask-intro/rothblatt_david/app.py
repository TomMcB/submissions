from flask import Flask, render_template
from random import randrange


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/funny")
def funny():
    return render_template("funny.html")

@app.route("/cronut")
def cronut():
    return render_template("cronut.html")

@app.route("/madlibify")
def madlibify():
    adjs = ["RED","YELLOW","BLUE","SAD","HAPPY","BRAVE",\
        "FAT","HAIRY","GRUMPY","FLYING"]
    animals = ["DOG","CAT","LION","TIGER","BEAR","GIRAFFE"]
    verbs = ["WALK","TALK","PLAY","YELL","EAT","FIGHT"]
    d = {'adj': adjs[randrange(len(adjs))], 
    'animal': animals[randrange(len(animals))], 
    'verb': verbs[randrange(len(verbs))] }
    return render_template("madlib.html", d=d)

@app.route("/bondify")
@app.route("/bondify/")
@app.route("/bondify/<last>/<first>/")
@app.route("/bondify/<last>/<first>")
def bondify(last="", first=""):
    d = {"last": last, "first": first}
    jobs = ["Teacher", "Doctor", "Lawyer", "CEO", "Web Designer", "Dancer", \
            "Accountant", "Politician", "Special Agent", "Cop", "Firefighter", \
            "Athlete", "Actor", "Pilot", "Engineer"]
    d['job'] = jobs[randrange(len(jobs))]
    agent_id = randrange(100, 10000)

    return render_template("bond.html", d=d, agent_id = agent_id)
    

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)



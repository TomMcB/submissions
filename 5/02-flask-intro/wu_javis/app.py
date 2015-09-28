from flask import Flask, render_template

app = Flask(__name__)
@app.route("/fortune/<name>")
def fortune(name):
    import random
    holder=name
    l = ['your future looks bleak.','you will have an awesome day.',
         'do not leave your house today.','today will be a day of love',
         'have no worries. You are forever fortunate.', 
         'your life will forever be horrible.'] 
    r=random.randrange(1,len(l))
    return render_template("fortune.html",fortunes=l,chance = r,person=holder)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=8001)

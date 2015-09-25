from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    page = """<h1>Home Page</h1>
    <button><a href="/about">To the About Page!</a></button>
    <button><a href="/pictures">Free Pictures!</a></button>
    """
    return page

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pictures")
def picture():
    return render_template("pictures.html")
    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)

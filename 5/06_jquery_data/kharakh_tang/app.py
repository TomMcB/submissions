from flask import Flask, render_template
import time,json

app = Flask(__name___)

@app.route("/")
def index():
    return render_template("index.html")

    if __name__ == "__main__":
    app.debug =True
    app.run(host="0.0.0.0", port=8000)

                
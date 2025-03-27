from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/length")

def length():
    return render_template("length.html")

@app.route("/temperature")

def temperture():
    return render_template("temperature.html")

@app.route("/weight")

def length():
    return render_template("weight.html")

if __name__ == "__main__":
    app.run()
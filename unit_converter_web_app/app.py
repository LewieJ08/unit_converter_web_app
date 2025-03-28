from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/length", methods=["GET", "POST"])

def length():
    return render_template("length.html")

@app.route("/temperature", methods=["GET", "POST"])

def temperature():
    return render_template("temperature.html" , )

@app.route("/weight",methods=["GET", "POST"])

def weight():
    return render_template("weight.html")

if __name__ == "__main__":
    app.run(debug=True)
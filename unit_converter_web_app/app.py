from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/length", methods=["GET", "POST"])

def length():

    length_conversions = {
        "mm": 0.001,     
        "cm": 0.01,        
        "m": 1,          
        "km": 1000,    
        "in": 0.0254,     
        "ft": 0.3048,     
        "yd": 0.9144,   
        "mi": 1609.34,
     }
    
    if request.method == "POST":
        unit = float(request.form["length"])
        unit_from = request.form["unitFrom"]
        unit_to = request.form["unitTo"]

        print(f"Calculating conversion: {unit} {unit_from} to {unit_to}...")

        length_in_meters = unit * length_conversions[unit_from]
        converted_length = length_in_meters / length_conversions[unit_to]

        return render_template("length.html", result = converted_length, unit_to = unit_to)
    
    else:
        return render_template("length.html", result = None)
    
@app.route("/temperature", methods=["GET", "POST"])

def temperature():
    return render_template("temperature.html" , )

@app.route("/weight",methods=["GET", "POST"])

def weight():
    return render_template("weight.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("diamond_prediction.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get input values from the form
            features = [
                float(request.form["carat"]),
                float(request.form["depth"]),
                float(request.form["table"]),
                float(request.form["x"]),
                float(request.form["y"]),
                float(request.form["z"]),
                float(request.form["cut"]),
                float(request.form["color"]),
                float(request.form["clarity"])
            ]
            prediction = model.predict([features])[0]
            return render_template("index.html", prediction=round(prediction, 2))
        except Exception as e:
            return render_template("index.html", prediction="Error: " + str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

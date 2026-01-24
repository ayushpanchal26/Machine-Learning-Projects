from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        try:
            # Get values from form
            spx = float(request.form["spx"])
            uso = float(request.form["uso"])
            slv = float(request.form["slv"])
            eur_usd = float(request.form["eur_usd"])

            # Prepare input for prediction
            input_data = np.array([[spx, uso, slv, eur_usd]])

            # Predict gold price
            prediction = model.predict(input_data)[0]

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)

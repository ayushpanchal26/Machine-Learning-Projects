from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        age = int(request.form["age"])
        sex = request.form["sex"]
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = request.form["region"]

        # Encode categorical variables
        sex_encoded = 1 if sex == "male" else 0
        smoker_encoded = 1 if smoker == "yes" else 0

        region_mapping = {
            "northeast": 0,
            "northwest": 1,
            "southeast": 2,
            "southwest": 3
        }
        region_encoded = region_mapping.get(region, 0)

        # Prepare input for prediction
        input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])

        # Predict insurance cost
        prediction = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction_text=f"Estimated Medical Insurance Cost: ₹ {prediction:,.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error: Please enter valid input values."
        )

if __name__ == "__main__":
    app.run(debug=True)

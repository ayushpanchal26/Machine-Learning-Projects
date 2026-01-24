from flask import Flask, render_template, request
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get input values from form
    input_features = [
        float(x) for x in request.form.values()
    ]

    # Convert to numpy array and reshape
    final_features = np.array(input_features).reshape(1, -1)

    # Make prediction
    prediction = model.predict(final_features)

    # Output result
    if prediction[0] == 1:
        result = "⚠️ Fraudulent Transaction"
    else:
        result = "✅ Legitimate Transaction"

    return render_template(
        "index.html",
        prediction_text=f"Prediction Result: {result}"
    )

if __name__ == "__main__":
    app.run(debug=True)

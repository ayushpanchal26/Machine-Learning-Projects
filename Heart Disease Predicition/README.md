# ❤️ Heart Disease Prediction – Machine Learning Project

This project predicts whether a person has **heart disease or not** using a **Machine Learning model (Logistic Regression)** and provides a simple **Flask web application** for user interaction.

---

## 📌 Project Overview

- **Problem Type:** Binary Classification  
- **Algorithm Used:** Logistic Regression  
- **Output:**
  - `1` → Person **has heart disease**
  - `0` → Person **does not have heart disease**

The model is trained on medical attributes and predicts the presence of heart disease based on user input.

---

## 📂 Project Structure
- Heart-Disease-Prediction/
- │
- ├── app.py # Flask application
- ├── model.pkl # Trained ML model (saved using pickle)
- ├── heart.csv # Dataset (optional for reference)
- │
- ├── templates/
- │ └── index.html # Frontend HTML page
- │
- └── README.md # Project documentation

📝 Input Details (From User)

The user enters medical values such as:
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- ECG Result
- Maximum Heart Rate
- Exercise Induced Angina
- Oldpeak
- Slope
- Number of Major Vessels
- Thalassemia

📊 Output

“The Person does not have Heart Disease”

“The Person has Heart Disease”a
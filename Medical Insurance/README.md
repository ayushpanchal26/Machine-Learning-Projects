# 🏥 Medical Insurance Cost Prediction

This project predicts **medical insurance charges** based on personal and lifestyle information using **Machine Learning**.  
It is a complete end-to-end project that includes **data preprocessing, model training, evaluation, and deployment using Flask**.

---

## 📌 Problem Statement

Medical insurance costs vary depending on factors like age, BMI, smoking habits, and region.  
The goal of this project is to **predict insurance charges** for a person based on these inputs using a regression model.

---

## 📊 Dataset Information

The dataset contains the following features:

| Feature     | Description |
|------------|------------|
| age        | Age of the person |
| sex        | Gender (male / female) |
| bmi        | Body Mass Index |
| children   | Number of children |
| smoker    | Smoking status (yes / no) |
| region    | Residential region |
| charges   | Medical insurance cost (Target variable) |

---

## 🧠 Machine Learning Model

- **Algorithm Used:** Linear Regression  
- **Type:** Supervised Learning (Regression)
- **Library:** scikit-learn

---

## 🧹 Data Preprocessing Steps

- Converted categorical variables into numerical format
- Selected relevant features
- Split data into training and testing sets
- Trained the regression model on processed data

---

## 📈 Model Evaluation

The model was evaluated by:
- Comparing actual vs predicted values
- Checking regression performance metrics

The results show that the model can reasonably predict insurance costs based on input features.

---

## 🌐 Web Application (Flask)

A Flask-based web application allows users to:
1. Enter personal details through a form
2. Submit the data
3. Instantly receive a predicted insurance cost

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask  
- HTML / CSS  

---

## 📂 Project Structure
- Medical-Insurance-Cost-Prediction/
- │
- ├── app.py
- ├── medical_insurance_model.pkl
- ├── templates/
- │ └── index.html
- ├── static/
- │ └── style.css (optional)
- ├── medical_insurance_cost_prediction.ipynb
- └── README.md
# 💳 Credit Card Fraud Detection System

A Machine Learning project that detects fraudulent credit card transactions using **Logistic Regression**.  
The model is trained on a **balanced dataset** created from a highly imbalanced real-world dataset.

---

## 📌 Project Overview

Credit card fraud is a major financial issue. This project aims to build a **binary classification model** that predicts whether a transaction is:

- **0 → Legitimate**
- **1 → Fraudulent**

The project handles the challenge of **class imbalance** and deploys the trained model using a **Flask web application**.

---

## 🧠 Machine Learning Approach

- **Algorithm Used:** Logistic Regression  
- **Problem Type:** Binary Classification  
- **Imbalance Handling:** Undersampling  
- **Evaluation Metric:** Accuracy Score  

---

## 📊 Dataset Information

- Dataset: `creditcard.csv`
- Features:
  - `V1` to `V28` (PCA transformed)
  - `Time`
  - `Amount`
- Target Column:
  - `Class`
    - `0` → Legit Transaction
    - `1` → Fraud Transaction

### ⚠️ Class Imbalance (Original Dataset)
| Class | Count |
|------|------|
| Legit (0) | ~284,315 |
| Fraud (1) | 492 |

---

## ⚖️ Handling Imbalanced Data

To avoid model bias, **undersampling** is applied:

- 492 Legit transactions selected randomly
- All 492 Fraud transactions retained

Final balanced dataset:
- **984 total samples**
- **50% Legit / 50% Fraud**

---

## 🛠️ Model Pipeline

1. Load and inspect dataset
2. Handle class imbalance using undersampling
3. Split data into features (`X`) and target (`Y`)
4. Train-test split with stratification
5. Train Logistic Regression model
6. Evaluate model performance

---

## 📈 Model Performance

- Training Accuracy: ✔️ High
- Testing Accuracy: ✔️ Consistent

> ⚠️ Note: Accuracy alone is not ideal for fraud detection.  
> Metrics like Precision, Recall, and F1-score are better for real-world systems.

---

## 🌐 Web Application (Flask)

The trained model is deployed using **Flask**, allowing users to:

- Enter transaction feature values
- Predict whether a transaction is **Fraud or Legit**

---

## 📁 Project Structure
- ├── app.py
- ├── Credit_card_fraud.ipynb
- ├── model.pkl
- ├── creditcard.csv
- ├── templates/
- │ └── index.html
- └── README.md

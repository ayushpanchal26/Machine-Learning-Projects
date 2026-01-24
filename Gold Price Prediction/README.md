# 🪙 Gold Price Prediction using Machine Learning

This project predicts the **price of gold (GLD)** using a **Random Forest Regressor** based on key financial indicators such as stock market index, oil price, silver price, and EUR/USD exchange rate.  
The trained model is deployed using a **Flask web application**.

---

## 📌 Project Overview

Gold prices are influenced by multiple economic and market factors. This project uses historical financial data and a machine learning regression model to predict gold prices accurately.

**Type of Problem:** Regression  
**Algorithm Used:** Random Forest Regressor  

---

## 📂 Dataset Information

Dataset file: `gld_price_data.csv`

### Columns:
- `Date` – Date of observation
- `SPX` – S&P 500 Index
- `USO` – Crude Oil Price
- `SLV` – Silver Price
- `EUR/USD` – Euro to USD exchange rate
- `GLD` – **Gold Price (Target Variable)**

✔ No missing values  
✔ Clean numerical data  

---

## 🎯 Features & Target

**Input Features (X):**
- SPX
- USO
- SLV
- EUR/USD

**Target Variable (Y):**
- GLD (Gold Price)

---

## 🧠 Machine Learning Model

- **Model:** RandomForestRegressor
- **Number of Trees:** 100
- **Train-Test Split:** 80% training, 20% testing
- **Evaluation Metric:** R² Score

Random Forest was chosen due to its robustness and ability to capture non-linear relationships in financial data.

---

## 🧪 Model Performance

The model achieves a strong **R² score**, indicating good predictive accuracy.  
A comparison plot between **actual vs predicted gold prices** is used to visually evaluate performance.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Flask
- Pickle

---

## 📁 Project Structure
Gold-Price-Prediction/
- │
- ├── gld_price_data.csv
- ├── gold_prediction.ipynb
- ├── model.pkl
- ├── app.py
- ├── templates/
- │ └── index.html
- └── README.md
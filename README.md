# 🌾 Crop Recommendation System

A Machine Learning-based web application that recommends the most suitable crop and predicts expected yield based on soil nutrients and environmental conditions.

---

## 📌 Project Overview

This project uses Machine Learning algorithms to analyze agricultural data and provide:

* 🌱 Recommended Crop
* 📈 Expected Yield
* 📊 Model Comparison (Decision Tree, Random Forest, Gradient Boosting)

The system takes user inputs such as soil nutrients and weather conditions and predicts the best crop for cultivation.

---

## 🚀 Features

* ✅ Crop prediction using ML models
* ✅ Yield prediction using regression
* ✅ Comparison of multiple models
* ✅ Interactive web interface (Flask)
* ✅ Supports all Indian states
* ✅ Visualization of model performance

---

## 🧠 Machine Learning Models Used

* Decision Tree Classifier
* Random Forest Classifier
* Gradient Boosting Classifier
* Random Forest Regressor (for yield prediction)

---

## 📊 Input Parameters

The system takes the following inputs:

* State
* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Rainfall
* pH value

---

## 📈 Output

* 🌱 Recommended Crop
* 📈 Predicted Yield
* 📊 Model Comparison Graph

---

## 🗂️ Project Structure

```
capstone/
│
├── dataset.py
├── model.py
├── app.py
├── final_dataset.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── graph.png
│
└── README.md
```


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import joblib
import os

# Ensure static folder exists
os.makedirs("static", exist_ok=True)

# Load dataset
df = pd.read_csv("final_dataset.csv")

# Encoding
le_state = LabelEncoder()
df['State'] = le_state.fit_transform(df['State'])

le_crop = LabelEncoder()
df['Crop'] = le_crop.fit_transform(df['Crop'])

# Features
X = df[['State','N','P','K','temperature','rainfall','ph']]
y_crop = df['Crop']
y_yield = df['Yield']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y_crop, test_size=0.2)

# Models
dt = DecisionTreeClassifier()
rf = RandomForestClassifier()
gb = GradientBoostingClassifier()

models = {"Decision Tree": dt, "Random Forest": rf, "Gradient Boosting": gb}
acc = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc[name] = accuracy_score(y_test, pred)

# Save best model
best_model = models[max(acc, key=acc.get)]
joblib.dump(best_model, "best_model.pkl")

# Yield model
yield_model = RandomForestRegressor()
yield_model.fit(X, y_yield)
joblib.dump(yield_model, "yield_model.pkl")

# Save encoders
joblib.dump(le_state, "state.pkl")
joblib.dump(le_crop, "crop.pkl")

# Plot graph
plt.figure()
plt.bar(acc.keys(), acc.values())
plt.title("Model Comparison")
plt.ylabel("Accuracy")
plt.savefig("static/graph.png")

print("Model training complete!")
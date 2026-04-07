from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("best_model.pkl")
yield_model = joblib.load("yield_model.pkl")

le_state = joblib.load("state.pkl")
le_crop = joblib.load("crop.pkl")

@app.route('/')
def home():
    return render_template("index.html", states=le_state.classes_)

@app.route('/predict', methods=['POST'])
def predict():
    state = request.form['state']
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temp = float(request.form['temp'])
    rainfall = float(request.form['rainfall'])
    ph = float(request.form['ph'])

    state_enc = le_state.transform([state])[0]

    data = np.array([[state_enc, N, P, K, temp, rainfall, ph]])

    crop = le_crop.inverse_transform(model.predict(data))[0]
    yield_val = yield_model.predict(data)[0]

    return render_template("index.html",
                           crop=crop,
                           yield_val=round(yield_val, 2),
                           states=le_state.classes_)

if __name__ == "__main__":
    app.run(debug=True)
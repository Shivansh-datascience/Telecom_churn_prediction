import flask
from flask import Flask, request, jsonify
from tensorflow import keras
from keras.models import load_model
import numpy as np
import joblib
from pymongo import MongoClient
import warnings
from dotenv import load_dotenv
import os

warnings.filterwarnings("ignore")
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# === Load Models ===
rf_model_path = r'D:\Saiket_internship\backend\notebook\models\prediction_model.pkl'
ann_model_path = r'D:\Saiket_internship\backend\notebook\models\probability_model.keras'

try:
    rf_model = joblib.load(rf_model_path)
    print(f"Random Forest model loaded from {rf_model_path}")
except FileNotFoundError:
    raise FileNotFoundError(f"Random Forest model not found at {rf_model_path}")

try:
    ann_model = load_model(ann_model_path)
    print(f"ANN model loaded from {ann_model_path}")
except OSError:
    raise OSError(f"ANN model not found at {ann_model_path}")



# === Predict Risk Category using ANN model
@app.route('/Predict_risk_customers', methods=['POST'])
def predict_risk_customers():
    try:
        json_data = request.get_json()
        features = json_data["features"]

        input_data = np.array(features).reshape(1, -1)
        churn_result = ann_model.predict(input_data)
        if churn_result > 0.5:
            return jsonify({"message": "You are likely to churn"})
        else:
            return jsonify({"message": "You are not likely to churn"})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# === Predict Risk Probability through Rand forest
@app.route('/predict_probability', methods=['POST'])
def predict_risk_probability():
    try:
        json_data = request.get_json()
        features = json_data["features"]

        input_data = np.array(features).reshape(1, -1)
        prediction_probability = rf_model.predict_proba(input_data)
        prob_risk = float(prediction_probability[0][1]) 
        return jsonify({"Probability_of_Risk": prob_risk})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# === Run the app ===
if __name__ == '__main__':
    app.run(debug=True)

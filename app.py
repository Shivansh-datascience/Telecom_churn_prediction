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

#Creating an mongo db database
MONGO_CLIENT = "mongodb://localhost:27017/"
MONGO_DATABASE = "CRM"
MONGO_COLLECTIONS = "churn_results"

def configure_mongo_credentials(MONGO_CLIENT,MONGO_DATABASE,MONGO_COLLECTIONS):
    try:
        #initialize client 
        mongo_client = MongoClient(MONGO_CLIENT)
        
        #connect with database
        mongo_db = mongo_client[MONGO_DATABASE]

        #connect with collections
        mongo_collection = mongo_db[MONGO_COLLECTIONS]
        return mongo_collection
    except Exception as e:
        raise e
    
mongo_collections = configure_mongo_credentials(
    MONGO_CLIENT,
    MONGO_DATABASE,
    MONGO_COLLECTIONS
    )

# === Predict Risk Category using ANN model
@app.route('/Predict_risk_customers', methods=['POST'])
def predict_risk_customers():
    try:
        json_data = request.get_json()
        features = json_data["features"]

        input_data = np.array(features).reshape(1, -1)
        churn_result = ann_model.predict(input_data)
        if churn_result > 0.5:
            collections_store = {
                'input_data':input_data.flatten().tolist(),
                'result':churn_result.tolist()
            }
            mongo_collections.insert_one(collections_store)
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
        collection_store = {
            'features':input_data.flatten().tolist(),
            'probability':prob_risk.tolist()
        }
        mongo_collections.insert_one(collection_store)
        return jsonify({"Probability_of_Risk": prob_risk})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# === Run the app ===
if __name__ == '__main__':
    app.run(debug=True)



# 📊 Churn Prediction API

This is a **Flask-based REST API** that predicts customer churn using pre-trained machine learning models. It supports both churn classification and churn probability prediction, and logs all predictions into a **MongoDB** database.

---

## 🚀 Features

- ✅ Predict **Churn Risk**: Classification (`0 = No Churn`, `1 = Churn`)
- ✅ Predict **Churn Probability Score**: Float between `0.0` to `1.0`
- ✅ Store prediction inputs and outputs in **MongoDB**
- ✅ Test easily using **Postman**
- ✅ Load models using **TensorFlow/Keras** and **Joblib**

---

## 🧠 Tech Stack

| Component       | Technology                    |
|----------------|-------------------------------|
| API Framework   | Flask (Python 3.8+)           |
| ML Models       | ANN (Keras), Random Forest (Joblib) |
| Model Format     | `.keras` (ANN), `.pkl` (RF)   |
| Database        | MongoDB                       |
| Data Handling   | NumPy, Pandas, Scikit-learn   |

---

## 🧪 Models Used

### 1. Churn Classifier – `prediction_model.pkl`
- **Type**: Random Forest
- **Output**: `0` or `1`

### 2. Churn Probability Predictor – `probability_model.keras`
- **Type**: Artificial Neural Network (ANN)
- **Output**: Probability between `0.0` and `1.0`

---

## 🔧 Installation & Setup

### 1. Clone the Repository

git clone https://github.com/yourusername/churn-prediction-api.git
cd churn-prediction-api

2. Install Required Packages

Ensure Python 3.8+ is installed.

pip install -r requirements.txt

3. Start MongoDB

Ensure MongoDB is running locally or remotely and accessible via the connection string provided in the code (mongodb://localhost:27017/ by default).


---

🌐 API Endpoints

🔹 POST /predict

Purpose: Returns churn classification (0 or 1)

Request JSON:

{
  "feature1": [0,0,1,1,95.0,95.0,0]
}

Response JSON:

{
  "churn_prediction": "You are likely to churn 
}



🔹 POST /predict_proba

Purpose: Returns churn probability (float between 0 and 1)

Request JSON:

{
  "feature1": [0,0,1,1,95.0,95.0,0]
}

Response JSON:

{
  "churn_probability": 0.78
}


---

🗃️ MongoDB Integration

All API requests and prediction results are stored in a MongoDB collection named (e.g., churn_predictions).


---

📁 Project Structure

churn-prediction-api/
│
├── app.py                       # Flask app with API routes
├── requirements.txt             # Python dependencies
├── model/
│   ├── prediction_model.pkl     # Random Forest model
│   └── probability_model.keras  # ANN model
├── utils/
│   └── preprocess.py            # Feature preprocessing helpers (optional)


---

📬 Example Usage (via curl or Postman)

Classification

curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"feature1": 0.5, "feature2": 3.2, ...}'

Probability

curl -X POST http://localhost:8000/predict_proba \
-H "Content-Type: application/json" \
-d '{"feature1": 0.5, "feature2": 3.2, ...}'


---

👨‍💻 Author

Shivansh Bajpai
📧 shivanshb884@gmail.com


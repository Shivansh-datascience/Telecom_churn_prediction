# Churn Prediction API

This project is a Flask-based REST API for predicting customer churn risk and churn probability. It uses a pre-trained Artificial Neural Network (ANN) model and a Random Forest model to serve predictions. It also stores prediction data in MongoDB.

---

## Features

- Predict churn risk classification (`0` = no churn, `1` = churn)
- Predict churn probability score (0.0 to 1.0)
- Store prediction results and features in MongoDB
- Easy to test via REST endpoints (Postman or curl)
- Load models using TensorFlow/Keras and Joblib

---

## Prerequisites

- Python 3.8+
- MongoDB running locally or accessible remotely
- Required Python packages (see `requirements.txt`)
- Pre-trained models (`prediction_model.pkl` and `probability_model.keras`)

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/churn-prediction-api.git
cd churn-prediction-api


Build Docker Image
Make sure Docker Desktop is running.

bash
Copy code
docker build -t shivanshbajpai/churnapi:latest .
Run Docker Container Locally
bash
Copy code
docker run -p 8000:8000 shivanshbajpai/churnapi:latest
Now, open your browser or API client and visit:

arduino
Copy code
http://localhost:8000
Push Docker Image to Docker Hub
Make sure you’re logged in:

bash
Copy code
docker login
Push the image:

bash
Copy code
docker push shivanshbajpai/churnapi:latest


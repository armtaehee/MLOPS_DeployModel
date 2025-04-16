# 🏡 House Price Prediction API - Project Showcase 🚀

Welcome to the **House Price Prediction API**, a sleek **Flask-based** web service that predicts house prices using a trained machine learning model. The project is **containerized with Docker** for easy deployment, making it production-ready and developer-friendly. Below, you'll find everything you need — code, setup, and usage — all in one Markdown file! 🎉

---

## 📖 Overview

This API uses a pre-trained **regression model** to predict house prices based on features such as:

- 🏠 Area  
- 🛏️ Number of bedrooms  
- 🛁 Bathrooms  
- 🌬️ Air conditioning  
- 🛋️ Furnishing status  

Built with **Flask** and containerized with **Docker**, it's a real-world-ready microservice you can run locally or on the cloud. 🚀

---

## 📂 Project Structure
MLOPS_DeployModel/ ├── app.py # Flask application ✨ 
├── model.pkl # Trained ML model 🧠 
├── requirements.txt # Python dependencies 📦 
├── Dockerfile # Docker configuration 🐳 
└── README.md # Project documentation 📜
## 🛠️ Setup Instructions

### ✅ Prerequisites

- 🐍 Python 3.8+
- 🐳 Docker (optional, for containerized deployment)
- 📂 Git

### ⚙️ 1. Clone the Repository
git clone https://github.com/armtaehee/MLOPS_DeployModel.git

cd MLOPS_DeployModel

### ⚙️ 2. Clone the Repository
pip install -r requirements.txt

### 🧪 3. Run the API Locally
python app.py(The API will run at: http://localhost:9000)

### 🐳 4. Run with Docker (Optional)
docker build -t houseprice-app .

docker run -p 9000:9000 houseprice-app

### 🧾 Example Request

curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [7420, 4, 2, 3, 1, 0, 0, 0, 1, 2, 1, 2]}'

     
### 🧾 Example Response

{
  "prediction": 13300000.0
}


### 🧠 Model Info
Dataset: Trained on 545 property listings.

Features:

Numerical: area, bedrooms, bathrooms, stories, parking

Categorical: mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus

Tech Stack: Python, Scikit-learn, Pickle


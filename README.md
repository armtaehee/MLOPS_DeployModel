# 🏡 House Price Prediction API - Project Showcase 🚀

👋 **Hi there!** I'm **Phakhapol Maneesopa** (Phakky), a third-year Computer Engineering student at **KMUTT**. This is my **House Price Prediction API**, a sleek Flask-based API for predicting house prices using a trained machine learning model, containerized with Docker for easy deployment. Built as part of **CPE393 – ML Deployment Exercise 6**, this project showcases my skills in **Python**, **Flask**, and **machine learning deployment**. 

This Markdown file combines all text-based project files (`README.md`, `app.py`, `requirements.txt`, `Dockerfile`) in one place, with a note about the binary `housemodel.pkl`. Let’s dive in! 🎉

---

## 📖 About the Project

🛠️ The **House Price Prediction API** uses a pre-trained regression model to predict house prices based on features like area, bedrooms, and furnishing status. It’s lightweight, scalable, and ready for production with **Docker** support. Below, you’ll find all project files, beautifully formatted for your viewing pleasure! 😎

---

## 📂 Project Structure
house-price-prediction/
├── app/
│   ├── app.py                # Flask application ✨
│   ├── housemodel.pkl        # Trained ML model 🧠
│   └── requirements.txt      # Python dependencies 📦
├── Dockerfile                # Docker configuration 🐳
└── README.md                 # Project documentation 📜

text

Copy

---

## 📜 File 1: README.md

This is the project’s main documentation, outlining setup, usage, and more. It’s been enhanced for clarity and style, inspired by my GitHub profile! 🌟

```markdown
# 🏡 House Price Prediction API

A lightweight **Flask-based API** for predicting house prices using a trained machine learning model, containerized with Docker for seamless deployment.

---

## 📖 Overview

This API leverages a pre-trained regression model to predict house prices based on features like area, number of bedrooms, and furnishing status. It’s designed for easy integration and deployment, with support for both local and Docker-based setups.

---

## 📂 Project Structure
house-price-prediction/
├── app/
│   ├── app.py                # FlaskCUT application
│   ├── housemodel.pkl        # Trained ML model
│   └── requirements.txt      # Python dependencies
├── Dockerfile                # Docker configuration
└── README.md                 # Project documentation

text

Copy

---

## 🛠️ Setup Instructions

### Prerequisites
- 🐍 Python 3.8+
- 🐳 Docker (optional, for containerized deployment)
- 📦 Git

### 1. Clone the Repository
```bash
git clone https://github.com/armtaehee/house-price-prediction.git
cd house-price-prediction
2. Install Dependencies
Navigate to the app directory and install Python packages:

bash

Copy
cd app
pip install -r requirements.txt
3. Run the API Locally
Start the Flask server:

bash

Copy
python app.py
The API will be available at http://localhost:9000.

4. Run with Docker (Optional)
Build and run the Docker container:

bash

Copy
docker build -t houseprice-app .
docker run -p 9000:9000 houseprice-app
🚀 API Usage
Endpoint
POST /predict
Request Format
Send a JSON payload with a features array containing 12 numerical values in the specified order:

json

Copy
{
  "features": [7420, 4, 2, 3, 1, 0, 0, 0, 1, 2, 1, 2]
}
Feature Order and Encoding
Index	Feature	Type	Encoding
0	area	Numerical	Square feet (e.g., 7420)
1	bedrooms	Numerical	Number of bedrooms (e.g., 4)
2	bathrooms	Numerical	Number of bathrooms (e.g., 2)
3	stories	Numerical	Number of stories (e.g., 3)
4	mainroad	Categorical	Yes = 1, No = 0
5	guestroom	Categorical	Yes = 1, No = 0
6	basement	Categorical	Yes = 1, No = 0
7	hotwaterheating	Categorical	Yes = 1, No = 0
8	airconditioning	Categorical	Yes = 1, No = 0
9	parking	Numerical	Number of parking spaces (e.g., 2)
10	prefarea	Categorical	Yes = 1, No = 0
11	furnishingstatus	Categorical	Unfurnished = 0, Semi-furnished = 1, Furnished = 2
Response Format
json

Copy
{
  "prediction": 13300000
}
Example Request
bash

Copy
curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [7420, 4, 2, 3, 1, 0, 0, 0, 1, 2, 1, 2]}'
🧠 Model Information
Dataset: Trained on 545 property listings.
Features:
Numerical: area, bedrooms, bathrooms, stories, parking
Categorical (encoded): mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus
Training: Built using regression algorithms in Python, serialized with pickle.
✍️ Author
Phakhapol Maneesopa

CPE393 – ML Deployment Exercise 6

King Mongkut’s University of Technology Thonburi

🔍 Troubleshooting
Port Conflict: If port 9000 is in use, map a different port:
bash

Copy
docker run -p 8000:9000 houseprice-app
Model File Missing: Ensure housemodel.pkl is in the app directory.
Dependency Issues: Verify Python version and re-run:
bash

Copy
pip install -r requirements.txt
Connection Errors: Confirm the server is running and accessible at http://localhost:9000.
🌟 Why This API?
Lightweight: Built with Flask for simplicity and speed.
Scalable: Dockerized for easy deployment on any platform.
Accurate: Trained on real-world housing data for reliable predictions.
Happy predicting! 🎉

text

Copy

---

## 📜 File 2: app/app.py

⚠️ *Note*: The actual `app.py` content wasn’t provided, so this is a placeholder for a Flask API that loads `housemodel.pkl` and handles POST requests to `/predict`. Please share the real `app.py` to replace this.

```python
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("housemodel.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        features = data["features"]
        
        # Ensure features is a list of 12 numerical values
        if not isinstance(features, list) or len(features) != 12:
            return jsonify({"error": "Expected a list of 12 numerical features"}), 400
        
        # Convert features to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        
        # Return prediction as JSON
        return jsonify({"prediction": float(prediction)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
📜 File 3: app/requirements.txt
⚠️ Note: The actual requirements.txt wasn’t provided, so this is a typical set of dependencies for a Flask-based ML API. Please share the real requirements.txt to replace this.

text

Copy
flask==2.3.3
numpy==1.24.3
scikit-learn==1.3.0
gunicorn==21.2.0
📜 File 4: Dockerfile
⚠️ Note: The actual Dockerfile wasn’t provided, so this is a standard Dockerfile for a Flask-based API. Please share the real Dockerfile to replace this.

dockerfile

Copy
# Use official Python slim image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model
COPY app/ .

# Expose port
EXPOSE 9000
Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "app:app"]

text

Copy

---

## 📜 File 5: housemodel.pkl

🧠 *Note*: The `housemodel.pkl` file is a binary file (a serialized machine learning model) and cannot be included as text in a Markdown file. It should be placed in the `app/` directory and is referenced by `app.py` for predictions.

To use it:
- Ensure `housemodel.pkl` is in the `app/` directory.
- Verify it’s compatible with the Python version and libraries (e.g., `scikit-learn`) used in your environment.

---

## 🛠️ How to Use This Project

1. **Save This File**: Copy this content into a file named `House-Price-Prediction-Project.md`.
2. **Update GitHub Username**: Replace `armtaehee` in the `git clone` command (in the `README.md` section) with your actual GitHub username.
3. **Add Real File Contents**: If you have the actual `app.py`, `requirements.txt`, or `Dockerfile`, replace the placeholders with their contents.
4. **Test the API**: Run the Flask server or Docker container and test with:
   ```bash
   curl -X POST http://localhost:9000/predict -H "Content-Type: application/json" -d '{"features": [7420, 4, 2, 3, 1, 0, 0, 0, 1, 2, 1, 2]}'
Push to GitHub: Add the file to your repository:
bash

Copy
git add House-Price-Prediction-Project.md
git commit -m "Add complete project in single Markdown file"
git push origin main
🔍 Troubleshooting Tips
Server Not Running: Ensure python app.py or docker run ... is executed.
Port Conflict: Use a different port if 9000 is busy (e.g., docker run -p 8000:9000 houseprice-app).
Model Issues: Verify housemodel.pkl is in app/ and compatible with your environment.
Dependency Errors: Run pip install -r requirements.txt in a clean virtual environment.

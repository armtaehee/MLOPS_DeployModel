# 🏠 House Price Prediction API

A lightweight Flask-based API for predicting house prices using a trained machine learning model.

---

## 📋 Overview

This API uses a pre-trained regression model to predict house prices based on numerical and categorical features such as area, number of bedrooms, and furnishing status. The API is containerized with Docker for easy deployment.

---

## 📂 Project Structure
house-price-prediction/
├── app/
│   ├── app.py                # Flask application
│   ├── housemodel.pkl        # Trained machine learning model
│   └── requirements.txt      # Python dependencies
├── Dockerfile                # Docker configuration
└── README.md                 # Project documentation

text

Copy

---

## 🔧 Setup Instructions

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
2. Install Dependencies
Navigate to the app directory and install the required Python packages:

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

4. (Optional) Run with Docker
Build and run the Docker container:

bash

Copy
docker build -t houseprice-app .
docker run -p 9000:9000 houseprice-app
🚀 API Usage
Endpoint
POST /predict
Request Format
Send a JSON payload with a features array containing 12 numerical values in the following order:

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
📂 Model Information
Dataset: Trained on a dataset of 545 property listings.
Features:
Numerical: area, bedrooms, bathrooms, stories, parking
Categorical (encoded): mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus
Training: Built using regression algorithms in Python and serialized with pickle.
✍️ Author
Phakhapol Maneesopa

CPE393 – ML Deployment Exercise 6

King Mongkut’s University of Technology Thonburi

🛠️ Troubleshooting
Port Conflict: If port 9000 is in use, update the docker run command to map a different port (e.g., -p 8000:9000).
Model File Missing: Ensure housemodel.pkl is in the app directory.
Dependency Issues: Verify Python version compatibility and re-run pip install -r requirements.txt.
text

Copy

### Instructions
1. Copy the entire content above.
2. Paste it into your `README.md` file in the root of your project directory (`house-price-prediction/`).
3. Replace `your-username` in the `git clone` command with your actual GitHub username.
4. Save the file.

This version is complete, properly formatted, and ready to use. It includes all the improvement

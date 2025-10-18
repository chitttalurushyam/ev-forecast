# 🚗⚡ End-to-End EV Charging Demand Forecasting  
**From APIs to a live FastAPI model**

## 🎯 Project Overview
This project predicts **daily EV charging demand** using real-world data from DOE/NREL, OpenChargeMap, and Meteostat.  
It demonstrates a **complete machine learning workflow** — from data ingestion and feature engineering to model training, deployment, and serving predictions through a live FastAPI endpoint.

---

## 💡 Why This Project
With the rise in electric vehicle (EV) adoption, utilities and charging network providers need accurate demand forecasting to:

- ⚙️ Optimize charging station utilization  
- 🔋 Balance grid load efficiently  
- 📍 Identify high-priority locations for new charging sites  
- 🚙 Enhance user experience with better station availability  

---

## 🧩 Workflow Breakdown

### 1️⃣ Data Collection
Collected and combined open datasets from:
- **NREL Alternative Fuel Stations (DOE):** Station metadata (location, network, connectors)  
- **OpenChargeMap:** Real-time station and connector availability  
- **Meteostat:** Historical daily weather for selected cities (e.g., Los Angeles, Davis)

All raw data is stored under:  
data/raw/

markdown
Copy code

---

### 2️⃣ Data Cleaning & Feature Engineering
- Standardized and merged datasets by city and date  
- Engineered time-based features: `month`, `dayofweek`, `is_weekend`  
- Integrated weather metrics (`tavg`, `prcp`, `wspd`)  
- Generated realistic target variable `daily_sessions`  
- Final processed dataset saved to:
data/processed/ev_city_weather_demand.csv

yaml
Copy code

---

### 3️⃣ Model Development
- Algorithm: **XGBoost Regressor**  
- Features included weather, infrastructure, and time-based patterns  
- Evaluation Metrics:  
  - **MAE:** 2.13  
  - **R² Score:** 0.948  
- Trained model saved as:
data/processed/xgb_ev_model.pkl

yaml
Copy code

---

### 4️⃣ API Deployment
Built with **FastAPI**, the app exposes a `/predict` endpoint that loads the trained model at startup.

#### Example Request
```bash
POST /predict
{
  "tavg": 18.2,
  "tmin": 12.0,
  "tmax": 22.5,
  "prcp": 0.0,
  "month": 5,
  "dayofweek": 3,
  "is_weekend": 0,
  "num_stations": 80,
  "ev_level2_ports": 120,
  "ev_dc_fast_ports": 20,
  "total_points": 100,
  "avg_power_kw": 22
}
Example Response
json
Copy code
{
  "predicted_daily_sessions": 82.6
} ```bash

---
## 🗂️ Folder Structure
graphql
Copy code
ev-forecast/
│
├── data/
│   ├── raw/               # API source data
│   └── processed/          # Clean data & trained model
│
├── notebooks/
│   └── 1_data_collection.ipynb
│
├── src/
│   └── api/
│       └── app.py          # FastAPI app with /predict endpoint
│
├── README.md
├── requirements.txt
└── .gitignore

---
## 🚀 Quickstart
1. Install Dependencies
bash
Copy code
pip install -r requirements.txt
2. Run the API
bash
Copy code
python -m uvicorn src.api.app:app --reload
3. Open Swagger Docs
Visit:
👉 http://127.0.0.1:8000/docs
---
## 🧠 Tech Stack
Python (pandas, numpy, xgboost, scikit-learn)

FastAPI for deployment

Joblib for model persistence

APIs: DOE/NREL, OpenChargeMap, Meteostat

Visualization: Matplotlib, Seaborn
---
## ✨ Future Improvements
Incorporate real-time EV charging session data

Add demand forecasting by hour instead of daily

Deploy API as a Docker container

Integrate CI/CD with AWS Lambda or Azure Functions


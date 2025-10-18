🚗⚡ End-to-End EV Charging Demand Forecasting — from APIs to a live FastAPI model


> \*\*Goal:\*\* Predict future daily EV charging demand using real-world data from DOE/NREL, OpenChargeMap, and Meteostat.  

> This project demonstrates an end-to-end machine learning workflow — from data ingestion and feature engineering to model training, deployment, and API integration.



---



\## 🏁 Why This Project



With rapid EV adoption, energy utilities and charging network providers must plan infrastructure capacity effectively.  

Accurately forecasting daily charging sessions helps:

\- \*\*Optimize station utilization\*\*

\- \*\*Balance grid load\*\*

\- \*\*Prioritize new charging site locations\*\*

\- \*\*Improve customer experience through better availability\*\*



---



\## 🧩 What We Did — Step by Step



\### \*\*1️⃣ Data Collection\*\*

We pulled public data from three key APIs:

\- \*\*NREL Alternative Fuel Stations (DOE)\*\* → Station metadata (location, connector types, network)

\- \*\*OpenChargeMap\*\* → Real-time station status, number of connectors, power capacity

\- \*\*Meteostat\*\* → Daily weather data for pilot cities (Los Angeles, Davis)



All raw datasets were stored under `data/raw/`.



\### \*\*2️⃣ Data Cleaning \& Feature Engineering\*\*

\- Standardized station coordinates and joined datasets by city.

\- Added time features: `month`, `dayofweek`, `is\_weekend`.

\- Merged weather metrics (`tavg`, `prcp`, `wspd`) with station statistics.

\- Created a synthetic but realistic target variable `daily\_sessions` based on temperature, weather, and station density.

\- Stored clean, joined dataset under `data/processed/ev\_city\_weather\_demand.csv`.



\### \*\*3️⃣ Model Development\*\*

\- Chose \*\*XGBoost Regressor\*\* for its robustness with tabular + non-linear data.

\- Trained using features such as weather, infrastructure, and time patterns.

\- Evaluation metrics:

&nbsp; - \*\*Mean Absolute Error (MAE): 2.13\*\*

&nbsp; - \*\*R² Score: 0.948\*\*

\- Saved final model as `data/processed/xgb\_ev\_model.pkl`.



\### \*\*4️⃣ API Deployment\*\*

\- Built a \*\*FastAPI\*\* microservice exposing a `/predict` endpoint.

\- Model automatically loads on startup.

\- Accepts a JSON input of 12 features (weather, infrastructure, etc.) and returns a forecasted number of charging sessions.



Example:



```bash

POST /predict

{

&nbsp; "tavg": 18.2,

&nbsp; "tmin": 12.0,

&nbsp; "tmax": 22.5,

&nbsp; "prcp": 0.0,

&nbsp; "month": 5,

&nbsp; "dayofweek": 3,

&nbsp; "is\_weekend": 0,

&nbsp; "num\_stations": 80,

&nbsp; "ev\_level2\_ports": 120,

&nbsp; "ev\_dc\_fast\_ports": 20,

&nbsp; "total\_points": 100,

&nbsp; "avg\_power\_kw": 22

}

## Folder Structure 
ev-forecast/
  data/
    raw/          # API pulls (ignored by git)
    processed/    # features & model
  notebooks/
    1_data_collection.ipynb
  src/
    api/
      app.py      # FastAPI: POST /predict
  README.md
  requirements.txt
  .gitignore



## 🚀 Quickstart

```bash
pip install -r requirements.txt
python -m uvicorn src.api.app:app --reload
# open http://127.0.0.1:8000/docs


from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="EV Demand Forecaster")

MODEL_PATH = "data/processed/xgb_ev_model.pkl"
FEATURES = [
    "tavg","tmin","tmax","prcp",
    "month","dayofweek","is_weekend",
    "num_stations","ev_level2_ports","ev_dc_fast_ports",
    "total_points","avg_power_kw"
]

@app.on_event("startup")
def _load_model():
    global model
    model = joblib.load(MODEL_PATH)

class EVRequest(BaseModel):
    tavg: float
    tmin: float
    tmax: float
    prcp: float
    month: int
    dayofweek: int
    is_weekend: int
    num_stations: float
    ev_level2_ports: float
    ev_dc_fast_ports: float
    total_points: float
    avg_power_kw: float

@app.post("/predict")
def predict(req: EVRequest):
    df = pd.DataFrame([req.model_dump()])[FEATURES]
    y = model.predict(df)[0]
    return {"predicted_daily_sessions": round(float(y), 2)}

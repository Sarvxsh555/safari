from fastapi import APIRouter
import pandas as pd
import numpy as np

from src.features.feature_pipeline import generate_features
from src.hotspot.hotspot_detector import get_hotspots
from src.explainability.shap_explainer import ShapExplainer
from src.utils.analytics import *

router = APIRouter()
explainer = ShapExplainer()


# ---------------- MOCK DATA ----------------
def load_dummy_data(n=100):
    return pd.DataFrame({
        "id": [f"SEG-{i:03}" for i in range(n)],
        "latitude": np.random.uniform(10, 30, n),
        "longitude": np.random.uniform(70, 90, n),
        "forest_dist_km": np.random.uniform(0, 5, n),
        "water_dist_km": np.random.uniform(0, 5, n),
        "traffic_density": np.random.uniform(10, 100, n),
        "speed_limit": np.random.uniform(40, 100, n),
        "visibility_distance": np.random.uniform(50, 500, n),
        "rain": np.random.randint(0, 2, n),
        "fog": np.random.randint(0, 2, n),
        "hour": np.random.randint(0, 24, n),
        "historical_incidents": np.random.randint(0, 10, n),
        "road_curvature": np.random.uniform(0, 1, n),
        "vegetation_density": np.random.uniform(0.2, 1, n)
    })


def mock_predict(df):
    return np.random.uniform(0, 1, len(df))


def prepare_data():
    df = load_dummy_data()
    df = generate_features(df)
    df["risk_score"] = mock_predict(df)

    df = add_risk_level(df)
    return df


# ---------------- ROUTES ----------------

@router.get("/")
def home():
    return {"status": "running"}


# ---------------- OVERVIEW ----------------
@router.get("/overview")
def overview():
    df = prepare_data()
    return get_overview_stats(df)


# ---------------- TREND ----------------
@router.get("/trend")
def trend():
    return get_trend_data()


# ---------------- DISTRIBUTION ----------------
@router.get("/risk-distribution")
def distribution():
    df = prepare_data()
    return get_distribution(df)


# ---------------- MAP ----------------
@router.get("/map-data")
def map_data():
    df = prepare_data()

    return df[["id", "latitude", "longitude", "risk_score", "risk_level"]] \
        .rename(columns={"latitude": "lat", "longitude": "lon"}) \
        .to_dict(orient="records")


# ---------------- TOP HOTSPOTS ----------------
@router.get("/top-hotspots")
def top_hotspots():
    df = prepare_data()
    return get_hotspots(df).head(10).to_dict(orient="records")


# ---------------- SEGMENT DETAIL ----------------
@router.get("/segment/{segment_id}")
def segment(segment_id: str):
    df = prepare_data()
    row = df[df["id"] == segment_id]

    if row.empty:
        return {"error": "not found"}

    row = row.iloc[0]

    return {
        "id": row["id"],
        "risk": float(row["risk_score"]),
        "zone": "Northern",
        "vegetation_density": float(row["vegetation_density"]),
        "water_proximity": float(row["water_dist_km"]),
        "speed_limit": float(row["speed_limit"]),
        "historical_incidents": int(row["historical_incidents"])
    }


# ---------------- SHAP GLOBAL ----------------
@router.get("/shap/global")
def shap_global():
    return {
        "features": [
            "vegetation_density",
            "traffic_density",
            "water_dist_km",
            "speed_limit",
            "night"
        ],
        "importance": [0.25, 0.2, 0.18, 0.15, 0.1]
    }


# ---------------- SHAP LOCAL ----------------
@router.get("/shap/local/{segment_id}")
def shap_local(segment_id: str):
    df = prepare_data()
    row = df[df["id"] == segment_id]

    if row.empty:
        return {"error": "not found"}

    row = row.iloc[0]
    explanation = explainer.explain(row)

    return {
        "id": segment_id,
        "risk": float(row["risk_score"]),
        "explanation": explanation
    }


# ---------------- FORECAST ----------------
@router.get("/forecast")
def forecast():
    days = list(range(1, 91))

    return {
        "days": days,
        "SEG-001": np.random.uniform(0.4, 0.7, 90).tolist(),
        "SEG-002": np.random.uniform(0.4, 0.7, 90).tolist(),
        "SEG-003": np.random.uniform(0.4, 0.7, 90).tolist()
    }


# ---------------- SIMULATION ----------------
@router.post("/simulation")
def simulation(data: dict):
    speed = data.get("speed", 60)
    traffic = data.get("traffic", 500)
    vegetation = data.get("vegetation", 0.5)

    risk = (0.3 * (speed/100)) + (0.3 * (traffic/1000)) + (0.4 * vegetation)

    return {"risk": round(risk, 2)}


# ---------------- TABLE DATA ----------------
@router.get("/table-data")
def table_data():
    df = prepare_data()

    return df[[
        "id", "risk_score", "risk_level",
        "historical_incidents", "vegetation_density",
        "water_dist_km", "speed_limit", "traffic_density"
    ]].to_dict(orient="records")
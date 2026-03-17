import pandas as pd


def add_historical_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["incident_density"] = df["historical_incidents"] / (df["historical_incidents"].max() + 1)

    df["neighbor_incident_count"] = df["historical_incidents"].rolling(5, min_periods=1).sum()

    df["historical_risk_score"] = (
        0.5 * df["historical_incidents"] +
        0.3 * df["incident_density"] +
        0.2 * df["neighbor_incident_count"]
    )

    return df
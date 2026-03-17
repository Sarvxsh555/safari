import pandas as pd


def add_distance_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["near_forest"] = (df["forest_dist_km"] < 1).astype(int)
    df["near_water"] = (df["water_dist_km"] < 1).astype(int)

    df["forest_proximity"] = 1 / (df["forest_dist_km"] + 1)
    df["water_proximity"] = 1 / (df["water_dist_km"] + 1)

    df["ecological_risk_index"] = (
        0.6 * df["forest_proximity"] +
        0.4 * df["water_proximity"]
    )

    return df
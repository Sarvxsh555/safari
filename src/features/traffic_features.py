import pandas as pd


def add_traffic_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["high_speed_flag"] = (df["speed_limit"] > 70).astype(int)

    df["traffic_density_category"] = pd.cut(
        df["traffic_density"],
        bins=[0, 50, 100, 1000],
        labels=[0, 1, 2]
    ).astype(float)

    return df
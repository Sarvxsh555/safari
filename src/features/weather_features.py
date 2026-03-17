import pandas as pd


def add_weather_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["low_visibility_flag"] = (df["visibility_distance"] < 200).astype(int)

    df["bad_weather_flag"] = (
        (df["rain"] > 0) | (df["fog"] > 0)
    ).astype(int)

    return df
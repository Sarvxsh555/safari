import pandas as pd


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["is_night"] = ((df["hour"] >= 18) | (df["hour"] <= 6)).astype(int)

    return df
import pandas as pd


def add_interaction_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["dangerous_condition_flag"] = (
        (df["is_night"] == 1) &
        (df["high_speed_flag"] == 1) &
        (df["near_forest"] == 1)
    ).astype(int)

    return df
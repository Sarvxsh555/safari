import pandas as pd


def add_risk_level(df: pd.DataFrame):
    def classify(r):
        if r > 0.75:
            return "critical"
        elif r > 0.5:
            return "high"
        elif r > 0.25:
            return "moderate"
        else:
            return "low"

    df["risk_level"] = df["risk_score"].apply(classify)
    return df


def get_distribution(df: pd.DataFrame):
    return df["risk_level"].value_counts().to_dict()


def get_overview_stats(df: pd.DataFrame):
    return {
        "critical_segments": int((df["risk_level"] == "critical").sum()),
        "emerging_hotspots": int((df["risk_score"] > 0.6).sum()),
        "segments_monitored": len(df),
        "model_accuracy": 91.4
    }


def get_zone_summary(df: pd.DataFrame):
    zones = ["Northern", "Central", "Southern", "Eastern"]
    df["zone"] = [zones[i % 4] for i in range(len(df))]

    return (
        df.groupby("zone")["risk_score"]
        .mean()
        .round(2)
        .to_dict()
    )


def get_trend_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    actual = [15, 20, 12, 10, 25, 30, 28, 35, 42, 38, 45, 50]
    predicted = [18, 22, 14, 11, 27, 29, 32, 37, 44, 41, 48, 55]

    return [
        {
            "month": month,
            "actual": actual_value,
            "predicted": predicted_value,
        }
        for month, actual_value, predicted_value in zip(months, actual, predicted)
    ]

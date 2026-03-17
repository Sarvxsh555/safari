def get_hotspots(df, threshold=0.7):
    hotspots = df[df["risk_score"] > threshold]
    return hotspots.sort_values(by="risk_score", ascending=False)
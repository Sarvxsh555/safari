from .distance_features import add_distance_features
from .traffic_features import add_traffic_features
from .time_features import add_time_features
from .weather_features import add_weather_features
from .historical_features import add_historical_features
from .interaction_features import add_interaction_features


def generate_features(df):
    df = add_distance_features(df)
    df = add_traffic_features(df)
    df = add_time_features(df)
    df = add_weather_features(df)
    df = add_historical_features(df)
    df = add_interaction_features(df)
    return df
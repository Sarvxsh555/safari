import pandas as pd
import pickle
import os
from typing import Any

def save_dataframe(df: pd.DataFrame, path: str) -> None:
    """Save a DataFrame to CSV."""
    df.to_csv(path, index=False)
    print(f"DataFrame saved to {path}")

def save_model(model: Any, path: str) -> None:
    """Save a model using pickle."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {path}")

def load_model(path: str) -> Any:
    """Load a model using pickle."""
    with open(path, "rb") as f:
        return pickle.load(f)

import pandas as pd
import os
from src.utils.io import load_model
from typing import Any

def predict_risk(model_path: str, input_data_path: str, output_path: str) -> pd.DataFrame:
    """
    Load model and predict risk scores for new data.
    """
    model = load_model(model_path)
    df = pd.read_csv(input_data_path)
    
    # TODO: Ensure input_data has same features as training data
    
    predictions = model.predict(df)
    probabilities = model.predict_proba(df)[:, 1] if hasattr(model, "predict_proba") else None
    
    df['predicted_class'] = predictions
    if probabilities is not None:
        df['risk_score'] = probabilities
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")
    
    return df

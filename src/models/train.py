import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import os
import json
from src.utils.logger import setup_logger
from src.utils.io import save_model

logger = setup_logger(__name__)

def train_pipeline(data_path: str, target_col: str, output_dir: str = "outputs/models/"):
    """
    Starter training pipeline.
    """
    logger.info(f"Loading processed data from {data_path}")
    df = pd.read_csv(data_path)
    
    # Separate features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "RandomForest": RandomForestClassifier(n_estimators=100),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    }
    
    results = {}
    best_model_name = None
    best_f1 = -1
    
    logger.info("Starting model training and evaluation...")
    for name, model in models.items():
        logger.info(f"Training {name}...")
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
        
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1": f1_score(y_test, y_pred),
        }
        if y_prob is not None:
            metrics["roc_auc"] = roc_auc_score(y_test, y_prob)
            
        results[name] = metrics
        logger.info(f"{name} Results: {metrics}")
        
        # Save model
        save_model(model, os.path.join(output_dir, f"{name.lower()}_model.pkl"))
        
        if metrics["f1"] > best_f1:
            best_f1 = metrics["f1"]
            best_model_name = name

    # Save comparison results
    with open("outputs/metrics/model_comparison.json", "w") as f:
        json.dump(results, f, indent=4)
    
    logger.info(f"Best model: {best_model_name} with F1 score: {best_f1}")
    return results

if __name__ == "__main__":
    # Example usage (will fail if data/processed/sample.csv doesn't exist)
    # train_pipeline("data/processed/sample.csv", "target")
    pass

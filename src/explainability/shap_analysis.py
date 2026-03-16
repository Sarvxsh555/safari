import shap
import matplotlib.pyplot as plt
import pandas as pd
import os
from src.utils.io import load_model

def run_shap_analysis(model_path: str, data_path: str, output_dir: str = "outputs/shap/"):
    """
    Compute SHAP values and generate plots for a tree-based model.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    model = load_model(model_path)
    X = pd.read_csv(data_path)
    if 'target' in X.columns:
        X = X.drop(columns=['target'])
        
    # Initialize explainer (TreeExplainer for tree-based models)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    
    # Summary plot
    plt.figure()
    shap.summary_plot(shap_values, X, show=False)
    plt.savefig(os.path.join(output_dir, "shap_summary_plot.png"))
    plt.close()
    
    # Feature importance output
    # For binary classification with XGBoost/RF, shap_values can be a list or array
    # We'll take the mean absolute SHAP values as a simple importance measure
    import numpy as np
    if isinstance(shap_values, list):
        # Multi-class or certain RF implementations
        mean_shap = np.abs(shap_values[1]).mean(axis=0)
    else:
        mean_shap = np.abs(shap_values).mean(axis=0)
        
    importance_df = pd.DataFrame({
        'feature': X.columns,
        'importance': mean_shap
    }).sort_values(by='importance', ascending=False)
    
    importance_df.to_csv(os.path.join(output_dir, "feature_importance_shap.csv"), index=False)
    print("SHAP analysis completed and saved.")

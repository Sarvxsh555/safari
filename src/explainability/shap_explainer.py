import numpy as np
import pandas as pd


class ShapExplainer:
    def __init__(self, model=None):
        """
        model = actual ML model (optional for now)
        """
        self.model = model
        self.use_real_shap = False  # toggle later

    # -------------------------------
    # MOCK EXPLANATION (CURRENT)
    # -------------------------------
    def mock_explain(self, row: pd.Series):
        """
        Generate fake SHAP-like explanation
        """

        explanation = {}

        # Key features influencing risk
        explanation["near_forest"] = float(row.get("near_forest", 0)) * 0.3
        explanation["high_speed"] = float(row.get("high_speed_flag", 0)) * 0.25
        explanation["is_night"] = float(row.get("is_night", 0)) * 0.2
        explanation["historical_risk"] = float(row.get("historical_risk_score", 0)) * 0.25

        return explanation

    # -------------------------------
    # REAL SHAP (FUTURE)
    # -------------------------------
    def real_shap_explain(self, X: pd.DataFrame):
        """
        Replace this later with actual SHAP
        """
        import shap

        explainer = shap.Explainer(self.model)
        shap_values = explainer(X)

        return shap_values

    # -------------------------------
    # MAIN FUNCTION
    # -------------------------------
    def explain(self, row: pd.Series):
        if self.use_real_shap and self.model is not None:
            return self.real_shap_explain(row.to_frame().T)
        else:
            return self.mock_explain(row)
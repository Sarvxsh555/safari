# S.A.F.A.R.I.
**Segment-based Animal Forecasting and Risk Intelligence**

## Project Goal
Build an explainable machine learning system that predicts future wildlife-vehicle collision (WVC) hotspots on highway segments using environmental, traffic, terrain, and historical incident data. This repository provides a scalable foundation for training ML models, generating risk scores, and explaining predictions.

## Repo Structure
```text
.
├── configs/            # Configuration files (YAML)
├── data/               # Data storage
│   ├── raw/            # Original, immutable data
│   ├── interim/        # Transformed, intermediate data
│   ├── processed/      # Final data for modeling
│   └── external/       # Data from third-party sources
├── docs/               # Project documentation
├── notebooks/          # Jupyter notebooks for exploration
├── outputs/            # Generated files
│   ├── models/         # Saved model binaries (.pkl)
│   ├── metrics/        # Evaluation results (JSON/CSV)
│   ├── predictions/    # Prediction outputs
│   ├── shap/           # SHAP plots and data
│   └── figures/        # Miscellaneous plots
├── src/                # Source code
│   ├── data/           # Data loading and preprocessing
│   ├── features/       # Feature engineering
│   ├── models/         # Training and evaluation logic
│   ├── explainability/ # SHAP analysis and interpretability
│   └── utils/          # Utility functions (logger, io, config)
├── tests/              # Unit tests
├── README.md           # Project overview
├── requirements.txt    # Python dependencies
└── pyproject.toml      # Packaging and tool config
```

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd safari
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### 1. Training Pipeline
To train the initial models (Logistic Regression, Random Forest, XGBoost) and compare metrics:
```bash
python -m src.models.train
```
*Note: Ensure `data/processed/sample.csv` exists or update the path in `train_pipeline`.*

### 2. SHAP Analysis
To generate explainability reports for a trained model:
```bash
# Example snippet in a notebook or script
from src.explainability.shap_analysis import run_shap_analysis
run_shap_analysis("outputs/models/xgboost_model.pkl", "data/processed/sample.csv")
```

### 3. Running Tests
```bash
pytest
```

## Future Modules
- **FastAPI Backend**: Deploy models as REST APIs for real-time risk scoring.
- **Streamlit Dashboard**: Interactive visualization of hotspots and prediction explanations.
- **Reporting Module**: Automated generation of safety reports for highway authorities.

## Team Collaboration
- **Modular Design**: Each component in `src/` is decoupled to allow parallel development.
- **Config Driven**: All paths and parameters should be managed via `configs/config.yaml`.
- **Quality First**: Follow the patterns in `tests/` to ensure robust code.

# SAFARI
Segment-based Animal Forecasting and Risk Intelligence

## Overview
SAFARI is an end-to-end wildlife collision risk intelligence platform built around road-segment analysis. It is designed to estimate wildlife-vehicle collision risk for highway segments, rank dangerous segments, explain why those segments are risky, and present the results through a FastAPI backend and a React dashboard.

The system combines feature engineering, model development, explainability, analytics, and visualization into one modular repository.

## What The Project Does
SAFARI can:

- generate segment-level road risk data
- engineer ecological, traffic, time, weather, and historical incident features
- assign segment risk scores and convert them into risk levels
- identify top-risk wildlife collision hotspots
- provide global and local explanation outputs for predictions
- expose the analytics through REST API endpoints
- visualize the outputs through a dashboard with cards, charts, maps, hotspot lists, and tables
- train and compare machine learning models offline
- save model outputs, evaluation reports, and predictions

## Core System Flow
The project is organized as a full analytics pipeline:

1. Raw segment attributes are loaded or generated.
2. Feature engineering transforms those inputs into risk-related signals.
3. A scoring layer assigns a risk score to each segment.
4. Utility logic derives risk categories, summaries, and trend outputs.
5. Explainability logic provides feature importance and local explanations.
6. FastAPI exposes the outputs through endpoints.
7. A React frontend consumes the API and displays the system as an operational dashboard.

## Feature Engineering
Feature generation is coordinated through [src/features/feature_pipeline.py](src/features/feature_pipeline.py).

The pipeline currently builds:

- Distance and ecological features
  - near forest
  - near water
  - forest proximity
  - water proximity
  - ecological risk index

- Traffic features
  - high speed flag
  - traffic density category

- Time features
  - night condition flag

- Weather features
  - low visibility flag
  - bad weather flag

- Historical incident features
  - incident density
  - rolling neighbor incident count
  - historical risk score

- Interaction features
  - dangerous condition flag combining night driving, high speed, and ecological proximity

These features reflect the real purpose of the system: converting raw segment inputs into actionable wildlife collision risk signals.

## Hotspot Detection
Hotspot ranking is handled in [src/hotspot/hotspot_detector.py](src/hotspot/hotspot_detector.py).

The current logic:

- filters segments above a configurable risk threshold
- sorts them by descending risk score
- returns the highest-risk segments first

This gives the system an operational view of where intervention should happen first.

## Explainability
Explainability is implemented in [src/explainability/shap_explainer.py](src/explainability/shap_explainer.py).

The current system supports:

- mock SHAP-like local explanations for segment-level predictions
- a placeholder structure for integrating real SHAP with trained models later

Current explanation logic highlights factors such as:

- forest proximity
- high speed
- night driving
- historical incident risk

## API Backend
The backend is built with FastAPI and initialized in [src/api/app.py](src/api/app.py).

The main routes are defined in [src/api/routes.py](src/api/routes.py).

### Available endpoints

- `GET /`
  - service status check

- `GET /overview`
  - returns summary metrics such as:
    - critical segments
    - emerging hotspots
    - monitored segments
    - model accuracy

- `GET /trend`
  - returns month-wise actual vs predicted trend data for charts

- `GET /risk-distribution`
  - returns counts by risk level

- `GET /map-data`
  - returns segment coordinates with risk score and risk level

- `GET /top-hotspots`
  - returns the highest-risk segments

- `GET /segment/{segment_id}`
  - returns detailed information for a single segment

- `GET /shap/global`
  - returns global feature importance data

- `GET /shap/local/{segment_id}`
  - returns local explanation data for a segment

- `GET /forecast`
  - returns a 90-day forecast series for sample segments

- `POST /simulation`
  - accepts manual inputs such as speed, traffic, and vegetation to estimate risk

- `GET /table-data`
  - returns tabular segment analysis data

### Current backend status
The API is fully wired to the frontend, but its live scoring currently uses generated mock data and mock prediction behavior rather than a deployed trained model. That makes the backend a working prototype interface over a still-evolving modeling layer.

## Frontend Dashboard
The frontend is a React application located in `frontend/`.

The dashboard is routed in [frontend/src/App.js](frontend/src/App.js) and currently includes:

- Overview
- Risk Map
- Hotspots
- Explainability
- Forecast
- Segment Analysis

### Frontend pages

- Overview
  - summary KPI cards
  - trend chart for actual vs predicted incidents

- Risk Map
  - Leaflet-based map view of segment risk
  - segment markers colored by risk score

- Hotspots
  - ranked list of top-risk segments

- Explainability
  - global feature importance display

- Forecast
  - projected incident trend visualization

- Segment Analysis
  - tabular view of segment risk and historical attributes

### Frontend style
The frontend uses:

- React
- React Router
- Axios
- Leaflet / React Leaflet
- Recharts
- Tailwind CSS
- Framer Motion

The UI is currently styled as a dark analytics dashboard with sidebar navigation, cards, charts, map views, and data tables.

## Model Development Pipeline
The offline model training workflow is implemented in [src/models/train.py](src/models/train.py).

It currently supports training and comparing:

- Logistic Regression
- Random Forest
- XGBoost

The training pipeline:

- loads processed data
- splits train/test
- trains multiple models
- evaluates with:
  - accuracy
  - precision
  - recall
  - F1
  - ROC AUC
- saves trained models
- writes model comparison results

## Prediction Pipeline
Prediction logic is implemented in [src/models/predict.py](src/models/predict.py).

It can:

- load a saved model
- run predictions on new data
- add predicted class output
- add risk scores when the model exposes probabilities
- save predictions to CSV

## Evaluation Utilities
Evaluation helpers are implemented in [src/models/evaluate.py](src/models/evaluate.py).

The project can generate:

- confusion matrix plots
- ROC curve plots
- classification reports

This makes the repository useful not only for dashboard demonstrations, but also for model validation and experimentation.

## Project Structure
```text
.
|-- configs/
|-- frontend/
|   |-- src/
|   |   |-- api/
|   |   |-- components/
|   |   `-- pages/
|-- src/
|   |-- api/
|   |-- explainability/
|   |-- features/
|   |-- hotspot/
|   |-- models/
|   `-- utils/
|-- tests/
|-- pyproject.toml
|-- requirements.txt
`-- README.md
```

## How To Run

### Backend
From the project root:

```powershell
python -m uvicorn src.api.app:app
```

Backend URLs:

- API root: `http://127.0.0.1:8000/`
- API docs: `http://127.0.0.1:8000/docs`

### Frontend
From `frontend/`:

```powershell
cmd /c npm start
```

Frontend URL:

- `http://localhost:3000`

## Development Status
What is production-like already:

- modular code structure
- engineered feature pipeline
- model training and evaluation workflow
- explainability interface
- FastAPI integration
- React dashboard integration

What is still prototype-level:

- API scoring uses generated dummy data
- risk predictions are mock-scored in the live API
- SHAP integration is still partly placeholder
- some pages are still driven by synthetic analytics outputs

## Best Summary
SAFARI is a modular wildlife collision risk analytics platform that engineers road-segment features from environmental, traffic, temporal, weather, and historical incident data, estimates segment risk, ranks hotspots, provides explainability outputs, exposes the results through a FastAPI backend, and visualizes the system in a React dashboard for monitoring, analysis, and decision support.

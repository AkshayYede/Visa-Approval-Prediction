# Visa-Approval-Prediction

This is an end-to-end Machine Learning project built with production-readiness in mind. It predicts whether a visa application will be approved or not based on applicant and job-related features. The project goes far beyond notebooks—incorporating modular ML pipelines, logging, testing, model versioning, deployment, and CI/CD.

---

## 📌 Project Highlights

- ✅ End-to-End ML Pipeline from raw data to deployed model
- ✅ Modular Python package structure
- ✅ MongoDB-based data ingestion
- ✅ Data validation and drift detection using Evidently
- ✅ YAML-driven model configuration and training
- ✅ Model versioning, evaluation, and registry
- ✅ FastAPI-based prediction app
- ✅ Dockerized deployment setup
- ✅ CI/CD integration with GitHub Actions

---

## 🧠 Problem Statement

Predict visa approval status based on structured features like:
- Education level
- Job experience
- Prevailing wage
- Company profile
- And other regulatory metadata

---

## 🔧 Project Architecture

```

visa-approval-prediction/
│
├── config/
│   └── schema.yaml, model.yaml
│
├── src/
│   ├── components/              # Ingestion, transformation, training modules
│   ├── pipelines/               # Entry-point for all pipelines
│   ├── utils/                   # Logging, exceptions, helpers
│   ├── constants/               # Global configs and file names
│   ├── entity/                  # Artifact and config dataclasses
│   └── app.py                   # FastAPI app for predictions
│
├── notebook/                    # Exploratory analysis, data checks
├── artifacts/                  # Saved models, scalers, logs, etc.
├── requirements.txt
├── Dockerfile
├── .github/workflows/          # GitHub Actions CI/CD pipeline
└── README.md

````

---

## 📚 Features Breakdown

### 1. 🛢 Data Ingestion
- Loads data from MongoDB Atlas
- Saves clean data to a local feature store
- Splits into train/test sets

### 2. 🧪 Data Validation & Drift Detection
- Schema checks
- Missing value & duplicate detection
- Drift report using **Evidently** (HTML report)

### 3. 🧹 Data Transformation
- Scaling, encoding, skewness handling
- Feature engineering (e.g., company age)
- SMOTEENN for class imbalance

### 4. 🧠 Model Training
- Configurable via `model.yaml`
- GridSearchCV for hyperparameter tuning
- Tracks F1-score, precision, recall, accuracy

### 5. 📊 Model Evaluation
- Compares new model to previously deployed one
- Pushes model to registry only if improved

### 6. 🌐 FastAPI Web App
- HTML form interface for real-time predictions
- Loads trained model pipeline
- Predicts visa approval in seconds

### 7. 📦 Docker & CI/CD
- Dockerfile for containerized deployment
- GitHub Actions for automated build/test

---
## 🛡 Technologies Used

* Python
* Pandas, NumPy, Scikit-learn
* MongoDB Atlas
* FastAPI
* Evidently
* Docker
* GitHub Actions
* SMOTEENN
* joblib, PyYAML, Logging

---

## 🙌 Acknowledgments

Inspired by real-world MLOps needs — where clean engineering, reproducibility, and scalability matter more than just a notebook that "works."

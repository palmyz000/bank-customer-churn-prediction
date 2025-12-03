# 🏦 **Bank Customer Churn Prediction**

### *End-to-End Machine Learning & MLOps System*

![Project
Banner](https://img.shields.io/badge/Status-Production%20Ready-success)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5)

This project delivers a **production-ready MLOps pipeline** for
predicting customer churn in the banking sector.\
It includes EDA, model training, hyperparameter tuning, API deployment,
containerization, and Kubernetes scaling.

## 🎯 **Business Objective & Problem Statement**

Acquiring a new customer costs **5--10× more** than retaining an
existing one.\
The purpose of this project is to **identify high-risk customers** so
the business can take preventive retention actions.

### **Objective**

-   Predict customers who are likely to churn.

### **Business Value**

-   Enable targeted retention campaigns.\
-   Reduce customer attrition and maximize customer lifetime value
    (CLV).

### **Metric Strategy**

-   Primary metric: **Recall (minimize False Negatives)**\
-   Missing a churning customer is more costly than a false positive.

### **Optimized Threshold**

-   Decision threshold adjusted to **0.40**\
-   Captures \~**80%** of all churners.

## 🛠️ **Tech Stack & Tools**

### **Data Science & ML**

-   Python, Pandas, NumPy\
-   Scikit-learn, XGBoost\
-   Imbalanced-learn (SMOTE)

### **API Development**

-   FastAPI, Pydantic\
-   Uvicorn

### **DevOps & MLOps**

-   Docker & Docker Compose\
-   Kubernetes (Minikube / Docker Desktop)

### **Visualization**

-   Matplotlib, Seaborn

## 📊 **Key Insights from EDA**

-   Customers aged **40--60** show the highest churn rate.\
-   **Germany** has a significantly higher churn rate than other
    regions.\
-   Customers holding **3--4 banking products** have a much higher churn
    probability.\
-   Inactive members churn at a disproportionately high rate.

## 🏗 **Project Structure**

    customer_churn_project/
    ├── data/                       # Raw & Processed Data
    ├── models/                     # Serialized Models (.joblib)
    │   ├── bank_churn_model.joblib # xgboost model
    ├── notebooks/                  # Research Environment
    │   ├── bank_churn.ipynb        # Jupyter Notebooks
    │   └── Dockerfile              # Docker setup for Notebook
    ├── src/                        # Production API Source Code
    │   ├── main.py                 # FastAPI Application Logic
    │   └── Dockerfile              # Docker setup for API
    ├── k8s/                        # Kubernetes Manifests
    │   ├── deployment.yaml         # Deployment Config
    │   └── service.yaml            # Service (LoadBalancer) Config
    ├── docker-compose.yaml         # Local Orchestration (API + Notebook)
    ├── requirements.txt            # Python Dependencies
    └── README.md                   # Project Documentation

## 🚀 **Deployment Guide**

### **1. Run with Docker**

    # Start all services (API + Notebook)
    docker-compose up -d --build

    # To stop services
    docker-compose down

### **2. Deploy to Kubernetes**

    # Apply all configurations in k8s folder
    kubectl apply -f k8s/

    # Check status
    kubectl get pods

### **3. Access API Docs**

Visit: http://localhost:8000/docs

## 🧪 **Model Performance**

  Metric                Score   Meaning
  --------------------- ------- -------------------------
  Recall (Class 1)      \~80%   Captures most churners
  Precision (Class 1)   \~44%   Accepts false positives
  Accuracy              \~80%   Balanced performance

## 👤 **Author**

**Suphawit MeeSak**\
Junior AI Engineer / Junior Data Scientist\
LinkedIn: https://www.linkedin.com/in/suphawit-meesak/\
Email: Suphawit11@icloud.com

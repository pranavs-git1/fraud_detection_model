# 🛡️ FraudGuard AI: Financial Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

## Project Overview

**FraudGuard AI** is an end-to-end Data Science and Machine Learning application designed to simulate a real-world banking environment. It processes financial transactions, analyzes them for suspicious patterns, and flags potential fraud in real-time.

The system features a **Random Forest Classifier** trained on transaction behaviors (amount, time, location, device) and is deployed via an interactive, dark-mode **Streamlit Dashboard** for real-time monitoring and simulation.

---

## Key Features

### 1. 🧠 Intelligent Fraud Detection Model
* Utilizes a **Random Forest Classifier** robust against overfitting.
* Handles imbalanced data (fraud is rare, ~2%) using class weighting.
* Evaluated using **ROC-AUC** and **Confusion Matrix** for precision[cite: 5].

### 2. ⏳ Advanced Feature Engineering
To improve accuracy, the model doesn't just look at raw numbers; it understands context:
* **Time Since Last Transaction:** Detects impossible travel (e.g., two transactions in different cities within seconds).
* **Velocity Checks:** Tracks transaction frequency (e.g., 20 transactions in 1 hour)[cite: 5].
* **Temporal Analysis:** Identifies high-risk hours (e.g., 3:00 AM) and days.

### 3. 📊 Interactive Dashboard
A professional, "catchy" UI built with Streamlit featuring:
* **Live Overview:** Real-time KPIs (Total Fraud, Blocked Value) and neon-styled charts[cite: 1].
* **Deep Dive Analysis:** 3D Scatter plots and Heatmaps to visualize fraud clusters.
* **AI Predictor:** A simulation tool where users can input hypothetical transaction details to get a live "Risk Score."

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest, Pipeline, Imputers)
* **Visualization:** Plotly (Interactive 3D/2D), Seaborn, Matplotlib
* **Web Framework:** Streamlit
* **Infrastructure:** DNS Configuration (TXT Records for verification)

---

## 📂 Project Structure

```bash
├── generate_fake_data.py    # Script to create realistic synthetic transaction data
├── dashboard.py             # The main Streamlit application (UI + Model Training)
├── transactions.csv         # Generated dataset (created after running step 1)
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation

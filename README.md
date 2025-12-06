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

### 1. Intelligent Fraud Detection Model
* Utilizes a **Random Forest Classifier** robust against overfitting.
* Handles imbalanced data (fraud is rare, ~2%) using class weighting.
* Evaluated using **ROC-AUC** and **Confusion Matrix** for precision[cite: 5].

### 2. Advanced Feature Engineering
To improve accuracy, the model doesn't just look at raw numbers; it understands context:
* **Time Since Last Transaction:** Detects impossible travel (e.g., two transactions in different cities within seconds).
* **Velocity Checks:** Tracks transaction frequency (e.g., 20 transactions in 1 hour)[cite: 5].
* **Temporal Analysis:** Identifies high-risk hours (e.g., 3:00 AM) and days.

### 3. Interactive Dashboard
A professional, "catchy" UI built with Streamlit featuring:
* **Live Overview:** Real-time KPIs (Total Fraud, Blocked Value) and neon-styled charts[cite: 1].
* **Deep Dive Analysis:** 3D Scatter plots and Heatmaps to visualize fraud clusters.
* **AI Predictor:** A simulation tool where users can input hypothetical transaction details to get a live "Risk Score."

---

## Tech Stack

* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest, Pipeline, Imputers)
* **Visualization:** Plotly (Interactive 3D/2D), Seaborn, Matplotlib
* **Web Framework:** Streamlit
* **Infrastructure:** DNS Configuration (TXT Records for verification)

---

## Project Structure

```bash
├── generate_fake_data.py    # Script to create realistic synthetic transaction data
├── dashboard.py             # The main Streamlit application (UI + Model Training)
├── transactions.csv         # Generated dataset (created after running step 1)
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation

```
## How to Run the Project
Prerequisites
Make sure you have Python installed. It is recommended to use a virtual environment.

Step 1: Install Dependencies
```Bash

pip install pandas numpy scikit-learn matplotlib seaborn plotly streamlit
```
Step 2: Generate Data
Run the data generation script to create the synthetic dataset (transactions.csv).

```Bash

python generate_fake_data.py
```
Step 3: Launch the Dashboard
Run the Streamlit app. This will train the model in the background and open the dashboard in your browser.

```Bash

streamlit run dashboard.py
```
## Dashboard Preview
1. Live Monitor
Real-time tracking of transaction volume and fraud attempts. (Add screenshot here)

2. AI Simulation
Test the model by inputting custom transaction details. (Add screenshot here)

## Future Roadmap

Streaming Integration: Implement Apache Kafka for handling high-throughput real-time data.

Deep Learning: Integrate Autoencoders for unsupervised anomaly detection.

Graph Analysis: Use Neo4j to detect fraud rings and connected entities.

## License
This project is open-source and available under the MIT License.

<img width="800" height="500" alt="eda_fraud_distribution" src="https://github.com/user-attachments/assets/6e6d773d-6b8e-4eb9-9369-05430e8f8746" />
<img width="1200" height="600" alt="eda_amount_distribution" src="https://github.com/user-attachments/assets/47898e8f-003f-427f-8070-5d3e22a56e15" />
<img width="800" height="600" alt="model_confusion_matrix" src="https://github.com/user-attachments/assets/587df651-4f0c-44d0-b331-0211e387aa95" />
<img width="1200" height="600" alt="eda_hourly_fraud" src="https://github.com/user-attachments/assets/29d36eca-e2b5-49c0-8802-ba3af853024c" />


# 📊 Customer Retention Dashboard – Analysis & Risk Platform

## Project Overview
The **Customer Retention Dashboard** is an exploratory data analysis (EDA) and decision-support application designed to understand customer behavior and reduce customer loss. It converts raw service data into meaningful insights, enabling teams to monitor retention trends, identify key factors influencing churn, and assess potential customer risk in a clear and structured way.

## 🚀 Key Application Features

- **Customer Retention Analytics Dashboard**  
  Provides an overview of important metrics such as **Customer Loss Rate**, **Active Customers**, and **Revenue at Risk (₹)** to assess overall retention health.

- **Customer Risk Estimator**  
  An interactive tool that estimates customer risk based on contract type, service category, and monthly billing information.

- **Customer Behavior Analysis**  
  Enables deeper exploration of customer segments by analyzing **Plan Distribution** and identifying **Which Plans Customers Tend to Stay With**.

- **Data Quality Check**  
  Automatically identifies and handles missing values, removes duplicate records, and corrects inconsistent or invalid data to improve analysis reliability.

- **Key Insights Section**  
  Highlights important patterns and observations, such as service types or plans associated with higher customer loss.

## 🛠️ Technical Implementation

- **Frontend:** Streamlit-based web application with a clean, modern dark-themed user interface.
- **Visualization:** Interactive charts built using Plotly, including area charts, bar charts, and box plots for clear data interpretation.
- **Business Logic:** Python-based data processing workflow for data cleaning, result validation, and customer retention analysis.
- **Localization:** Configured for the Indian market with all monetary values displayed in **Indian Rupees (₹)**.

## 📂 Project Architecture
```text
exploratory data analysis/
├── app.py                # Main Dashboard Orchestrator
├── src/
│   ├── analyzer.py       # Statistics, Results Checking & Risk Scoring
│   ├── generator.py      # Automated Data Engine (Synthetic Data)
│   └── utils.py          # Data Filtering & CSV Report Export
├── data/                 # Auto-generated CSV Data Store
└── README.md             # Project Documentation
```

## 💻 Setup & Execution
1. **Clone & Install Dependencies**:
   ```bash
   pip install pandas numpy streamlit plotly scipy
   ```
2. **Launch the Dashboard**:
   ```bash
   streamlit run app.py
   ```


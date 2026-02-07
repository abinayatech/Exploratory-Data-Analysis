
import pandas as pd
import numpy as np
from scipy import stats

class ChurnAnalyzer:
    def __init__(self, df):
        self.df = df
        
    def get_quality_report(self):
        """Detect and report data quality issues for professional auditing."""
        report = {
            'missing': self.df.isnull().sum().to_dict(),
            'duplicates': self.df.duplicated().sum(),
            'outliers': self.df[self.df['MonthlyCharges'] > 150].shape[0],
            'invalid_total': self.df[self.df['TotalCharges'] < self.df['MonthlyCharges']].shape[0]
        }
        return report

    def clean_data(self):
        """Professional data pipeline to address identified anomalies."""
        df_clean = self.df.copy()
        
        # Currency Conversion: USD to INR (Approx 1 USD = 83 INR)
        conversion_rate = 83
        df_clean['MonthlyCharges'] = df_clean['MonthlyCharges'] * conversion_rate
        df_clean['TotalCharges'] = df_clean['TotalCharges'] * conversion_rate
        
        # Remove duplicates
        df_clean = df_clean.drop_duplicates()
        
        # Fix typing and missing charges
        df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')
        # Logic: If TotalCharge is missing, estimate based on tenure and monthly rate
        df_clean['TotalCharges'] = df_clean['TotalCharges'].fillna(df_clean['MonthlyCharges'] * df_clean['Tenure'])
        
        # Remove physical outliers that exceed business logic (e.g. testing records)
        # 500 USD * 83 ≈ 41500 INR
        df_clean = df_clean[df_clean['MonthlyCharges'] < 41500] 
        
        return df_clean

    def calculate_metrics(self, df):
        """Business intelligence metrics for real-world decision making."""
        metrics = {
            'churn_rate': (df['Churn'] == 'Yes').mean() * 100,
            'avg_tenure': df['Tenure'].mean(),
            'avg_monthly': df['MonthlyCharges'].mean(),
            'total_revenue_at_risk': df[df['Churn'] == 'Yes']['MonthlyCharges'].sum()
        }
        return metrics

    def run_statistical_tests(self, df):
        """Scientific validation of business assumptions."""
        results = {}
        
        # Relationship: Charges vs Churn
        churn_yes = df[df['Churn'] == 'Yes']['MonthlyCharges']
        churn_no = df[df['Churn'] == 'No']['MonthlyCharges']
        if len(churn_yes) > 1 and len(churn_no) > 1:
            t_stat, p_val = stats.ttest_ind(churn_yes, churn_no)
            results['price_sensitivity'] = {
                'stat': t_stat, 
                'p_value': p_val,
                'interpretation': "Significant" if p_val < 0.05 else "Not Significant"
            }
        return results
    def predict_churn(self, contract, internet, tenure, monthly):
        """Simple rule-based model to estimate churn risk for the calculator."""
        # Baseline risk
        risk = 0.1
        
        # Fiber optic increases risk in this synthetic dataset
        if internet == 'Fiber optic': risk += 0.2
        
        # Month-to-month is high risk
        if contract == 'Month-to-month': risk += 0.4
        elif contract == 'One year': risk -= 0.1
        else: risk -= 0.2
            
        # Higher charges usually mean higher risk
        if monthly > 4000: risk += 0.2 # 4000 INR ≈ 50 USD
        
        # Tenure reduces risk
        if tenure > 24: risk -= 0.2
        elif tenure < 6: risk += 0.1
            
        return max(0.01, min(0.99, risk))

    def get_segment_comparison(self, df):
        """Calculate performance across key dimensions."""
        segments = df.groupby('Contract').agg({
            'MonthlyCharges': 'mean',
            'Churn': lambda x: (x == 'Yes').mean() * 100
        }).reset_index()
        segments.columns = ['Segment', 'AvgBill', 'LossRate']
        return segments

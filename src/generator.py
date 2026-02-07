
import pandas as pd
import numpy as np
import os

def generate_telecom_data(n=2500):
    np.random.seed(42)
    
    # Demographics
    customer_ids = [f'TEL-{i:05d}' for i in range(1, n+1)]
    genders = np.random.choice(['Male', 'Female'], n)
    senior_citizen = np.random.choice([0, 1], n, p=[0.85, 0.15])
    
    # Account Info
    tenure = np.random.randint(0, 73, n)
    contract = np.random.choice(['Month-to-month', 'One year', 'Two year'], n, p=[0.5, 0.25, 0.25])
    payment = np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n)
    
    # Services
    internet = np.random.choice(['DSL', 'Fiber optic', 'No'], n, p=[0.3, 0.5, 0.2])
    tech_support = np.random.choice(['Yes', 'No'], n)
    
    # Charges
    monthly = np.random.normal(70, 25, n).clip(18, 120)
    total = (monthly * tenure).round(2)
    
    # Target: Churn logic
    # Higher monthly charges + Month-to-month + Fiber optic = Higher churn
    churn_prob = (monthly / 120) * 0.4 + (np.where(contract == 'Month-to-month', 0.3, 0)) + (np.where(internet == 'Fiber optic', 0.1, 0))
    churn_prob = churn_prob.clip(0, 1)
    churn = np.array(['Yes' if x > 0.6 else 'No' for x in np.random.random(n) + churn_prob - 0.5])
    
    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Gender': genders,
        'SeniorCitizen': senior_citizen,
        'Tenure': tenure,
        'InternetService': internet,
        'Contract': contract,
        'TechSupport': tech_support,
        'PaymentMethod': payment,
        'MonthlyCharges': monthly.round(2),
        'TotalCharges': total,
        'Churn': churn
    })
    
    # ⚠️ Introduce Data Quality Issues intentionally
    # 1. Missing values
    df.loc[df.sample(int(n*0.02)).index, 'TotalCharges'] = np.nan
    df.loc[df.sample(int(n*0.01)).index, 'InternetService'] = None
    
    # 2. Outliers
    df.iloc[0, 8] = 999.99 # Extreme Monthly Charge
    
    # 3. Duplicates
    df = pd.concat([df, df.head(15)], ignore_index=True)
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/telecom_churn.csv', index=False)
    print("✓ Dataset created at data/telecom_churn.csv")

if __name__ == "__main__":
    generate_telecom_data()

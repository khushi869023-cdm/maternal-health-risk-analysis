import pandas as pd
import numpy as np

# Create a synthetic dataset mimicking the UCI Maternal Health Risk dataset
# Including some "dirty" data to demonstrate Clinical Data Management (CDM) tasks
data = {
    'Age': [25, 35, 150, 40, 22],  # 150 is an outlier/error
    'SystolicBP': [120, 140, 90, 80, 130],
    'DiastolicBP': [80, 90, 100, 60, 85], # 90/100 is logically impossible (Sys < Dia)
    'BS': [7.0, 6.9, 15.0, 7.5, 6.8],
    'BodyTemp': [98.0, 98.6, 105.0, 99.0, 98.0],
    'HeartRate': [70, 76, 60, 72, 300], # 300 is physiologically unlikely for resting
    'RiskLevel': ['low risk', 'high risk', 'high risk', 'mid risk', 'low risk']
}

df = pd.DataFrame(data)

# CDM Task 1: Data Validation / Logic Checks
def run_cdm_checks(df):
    queries = []
    
    for index, row in df.iterrows():
        # Check 1: Age Validity
        if row['Age'] > 100 or row['Age'] < 10:
            queries.append(f"Row {index}: Age {row['Age']} is outside expected range (10-100).")
            
        # Check 2: BP Logic (Systolic must be > Diastolic)
        if row['SystolicBP'] <= row['DiastolicBP']:
            queries.append(f"Row {index}: Systolic BP ({row['SystolicBP']}) is <= Diastolic BP ({row['DiastolicBP']}). Logic Error.")
            
        # Check 3: Physiological Limits (Heart Rate)
        if row['HeartRate'] > 200 or row['HeartRate'] < 40:
             queries.append(f"Row {index}: Heart Rate {row['HeartRate']} is outside physiological limits.")

    return queries

validation_report = run_cdm_checks(df)

# CDM Task 2: Mock SDTM Mapping (Conceptual)
# We will create a simple VS (Vital Signs) domain representation
vs_domain = pd.DataFrame({
    'USUBJID': [f'SUBJ-00{i+1}' for i in range(len(df))], # Unique Subject ID
    'VSTESTCD': ['SYSBP'] * len(df),
    'VSTEST': ['Systolic Blood Pressure'] * len(df),
    'VSORRES': df['SystolicBP'], # Original Result
    'VSORRESU': ['mmHg'] * len(df),
    'VSSTRESC': df['SystolicBP'], # Standard Character Result
    'VSSTRESN': df['SystolicBP']  # Standard Numeric Result
})

print("--- CDM Validation Report (Discrepancy Management) ---")
for q in validation_report:
    print(q)

print("\n--- Mock SDTM VS (Vital Signs) Domain ---")
print(vs_domain.head())
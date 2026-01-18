# Maternal Health Risk Analysis (SQL)

## Overview
This project analyzes maternal health data to identify patterns associated with different pregnancy risk levels using SQL.  
The goal is to understand how vital indicators such as blood pressure, blood sugar, body temperature, and heart rate vary across risk categories.

---

## Dataset
The dataset contains clinical indicators related to maternal health.

### Columns
- **Age**: Age of the pregnant woman (years)
- **SystolicBP**: Systolic blood pressure (mmHg)
- **DiastolicBP**: Diastolic blood pressure (mmHg)
- **BS**: Blood sugar level
- **BodyTemp**: Body temperature (°F)
- **HeartRate**: Heart rate (beats per minute)
- **RiskLevel**: Pregnancy risk classification (low risk, mid risk, high risk)

---

## Objectives
- Analyze the distribution of patients across risk levels
- Compare blood pressure, blood sugar, and heart rate by risk category
- Identify clinical indicators associated with high-risk pregnancies

---

## Tools Used
- SQL (for data querying and analysis)
- SQLite / MySQL (database)

---

## Key Analysis Performed
- Patient count by risk level
- Average systolic and diastolic blood pressure by risk level
- Blood sugar trends across risk categories
- Derived blood pressure category using CASE statements

---

## Key Insights
Detailed insights and clinical interpretation are documented in `insights.md`.

---

## Files in This Repository
- `maternal_health.csv` – Raw dataset
- `maternal_health_analysis.sql` – SQL queries used for analysis
- `insights.md` – Non-technical interpretation of findings
- `README.md` – Project overview and documentation

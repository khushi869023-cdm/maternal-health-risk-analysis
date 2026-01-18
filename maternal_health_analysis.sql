-- Create Database for maternal health risk analysis
CREATE DATABASE maternal_healthcare;
USE maternal_healthcare;


-- Create table for maternal health data
CREATE TABLE data (
    id INT PRIMARY KEY,
    Age INT,
    Systolic_bp INT,
    Diastolic_bp INT,
    BS FLOAT,
    body_temp FLOAT,
    heart_rate INT,
    risk_level VARCHAR(50)
);

-- Load data from CSV file into the table
LOAD DATA INFILE 'D:/maternal-health-risk-analysis/maternal_health.csv'

CREATE DATABASE maternal_healthcare;
USE maternal_healthcare;
CREATE TABLE data (
Age INT,
SystolicBP INT, 
DiastolicBP INT,
BS FLOAT,
Bodytemp FLOAT, 
Heartrate INT,
Risk_level text
);

## 	SELECT TABLE
SELECT * FROM data;

## CHECK ALL THE VALUES PRESENT
SELECT DISTINCT Risk_level FROM data;

## COUNT PATIENTS BY risk_level;
SELECT *
FROM data
WHERE Risk_level = 'high risk';


## AVERAGE SystolicBP 
SELECT risk_level , AVG(SystolicBP) AS avg_sys
FROM data
GROUP BY Risk_level;

## CREATE A DERIVED COLUMN BP_Category
# normal, elevated or hypertension
SELECT *,
CASE
  WHEN SystolicBP < 120 THEN 'Normal'
  WHEN SystolicBP BETWEEN 120 AND 139 THEN 'Elevated'
  ELSE 'Hypertension'
END AS BP_Category
FROM data;


##RISK DISTRIBUTION 
SELECT risk_level, COUNT(*) AS patient_count
FROM data
GROUP BY risk_level;

## BP severity check
SELECT risk_level, 
   AVG (SystolicBP) AS avg_sys ,
   AVG (DiastolicBP) AS avg_dias
FROM data 
GROUP BY risk_level;

## Glucose stress
SELECT risk_level , AVG(BS) AS avg_bs
FROM data
GROUP BY risk_level ;










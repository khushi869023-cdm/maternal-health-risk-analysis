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

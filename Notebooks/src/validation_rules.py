# validation_rules.py
clinical_rules = {  
    "age_range" : {
        "min":10,
        "max":55,
        "severity" : "error",
        "description" : "Maternal age outside reproductive age"
    }, 
    "bp_range": {
        "systolic_min": 70,
        "systolic_max": 250,
        "diastolic_min": 40,
        "diastolic_max": 150,
        "severity" : "error",
        "description" : "Blood pressure values outside physiological range"
    }, 
    "bp_logic" : {
        "rule": "systolic >= diastolic",
        "severity" : "error",   
        "description" : "Physiologically impossible blood pressure"
    },
    "risk_mismatch" : {
        "rule" : "high_bp and low_risk",
        "severity" : "warning",
        "description": "Potential risk misclassification"
    }
}
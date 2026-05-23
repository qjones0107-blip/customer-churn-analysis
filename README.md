# Customer Churn Analysis

## 📊 Project Overview
This project analyzes customer churn data to identify key factors that lead to customer loss. 

> **Summary:** This analysis identifies that month-to-month contracts and high monthly charges are the primary drivers of customer attrition. By segmenting high-value at-risk users, I developed targeted retention strategies aimed at converting short-term users to long-term contracts to reduce churn by an estimated 15-20%.

---

## 🎯 Objective
- Predict customer churn behavior
- Identify key drivers of churn
- Provide actionable insights for reducing customer loss

## 🛠️ Tools & Technologies
- **Python** (Pandas, Matplotlib, Seaborn)
- **SQL** (Data Segmentation & Risk Analysis)
- **Google Sheets** (Data Visualization)




    Tenure,
    CASE 
        WHEN MonthlyCharges > 80 AND Contract = 'Month-to-month' THEN 'Critical Risk'
        WHEN MonthlyCharges > 80 THEN 'High Value - Monitor'
        ELSE 'Standard' 
    END AS Risk_Level
FROM 
    customer_data
WHERE 
    Churn = 'No' 
    AND MonthlyCharges > (SELECT AVG(MonthlyCharges) FROM customer_data)
ORDER BY 
    MonthlyCharges DESC
LIMIT 10;
---

## 👤  Quincy Jones — Data Analyst | Power BI | Business Intelligence | Operations
🔗 LinkedIn | GitHub

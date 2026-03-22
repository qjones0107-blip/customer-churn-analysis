import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('churn_data.csv')

# Preview data
print(df.head())

# Churn distribution
sns.countplot(x='churn', data=df)
plt.title('Churn Distribution')
plt.show()

# Contract type vs churn
sns.countplot(x='contract_type', hue='churn', data=df)
plt.title('Churn by Contract Type')
plt.xticks(rotation=45)
plt.show()

# Monthly charges vs churn
sns.boxplot(x='churn', y='monthly_charges', data=df)
plt.title('Monthly Charges vs Churn')
plt.show()

import pandas as pd

# Load dataset
df = pd.read_csv("C:\Intern\project2\WA_Fn-UseC_-HR-Employee-Attrition.csv", encoding='latin1')

# Quick view
print("First 5 rows:\n", df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Map 'Attrition' to 1 and 0
df['Attrition_FLAG'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Save the cleaned dataset
df.to_csv("C:\Intern\project2\hr_attrition_clean.csv", index=False)

print("\n Cleaned dataset saved as 'hr_attrition_clean.csv'")

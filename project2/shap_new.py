import pandas as pd

# Load SHAP output
df = pd.read_csv(r"C:\Intern\project2\shap_output.csv")

# Columns to keep
id_cols = ['EmployeeNumber', 'Actual_Attrition', 'Predicted_Attrition', 'Attrition_Probability', 'Total_Importance']

# Get only SHAP value columns
shap_cols = [col for col in df.columns if col not in id_cols]

# Melt to long format
shap_long = df.melt(id_vars=['EmployeeNumber'], value_vars=shap_cols,
                    var_name='Feature', value_name='SHAP_Value')

# Save to CSV
shap_long.to_csv(r"C:\Intern\project2\shap_long.csv", index=False)
print("shap_long.csv saved successfully.")


import pandas as pd

# Load long SHAP format
shap_long = pd.read_csv(r"C:\Intern\project2\shap_long.csv")

# Get top 3 features by absolute SHAP value per employee
shap_long['Abs_SHAP'] = shap_long['SHAP_Value'].abs()
top3_df = shap_long.sort_values(['EmployeeNumber', 'Abs_SHAP'], ascending=[True, False])
top3_df = top3_df.groupby('EmployeeNumber').head(3)

# Optional: add rank column
top3_df['Rank'] = top3_df.groupby('EmployeeNumber').cumcount() + 1

# Save to CSV
top3_df.to_csv(r"C:\Intern\project2\shap_top3.csv", index=False)
print("shap_top3.csv saved successfully.")

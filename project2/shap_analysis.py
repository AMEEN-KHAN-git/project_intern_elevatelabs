import pandas as pd
import shap
import joblib

# Load model and test data
model = joblib.load("C:/Intern/project2/logistic_model.pkl")
X_columns = joblib.load("C:/Intern/project2/feature_columns.pkl")
output_df = pd.read_csv(r"C:\Intern\project2\hr_model_output.csv")

# Prepare inputs
X_test_df = output_df[X_columns]

# Get SHAP values
explainer = shap.Explainer(model, X_test_df)
shap_values = explainer(X_test_df)

# Convert SHAP values to DataFrame
shap_df = pd.DataFrame(shap_values.values, columns=X_columns)

# Add metadata
shap_df['EmployeeNumber'] = output_df['EmployeeNumber']
shap_df['Actual_Attrition'] = output_df['Actual_Attrition']
shap_df['Predicted_Attrition'] = output_df['Predicted_Attrition']
shap_df['Attrition_Probability'] = output_df['Attrition_Probability']
shap_df['Total_Importance'] = shap_df[X_columns].abs().sum(axis=1)

# Save
shap_df.to_csv("C:/Intern/project2/shap_output.csv", index=False)
print("SHAP output saved to shap_output.csv")

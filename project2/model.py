import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load dataset
df = pd.read_csv(r"C:\Intern\project2\hr_attrition_clean.csv")

# Preserve EmployeeNumber
employee_ids_all = df['EmployeeNumber']

# Encode target
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df.drop('EmployeeNumber', axis=1), drop_first=True)

X = df_encoded.drop('Attrition', axis=1)
y = df_encoded['Attrition']

# Save column names for reuse
joblib.dump(X.columns, "C:/Intern/project2/feature_columns.pkl")

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=3000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model
joblib.dump(model, "C:/Intern/project2/logistic_model.pkl")

# Prepare DataFrame for Power BI
X_test_df = pd.DataFrame(X_test, columns=X.columns).reset_index(drop=True)
y_test_series = pd.Series(y_test.values, name='Actual_Attrition')
y_pred_series = pd.Series(y_pred, name='Predicted_Attrition')
y_prob_series = pd.Series(model.predict_proba(X_test)[:, 1], name='Attrition_Probability')

# Get EmployeeNumber for test set
hr_df = pd.read_csv(r"C:\Intern\project2\hr_attrition_clean.csv")
employee_ids_test = hr_df.loc[y_test.index, 'EmployeeNumber'].reset_index(drop=True)

# Final combined DataFrame
output_df = pd.concat([
    employee_ids_test.rename('EmployeeNumber'),
    X_test_df,
    y_test_series,
    y_pred_series,
    y_prob_series
], axis=1)

output_df.to_csv(r"C:\Intern\project2\hr_model_output.csv", index=False)
print("hr_model_output.csv saved successfully.")

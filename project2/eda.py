import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("C:\Intern\project2\hr_attrition_clean.csv")

# Set seaborn style
sns.set(style="whitegrid")

# ----- 1. Attrition Distribution -----
plt.figure(figsize=(6, 4))
sns.countplot(x='Attrition', data=df, palette='Set2')
plt.title('Overall Attrition Count')
plt.tight_layout()
plt.show()

# ----- 2. Attrition by Department -----
plt.figure(figsize=(7, 5))
sns.countplot(x='Department', hue='Attrition', data=df, palette='Set1')
plt.title('Attrition by Department')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# ----- 3. Monthly Income Distribution -----
plt.figure(figsize=(7, 4))
sns.histplot(df['MonthlyIncome'], kde=True, color='skyblue')
plt.title('Monthly Income Distribution')
plt.tight_layout()
plt.show()

# ----- 4. Attrition by Job Role -----
plt.figure(figsize=(10, 5))
sns.countplot(y='JobRole', hue='Attrition', data=df, palette='pastel')
plt.title('Attrition by Job Role')
plt.tight_layout()
plt.show()

# ----- 5. Correlation Heatmap -----
plt.figure(figsize=(12, 8))
numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

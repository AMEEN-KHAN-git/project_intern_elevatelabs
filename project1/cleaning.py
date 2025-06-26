import pandas as pd

# Load dataset
df = pd.read_csv("C:/Intern/project1/superstore.csv", encoding='ISO-8859-1')


# Preview
print(df.head())

# Drop unnecessary columns
df.drop(columns=["Postal Code"], inplace=True)

# Check for nulls
print(df.isnull().sum())

# Convert 'Order Date' and 'Ship Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create new columns
df['Month'] = df['Order Date'].dt.strftime('%b')
df['Year'] = df['Order Date'].dt.year
df['Month_Year'] = df['Order Date'].dt.to_period('M').astype(str)

# Save cleaned file
df.to_csv("superstore_cleaned.csv", index=False)

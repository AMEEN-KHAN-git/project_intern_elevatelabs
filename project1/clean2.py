import pandas as pd

df = pd.read_csv("C:/Intern/project1/superstore.csv", encoding='latin1')


# Convert date columns to MySQL-friendly format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

# Save new CSV
df.to_csv("C:/Intern/project1/superstore_clean.csv", index=False)

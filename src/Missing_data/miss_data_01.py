import pandas as pd

df = pd.read_csv('data/Titanic-Dataset.csv')

# number of missing values for each column
print(df.isnull().sum())

# Displays the number and percentage (%) of missing data.
missing = df.isnull().sum()
percentage = (missing / len(df)) * 100

result = pd.DataFrame({
    'Missing Values': missing,
    'Percentage (%)': percentage
})

print(result)

# Sort the columns in descending order of missing values.
sorted_missing = missing.sort_values(ascending=False)
print(sorted_missing)

# the columns with the most missing data

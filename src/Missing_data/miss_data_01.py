import pandas as pd

df = pd.read_csv('data/Titanic-Dataset.csv')

# number of missing values for each column
print("*"*10 + " number of missing values " + "*"*10)
print(df.isnull().sum())
print("*"*45)


# Displays the number and percentage (%) of missing data.
missing = df.isnull().sum()
percentage = (missing / len(df)) * 100

result = pd.DataFrame({
    'Missing Values': missing,
    'Percentage (%)': percentage
})

print("*"*10 + " the number and percentage (%) of missing data " + "*"*10)
print(result)
print("*"*65)


# Sort the columns in descending order of missing values.
sorted_missing = missing.sort_values(ascending=False)
print("*"*10 + " the columns in descending order of missing values " + "*"*10)
print(sorted_missing)
print("*"*70)

# the columns with the most missing data
print("*"*10 + " the columns with the most missing data " + "*"*10)
print(sorted_missing.head(3))
print("*"*60)

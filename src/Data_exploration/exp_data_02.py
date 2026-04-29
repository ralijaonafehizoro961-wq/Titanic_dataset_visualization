import pandas as pd
df = pd.read_csv('data/tested.csv')

# basic statistics for numeric columns
print(df.describe())

# the minimum and maximum values for Age
min_age = df['Age'].min()
max_age = df['Age'].max()

print("******* Min & Max for Age *******")
print(f"Valeur minimum : {min_age}")
print(f"Valeur maximum : {max_age}")   
print("*********************************")
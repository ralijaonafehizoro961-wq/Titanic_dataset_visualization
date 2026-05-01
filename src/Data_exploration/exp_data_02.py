import pandas as pd
df = pd.read_csv('data/tested.csv')

# basic statistics for numeric columns
print(df.describe())

# the minimum and maximum values for Age
min_age = df['Age'].min()
max_age = df['Age'].max()
mean_age = df['Age'].mean()

print("******* Min & Max for Age *******")
print(f"minimum value : {min_age}")
print(f"maximum value : {max_age}")
print(f"average age value : {mean_age}")   
print("*********************************")
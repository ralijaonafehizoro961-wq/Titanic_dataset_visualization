import pandas as pd
df = pd.read_csv('data/Titanic-Dataset.csv')

# Fill in the missing values in the age column with the median.
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
print(df['Age'].isnull().sum())

# fill the Embarked column with the mode
mode_embarked = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(mode_embarked)
print(df['Embarked'].isnull().sum())

# Create a binary variable for the cabin column
print(df['Cabin'].notnull())
df['HasCabin'] = df['Cabin'].notnull().astype(int)
print(df['HasCabin'].head())

# Saves the cleaned dataset
df.to_csv("results/donnees_nettoyees.csv", index=False)
import pandas as pd
df = pd.read_csv('data/Titanic-Dataset.csv')

# number of passengers who survived
survived = df['Survived'].value_counts().get(1, 0)
dead = df['Survived'].value_counts().get(0, 0)
print(f"number of passengers who survived : {survived}")
print(f"number of people who did not survive : {dead}")

# survival percentage
survived_pr = (survived / len(df['Survived'])) * 100
print(f"Survival percentage : {survived_pr:.2f} %")
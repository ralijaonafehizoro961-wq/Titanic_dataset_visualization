import pandas as pd

df = pd.read_csv('results/donnees_nettoyees.csv')

# survival rate for children and adults
children = df[df['Age'] <= 18]
adults = df[df['Age'] > 18]

rate_children = children['Survived'].mean() * 100
rate_adults = adults['Survived'].mean() * 100

print(f" Survival rate for children (Age <= 18) : {rate_children:.0f} %")
print(f" Survival rate for adults (Age > 18) : {rate_adults:.0f} %")


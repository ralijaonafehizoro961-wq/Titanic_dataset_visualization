import pandas as pd
df = pd.read_csv('results/donnees_nettoyees.csv')

# survival rate for women and man
women = df[df['Sex'] == 'female']
man = df[df['Sex'] == 'male']

rate_women = women['Survived'].mean() * 100
rate_man = man['Survived'].mean() * 100
print(f"Survival rate for women : {rate_women:.0f} %")
print(f"Survival rate for man   : {rate_man:.0f} %")
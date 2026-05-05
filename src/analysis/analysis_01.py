import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results/donnees_nettoyees.csv')

# survival rate for women and man
women = df[df['Sex'] == 'female']
man = df[df['Sex'] == 'male']

rate_women = women['Survived'].mean() * 100
rate_man = man['Survived'].mean() * 100
print(f"Survival rate for women : {rate_women:.0f} %")
print(f"Survival rate for man   : {rate_man:.0f} %")

# comparison graph
categories = [f'Women {rate_women:.0f} %', f'Men {rate_man:.0f} %']
rates = [rate_women, rate_man]
plt.figure(figsize=(6, 4))
plt.bar(categories, rates, color=['magenta', 'cyan'])
plt.title('Titanic Survival Rate by Gender')
plt.ylabel('Survival Rate (%)')
plt.ylim(0, 100)
plt.show()
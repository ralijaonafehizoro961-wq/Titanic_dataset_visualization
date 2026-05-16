import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('results/donnees_nettoyees.csv')

# survival rate for children and adults
children = df[df['Age'] <= 18]
adults = df[df['Age'] > 18]

rate_children = children['Survived'].mean() * 100
rate_adults = adults['Survived'].mean() * 100

print(f" Survival rate for children (Age <= 18) : {rate_children:.0f} %")
print(f" Survival rate for adults (Age > 18) : {rate_adults:.0f} %")

# the average age of the Survivors
avr_age = df[df['Survived'] == 1]['Age'].mean()   
print(f" The average age of the survivors : {avr_age:.0f} years")

# the average age of the non-survivors
avr_age = df[df['Survived'] == 0]['Age'].mean()   
print(f" The average age of the non-survivors : {avr_age:.0f} years")

# boxplot to compare the two groups
plt.figure(figsize=(10, 6))
sns.boxplot(x='Survived', y='Age', data=df, palette='Set2')
plt.title('Age distribution according to survival', fontsize=14)
plt.xlabel('Situation', fontsize=12)
plt.ylabel('Âge', fontsize=12)
plt.xticks([0, 1], ['non-survivors', 'survivors'])
plt.grid(axis='y', linestyle='--', alpha=0.7)

# hisplot for Age distribution by survival status
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', palette='Set2')
plt.title('Age distribution by survival status', fontsize=14)
plt.xlabel('Âge', fontsize=12)
plt.ylabel('Number of passengers', fontsize=12)
plt.legend(['non-survivors', 'Survivors'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

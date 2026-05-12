import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results/donnees_nettoyees.csv')

# survival rate for each class
class1 = df[df['Pclass'] == 1]
class2 = df[df['Pclass'] == 2]
class3 = df[df['Pclass'] == 3]

rate_class1 = class1['Survived'].mean() * 100
rate_class2 = class2['Survived'].mean() * 100
rate_class3 = class3['Survived'].mean() * 100

print(f"survival rate for class 1 : {rate_class1:.0f} %")
print(f"survival rate for class 2 : {rate_class2:.0f} %")
print(f"survival rate for class 3 : {rate_class3:.0f} %")

# graph comparison of survival rate for each class
classes = [f'class1 : {rate_class1:.0f} %',f'class2 : {rate_class2:.0f} %',f'class3 : {rate_class3:.0f} %']
rates = [rate_class1,rate_class2,rate_class3]

plt.figure(figsize=(6, 4))
plt.bar(classes, rates, color=['g', 'k','c'])
plt.title('Titanic Survival Rate by passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate (%)')
plt.ylim(0, 100)
plt.show()
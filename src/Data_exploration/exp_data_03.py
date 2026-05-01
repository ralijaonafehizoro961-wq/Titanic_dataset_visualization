import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/Titanic-Dataset.csv')

# number of passengers who survived
survived = df['Survived'].value_counts().get(1, 0)
dead = df['Survived'].value_counts().get(0, 0)
print(f"number of passengers who survived : {survived}")
print(f"number of people who did not survive : {dead}")

# survival percentage
survived_pr = (survived / len(df['Survived'])) * 100
print(f"Survival percentage : {survived_pr:.2f} %")

# Create a bar chart
counts = df['Survived'].value_counts()
ax = counts.plot(kind='bar',color=['red', 'blue'])
plt.title("Survivors vs Non-survivors")
plt.xlabel("Survived (0 = Dead, 1 = Survived)")
plt.ylabel("Number of passengers")
for i, value in enumerate(counts):
    ax.text(i, value, str(value), ha='center', va='bottom')
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('results/donnees_nettoyees.csv')

# Graph of Age Distribution of Titanic Passengers
df['Age'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results/donnees_nettoyees.csv')

columns = ['Survived', 'Age', 'Pclass', 'SibSp', 'Parch', 'Fare']

correlation = df[columns].corr()

sns.heatmap(correlation)

plt.show()
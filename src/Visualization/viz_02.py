import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('results/donnees_nettoyees.csv')

# Survival Distribution on the Titanic
df['Survived'].value_counts().plot(
    kind='pie',
    labels=['Dead', 'Survived'],
    autopct='%1.1f%%',
    colors=['red', 'green']
)

plt.title("Survival Distribution on the Titanic")


plt.show()
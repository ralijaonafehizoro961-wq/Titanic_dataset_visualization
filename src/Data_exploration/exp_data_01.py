import pandas as pd

# Load the CSV file with pandas
df = pd.read_csv('data/Titanic-Dataset.csv')

# Displays the first 10 lines
print("*"*150)
print(df.head(10))
print("*"*150)

# Displays the shape of the dataset
print("\n" + "Dataset shape: " + str(df.shape))

# Displays the names of all columns
print("\n" + "List of columns: " + str(df.columns.tolist()))

# Displays data types
print("\n" + "Types of columns : " + "\n" + str(df.dtypes))

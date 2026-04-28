import pandas as pd

# Load the CSV file with pandas
df = pd.read_csv('data/tested.csv')

# Displays the first 10 lines
print(df.head(10))

# Displays the shape of the dataset
print(df.shape)

# Displays the names of all columns
print(df.columns)

# Displays data types
print(df.dtypes)
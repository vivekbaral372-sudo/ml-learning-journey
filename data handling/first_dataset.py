import pandas as pd

# Load a simple dataset from the internet
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(url)

# Show first 5 rows
print(data.head())

# Show basic information about the dataset
print("\nDataset info:\n")
print(data.info())

# Show statistical summary
print("\nStatistical Summary:\n")
print(data.describe())

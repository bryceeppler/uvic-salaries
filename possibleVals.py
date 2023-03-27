import pandas as pd

# Replace 'path/to/your_file.csv' with the actual path to your CSV file
file_path = 'data.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Define the columns of interest
columns_of_interest = ['Department', 'Faculty']

# Print unique values for the selected columns
for column in columns_of_interest:
    if column in df.columns:
        print(f"Unique values for '{column}':")
        print(df[column].unique())
        print()
    else:
        print(f"Column '{column}' not found in the dataset.")

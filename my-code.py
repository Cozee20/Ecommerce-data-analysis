import pandas as pd
files = ['customers.csv', 'products.csv', 'sales.csv']
df_list = [pd.read_csv(file) for file in files]
combined_df = pd.concat(df_list, ignore_index=True)
missing_counts = combined_df.isnull().sum()
missing_columns = missing_counts[missing_counts > 0]
combined_df.isnull()
missing_counts = combined_df.isnull().sum()
print(missing_counts)
missing_columns = missing_counts[missing_counts > 0]
print("Columns with missing values and their counts:")
print(missing_columns)
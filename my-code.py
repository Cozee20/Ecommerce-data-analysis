import pandas as pd
import random
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
for col in combined_df.columns:
        duplicate_count = combined_df[col].duplicated().sum()
        if duplicate_count > 0:
            print(f"  Column '{col}' has {duplicate_count} duplicate values.")
        else:
            print(f"  Column '{col}' has no duplicates.")
import random
def random_number():
    return random.randint(1000, 9999)



for col in combined_df.columns:
    combined_df[col] = combined_df[col].apply(lambda x: random_number() if pd.isnull(x) else x)


for col in combined_df.columns:
    duplicate_mask = combined_df[col].duplicated()
    combined_df.loc[duplicate_mask, col] = [random_number() for _ in range(duplicate_mask.sum())]
print("After handling missing values and duplicates:")
print(combined_df)
combined_df['Revenue'] = combined_df['price'] * combined_df['quantity']
print(combined_df)


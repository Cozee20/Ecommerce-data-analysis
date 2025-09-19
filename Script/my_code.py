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
# Merge df1 and df2 on a common column, e.g. "ID"
df1 = pd.read_csv('customers.csv')
df2 = pd.read_csv('sales.csv')
merged12 = pd.merge(df1, df2, on=("customer_id"), how='inner')
df3 = pd.read_csv('products.csv')
final_merged = pd.merge(merged12, df3, on=(["product_id", "price"]), how='inner')
print(final_merged)
final_merged.to_csv("master_dataset.csv", index=False)
change = final_merged.groupby('customer_id')['revenue'].sum().reset_index()
change.columns = ['customer_id', 'customer_lifetime_value']
revenue_by_product = final_merged.groupby('product_id')['revenue'].sum().reset_index()
revenue_by_category = final_merged.groupby('category')['revenue'].sum().reset_index()
revenue_by_supplier = final_merged.groupby('supplier')['revenue'].sum().reset_index()
print("Customer Lifetime Value:")
print(change)
print("Revenue by Category:")
print(revenue_by_category)
print("Revenue by Supplier:")
print(revenue_by_supplier)
print("Revenue by Product:")
print(revenue_by_product)




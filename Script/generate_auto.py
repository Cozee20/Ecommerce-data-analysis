import pandas as pd
import random
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns
def random_number():
    return random.randint(1000, 9999)
folder_path = "C:\\Users\\Hp ProBook 640 G5\\Ecommerce-data-analysis\\data"
files = glob.glob(os.path.join(folder_path, "*.csv"))
df_list = [pd.read_csv(file) for file in files]
combined_df = pd.concat(df_list, ignore_index=True)
#find missing values
missing_counts = combined_df.isnull().sum()
missing_columns = missing_counts[missing_counts > 0]
missing_counts = combined_df.isnull().sum()
print(missing_counts)
missing_columns = missing_counts[missing_counts > 0]
print("Columns with missing values and their counts:")
print(missing_columns)
for col in combined_df.columns:
    combined_df[col] = combined_df[col].apply(lambda x: random_number() if pd.isnull(x) else x)
#check for duplicates
for col in combined_df.columns:
        duplicate_count = combined_df[col].duplicated().sum()
        if duplicate_count > 0:
            print(f"  Column '{col}' has {duplicate_count} duplicate values.")
        else:
            print(f"  Column '{col}' has no duplicates.")
#Handle duplicates
for col in combined_df.columns:
    duplicate_mask = combined_df[col].duplicated()
    combined_df.loc[duplicate_mask, col] = [random_number() for _ in range(duplicate_mask.sum())]#
print("After handling missing values and duplicates:")
print(combined_df)
combined_df['Revenue'] = combined_df['price'] * combined_df['quantity']
print(combined_df)
#Merge datasets and perform analysis
customers = pd.read_csv(r"C:\Users\Hp ProBook 640 G5\Ecommerce-data-analysis\data\customers.csv")
products = pd.read_csv(r"C:\Users\Hp ProBook 640 G5\Ecommerce-data-analysis\data\products.csv")
sales = pd.read_csv(r"C:\Users\Hp ProBook 640 G5\Ecommerce-data-analysis\data\sales.csv")
merged12 = pd.merge(customers, sales, on=("customer_id"), how='inner')
final_merged = pd.merge(merged12, products, on=(["product_id", "price"]), how='inner')
print(final_merged)

summary = """Sells are steady but shaky with fashion products leading the way. Electronics and Home Goods are trailing behind. Marketing efforts should focus on boosting these categories to balance sales. Overall, a solid performance with room for growth in specific areas.
"""
os.makedirs("reports", exist_ok=True)
report_path = "reports/auto_report.md"

with open(report_path, "w", encoding="utf-8") as f:
    f.write(summary)

print(f" Report generated: {report_path}")


os.system(f"start {report_path}")


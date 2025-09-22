import pandas as pd
import random
def random_number():
    return random.randint(1000, 9999)
df1 = pd.read_csv('customers.csv')
df2 = pd.read_csv('sales.csv')
df3 = pd.read_csv('products.csv')
files = ['customers.csv', 'products.csv', 'sales.csv']
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
merged12 = pd.merge(df1, df2, on=("customer_id"), how='inner')
final_merged = pd.merge(merged12, df3, on=(["product_id", "price"]), how='inner')
print(final_merged)
final_merged.to_csv("master_dataset.csv", index=True)
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
final_merged['signup_date'] = pd.to_datetime(final_merged['signup_date'])
final_merged['year_month'] = final_merged['signup_date'].dt.to_period('M').astype(str)
# Created a pivot table to show monthly revenue
ptable = pd.pivot_table(final_merged, values='revenue', index='year_month', aggfunc='sum', fill_value=0)    
print("Pivot Table - Monthly Revenue:")
print(ptable)
df = pd.read_csv("master_dataset.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"]) 
backend_date = df["timestamp"].max() + pd.Timedelta(days=1)
rfm = df.groupby("customer_id").agg({
    "timestamp": lambda x: (backend_date - x.max()).days,  
    "sale_id": "nunique",                                  
    "revenue": "sum"                                      
})
rfm.rename(columns={
    "timestamp": "Recency",
    "sale_id": "Frequency",
    "revenue": "Monetary"
}, inplace=True)
rfm["R_score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["F_score"] = pd.qcut(rfm["Frequency"], 5, labels=[1, 2, 3, 4, 5])
rfm["M_score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])
rfm["RFM_Score"] = (
    rfm["R_score"].astype(str) + 
    rfm["F_score"].astype(str) + 
    rfm["M_score"].astype(str)
)
def segment_customer(row):
    r = int(row["R_score"])
    if row["RFM_Score"] == "555":
        return "VIP"
    elif r == 5:
        return "ACTIVE"
    elif r == 1:
        return "AT_RISK"
    elif r < 1: 
        return "LOST"
    else:
        return "OTHERS"
 
rfm["Segment"] = rfm.apply(segment_customer, axis=1)
print("RFM Segmentation:")
print(rfm.head(10))  
       



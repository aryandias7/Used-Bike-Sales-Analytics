import pandas as pd

# 1. Loading Raw Data
url = "https://raw.githubusercontent.com/ROHAN0011/Data-Sets-from-YBI-Foundation/main/Bike%20Prices.csv"
df = pd.read_csv(url)

# 2. Perform the Cleaning
df = df.drop_duplicates().dropna()
df['Bike_Age'] = 2026 - df['Year']
df.rename(columns={'Ex_Showroom_Price': 'Original_Price'}, inplace=True)

#Classifying bikes as "Budget", "Mid-Range", and "Premium".
def categorize_price(price):
    if price < 50000:
        return "Budget Commuter"
    elif price < 150000:
        return "Mid-Range"
    else:
        return "Premium/Superbike"

df['Category'] = df['Original_Price'].apply(categorize_price)

# 4. Exporting to CSV
print("--- EXPORTING ---")
print(df.head())
df.to_csv('Cleaned_Bike_Data.csv', index=False)

print("Saved 'Cleaned_Bike_Data.csv' successfully.")

import pandas as pd

# 1. Load Raw Data
url = "https://raw.githubusercontent.com/ROHAN0011/Data-Sets-from-YBI-Foundation/main/Bike%20Prices.csv"
df = pd.read_csv(url)

# 2. Perform the Cleaning (The "Transformations")
df = df.drop_duplicates().dropna()
df['Bike_Age'] = 2026 - df['Year']
df.rename(columns={'Ex_Showroom_Price': 'Original_Price'}, inplace=True)

# 3. Categorize the Bikes (Creating a new "Dimension" for analysis)
# In the video, they classified "Power Hitters" vs "Anchors".
# We will classify bikes as "Budget", "Mid-Range", and "Premium".
def categorize_price(price):
    if price < 50000:
        return "Budget Commuter"
    elif price < 150000:
        return "Mid-Range"
    else:
        return "Premium/Superbike"

df['Category'] = df['Original_Price'].apply(categorize_price)

# 4. Export to CSV
print("--- EXPORTING ---")
print(df.head())
df.to_csv('Cleaned_Bike_Data.csv', index=False)
print("Saved 'Cleaned_Bike_Data.csv' successfully.")
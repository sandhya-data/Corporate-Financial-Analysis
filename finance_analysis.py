import pandas as pd
print("Analyzing Corporate Financial Performance...")
# Financial Data Setup
data = {
  'Year': [2021, 2022, 2023],
'Total_Revenue': [150000, 220000, 310000],
'Net_Profit': [50000, 68000, 90000]
}
# Create DataFrame
df = pd.DataFrame(data)
# Calculate Profit Margin Percentage
df['Profit_Margin_Percentage'] = (df['Net_Profit'] / df['Total_Revenue']) * 100
print("\n---Financial Metrics Summary---")
print(df.to_string(index=False))

#Libraries imported
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Global Commodity Trade Statistics dataset
df = pd.read_csv('/Users/subhangisati/Downloads/commodity_trade_statics_data.csv')

# About dataset
print(df.head())  # Display the first few rows of the dataset
print(df.info())  # Get information about the dataset

# Describing dataset
print(df.describe())

# Visualizations

# Example 1: Top Exporting Countries
top_exporters = df.groupby('country_or_area')['trade_usd'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 8))
top_exporters.plot(kind='bar', color='skyblue')
plt.title('Top 10 Exporting Countries')
plt.xlabel('Country')
plt.ylabel('Total Trade (USD)')
plt.show()

# Example 2: Trade Volume over Time
df['year'] = pd.to_datetime(df['year'], format='%Y')  # Convert 'year' to datetime format
trade_over_time = df.groupby('year')['trade_usd'].sum()
plt.figure(figsize=(12, 8))
trade_over_time.plot(kind='line', marker='o', color='green')
plt.title('Global Trade Over Time')
plt.xlabel('Year')
plt.ylabel('Total Trade (USD)')
plt.show()

# Example 3: Heatmap of Trade Correlations
correlation_matrix = df[['quantity_kg', 'trade_usd', 'netweight_kg', 'value_usd']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Trade Metrics')
plt.show()

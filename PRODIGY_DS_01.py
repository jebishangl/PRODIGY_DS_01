# TASK 1
# Load the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\Population Data.csv", skiprows=4)
df.head()

print(df.columns)

df = df.drop(columns=['Unnamed: 69'])

data = df[['Country Name', '2020']].dropna()

# Histogram
import matplotlib.pyplot as plt
plt.hist(data['2020'], bins=10)
plt.title("Population Distribution Across Countries (2020)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.show()

# Better Version
import seaborn as sns
sns.histplot(data['2020'], bins=10, kde=True)
plt.title("Population Distribution (2020)")
plt.show()

# Bar Chart
top10 = data.sort_values(by='2020', ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(top10['Country Name'], top10['2020'])
plt.xticks(rotation=45)
plt.title("Top 10 Most Populated Countries (2020)")
plt.show()


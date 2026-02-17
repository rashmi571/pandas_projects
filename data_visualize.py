#data visualization
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/content/sample_data/imdb_movies_shows.csv")

print("Data")
print(df.head())

print("\n information of data")
print(df.info())

print("\n Descibe of data")
print(df.describe(include='all'))

print("\n Missing values")
print(df.isnull().sum())

print("\n shape of the data")
print(f"Rows: {df.shape[0]}, columns: {df.shape[1]}")

print("Delete useless columns")
columns_to_drop = ['release_year','imdb_id']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

print("Visualization data by using pie chart")
x=df['type'].value_counts()
y=df['type'].value_counts().index
plt.figure(figsize=(10,6))
plt.pie(x, labels=y, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of movies and tv shows")
plt.show()



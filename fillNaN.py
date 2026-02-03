#fill nan values
import pandas as pd
data={
    "name":["rashmi","amna","sital","ankit","karishna"],
    "age":[21,22,23,24,None],
    "salary":[None,12000,24000,None,15000]
}
df =pd.DataFrame(data)
print("original dataframe")
print(df)



df_zero_filled = df.copy() 
df_zero_filled.fillna(0, inplace=True)
print("\nFill nan with default zeros")
print(df_zero_filled)


df_mean_filled = df.copy()


df_mean_filled['salary'] = df_mean_filled['salary'].fillna(df_mean_filled['salary'].mean())
df_mean_filled['age'] = df_mean_filled['age'].fillna(df_mean_filled['age'].mean())
print("\nFill nan with mean value (demonstrated on a fresh copy)")
print(df_mean_filled)
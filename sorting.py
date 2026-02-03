#for sorting
import pandas as pd
data={
    "name":["rashmi","amna","sital","ankit","karishna"],
    "age":[21,22,23,24,19],
    "salary":[12500,12000,24000,23000,15000]
}
df =pd.DataFrame(data)
print("original dataframe")
print(df)

#sorting by sort_values
print("\nsorted data in ascending order according to name")
df.sort_values(by="name",ascending=True,inplace=True)
print(df)

print("\n sorted data according to salary in descending order")
df.sort_values(by='salary',ascending=False,inplace=True)
print(df)
#grouping with aggregation
import pandas as pd
data={
    "name":["rashmi","amna","sital","ankit","karishna"],
    "age":[21,22,23,22,21],
    "salary":[60000,12000,24000,70600,15000]
}
df =pd.DataFrame(data)
print("original dataframe")
print(df)

#data grouping in single column
group=df.groupby("age")['salary'].sum()
print("\nAgggregate salary by age")
print(group)

#with multiple column
group1=df.groupby(["age","name"])['salary'].sum()
print("\nAgggregate salary by age and name")
print(group1)




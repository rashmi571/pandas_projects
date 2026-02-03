#remove duplicate rows
import pandas as pd
data={
    "student":["rashmi","amna","rashmi","ankit","karishna"],
    "marks":[21,22,21,24,25],
}
df=pd.DataFrame(data)
print("original data frame")
print(df)

print("\n check duplicate rows")
print(df.duplicated())

remove=df.drop_duplicates()
print("\n remove duplicate rows")
print(remove)




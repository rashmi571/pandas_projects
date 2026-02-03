#merge two data frame
import pandas as pd
data={
    "student":["rashmi","amna","sital","ankit","karishna"],
}
df1=pd.DataFrame(data)

data2={
    "marks":[21,22,23,24,25],
}
df2=pd.DataFrame(data2)

merged_df = pd.merge(df1,df2,right_index=True,left_index=True)
print(merged_df)

#for interplote data means-> filling nan values to predicted previous data ,it work on time series data and follow a trand
import pandas as pd
data={
    "name":["rashmi","amna","sital","ankit","karishna"],
    "age":[21,22,23,24,None],
    "salary":[None,12000,24000,None,15000]
}
df =pd.DataFrame(data)
print("original dataframe")
print(df)

print("\n fill nan space by interploate")
df['salary']=df['salary'].interpolate(method="linear")
df['age']=df['age'].interpolate(method="linear")
print(df)

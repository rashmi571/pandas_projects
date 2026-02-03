import pandas as pd
df=pd.read_excel("random_employee_data.xlsx")
print("Original data frame")
print(df)

#Access and modify
df.loc[2,'salary']=35000
print("\n",df)

#delete the exit column
print("\nDelete updated salary column")
df = df.dropna(axis=1)
print(df)
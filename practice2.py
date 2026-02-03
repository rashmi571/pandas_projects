#pandas question practice
import pandas as pd
data={
    "Name":["Aman","Riya","Rahul"],
      "Age":[21,22,23],
      "City":["Delhi","Mumbai","Pune"]
      }
df=pd.DataFrame(data)
print(df)

#Display: First 2 rows Last 1 row
df1=pd.read_excel("/content/sample_data/random_employee_data.xlsx")
print("\n first 2 rows")
print(df1.head(2))
print("\n last 1 row")
print(df1.tail(1))

#Check: Shape of DataFrame Column names Data types
print("\nShape of Dataframe")
print(df.shape)

print("\n column name of dataframe")
print(df.columns)

print("\n data type of dataframe")
print(df.dtypes)

#insert new passed column
# The insert method modifies the DataFrame in place and returns None, so assigning it to a variable is not necessary.
df.insert(2,"Passed",[True,False,True])
print("\n insert new column")
print(df) # Print the modified df instead of insert_column

#Rename column "City" to "Location".
name_change=df.rename(columns={"City": "Location"})
print("\n rename column")
print(name_change)

#Remove the column "Age".
remove_column=df.drop(columns=["Age"])
print("\n remove column")
print(remove_column)

#Read a CSV file using pd.read_csv()
# Fix: Create a dummy CSV file to ensure pd.read_csv works without FileNotFoundError
dummy_data = {
    'col1': [1, 2, 3],
    'col2': ['A', 'B', 'C']
}
dummy_df = pd.DataFrame(dummy_data)
dummy_df.to_csv('dummy_sample.csv', index=False)
df=pd.read_csv('dummy_sample.csv')
print("\n read csv file")
print(df)

#find missing na replace that with 0
Data={
    "student":["rashmi","amna","sital","ankit","karishna"],
    "marks":[None,22,None,24,25],
    "age":[21,None,23,24,None]
}
df=pd.DataFrame(Data)
print(df)

missing=df.isnull().sum()
print("\n check missing values")
print(missing)

replace=df.fillna(0)
print("\n replace missing values")
print(replace)

#print age > 21
# Note: The original 'student_data.xlsx' might not exist or be accessible in this environment. Using existing df for demonstration.
# If you have 'student_data.xlsx', please upload it to /content/sample_data/ or update the path.
# For now, using a sample DataFrame for this section.
df = pd.DataFrame({
    "Name": ["John", "Jane", "Mike", "Sara"],
    "Age": [20, 22, 25, 21],
    "City": ["New York", "London", "Paris", "Delhi"]
})
filtering=df[(df["Age"] > 21)]
print("\n filtering data show data above age 21")
print(filtering)

#sorting according to age
sort=df.sort_values(['Age'],ascending=False)
print("\n sorting according to age")
print(sort)

#only select city == delhi
select=df[(df["City"] == "Delhi")]
print("\n only select city == delhi")
print(select)

#Use .loc and .iloc to: Access second row Access Name and City columns
print("\n Access second row")
print(df.iloc[1])

print("\n Access Name and City columns")
print(df.loc[:,["Name","City"]])

#remove duplicated
sample={
    "Fruits":["Apple","Papaya","Banana","Apple","Orange"],
    "Quantity":[10,20,30,10,40],
}
df=pd.DataFrame(sample)
print(df)

find_dupli=df.duplicated()
print("\n find duplicate rows")
print(find_dupli)

remove_dupli=df.drop_duplicates()
print("\n remove duplicate rows")
print(remove_dupli)


#Age convert into float into int
age={
    "Name":["rashmi","amna","sital","ankit","karishna"],
    "Age":[21.0,22.0,23.0,29.9,70.9],
}
df=pd.DataFrame(age)
print(df)

df['Age']=df['Age'].astype(int)
print("\n age convert into int")
print(df)

#find meanage,minage,maxage
mean_age=df["Age"].mean()
print("\n mean age")
print(mean_age)

max_age=df["Age"].max()
print("\n max age")
print(max_age)

min_age=df["Age"].min()
print("\n min age")
print(min_age)

#Count how many students are from each city.
# Re-creating df for this section as previous operations might have changed it.
df = pd.DataFrame({
    "Name":["Aman","Riya","Rahul", "Sara"],
    "Age":[21,22,23, 22],
    "City":["Delhi","Mumbai","Delhi", "Pune"]
})
student_count=df["City"].value_counts()
print("\n student count")
print(student_count)

#Group by City and find average age.
df = pd.DataFrame({
    "Name":["Aman","Riya","Rahul"],
    "Age":[21,22,23],
    "City":["Delhi","Mumbai","Delhi"]
})
group=df.groupby("City")["Age"].mean()
print("\n group by city")
print(group)

#adult or young according to age
df["Age_Category"] = df["Age"].apply(
    lambda x: "Young" if x < 22 else "Adult"
)
print(df)


#increase markse
s={
    "marks":[1,2,3,4,5,6],
}
df=pd.DataFrame(s)
print(df)

df["marks"]=df["marks"].apply(lambda x: x+5)
print("\n increase marks")
print(df)


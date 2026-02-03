#finds rows and columns in data set [df.shape]
#find the columns name in data set [df.columns]
import pandas as pd
sample_data={
    "Fruit":["Apple","Orange","Banana","Mango","Grapes","pappya","watermelon","pineapple","lichi","kiwi"],
    "price_per_kg":[50,20,45,60,35,65,45,34,25,30],
    "sale":[40,70,70,80,90,76,75,68,90,90],
    "Quality":[90,80,90,70,80,90,60,67,87,90]
}
df=pd.DataFrame(sample_data)
print("shape",df.shape)
print("columns",df.columns)

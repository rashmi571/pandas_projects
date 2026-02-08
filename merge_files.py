import pandas as pd

train = pd.read_csv("/content/sample_data/Train.csv")
test = pd.read_csv("/content/sample_data/test.csv")

patient = pd.read_csv("/content/sample_data/Patient_Profile.csv")
camp = pd.read_csv("/content/sample_data/Health_Camp_Detail.csv")

first = pd.read_csv("/content/sample_data/First_Health_Camp_Attended.csv")
second = pd.read_csv("/content/sample_data/Second_Health_Camp_Attended.csv")
third = pd.read_csv("/content/sample_data/Third_Health_Camp_Attended.csv")

#merge train data
df=train.merge(patient,on='Patient_ID',how='left')
df=df.merge(camp,on='Health_Camp_ID',how='left')
df=df.merge(first,on=['Patient_ID','Health_Camp_ID'],how='left')
df=df.merge(second,on=['Patient_ID','Health_Camp_ID'],how='left')
df=df.merge(third,on=['Patient_ID','Health_Camp_ID'],how='left')

#merge test date
df_test=test.merge(patient,on='Patient_ID',how='left')
df_test=df_test.merge(camp,on='Health_Camp_ID',how='left')
df_test=df_test.merge(first,on=['Patient_ID','Health_Camp_ID'],how='left')
df_test=df_test.merge(second,on=['Patient_ID','Health_Camp_ID'],how='left')
df_test=df_test.merge(third,on=['Patient_ID','Health_Camp_ID'],how='left')

#save both data
df.to_csv('train_data.csv',index=False)
df_test.to_csv('test_data.csv',index=False)


import pandas as pd

df= pd.read_csv(r"C:\Users\BabitaTiwari\Downloads\CustomerData_Sample.csv")

print(df)

df['Phone']= df['Phone'].fillna('000')
df['Phone']= df['Phone'].str.replace(r'\D','')
df['Email']= df['Email'].fillna('example.com')
df['Email']= df['Email'].str.lower()
df['BirthYear']= df['BirthYear'].astype(int)
df['Age']= 2023 - df['BirthYear']
df['Customer Type'] = pd.cut(df['Age'],
                             bins=[0,30,50,float('inf')],
                             labels= ['Young', 'Middle-Aged','Senior'])

print (df)
df.to_csv('Customer_ModifiedSampleData.csv', index=False)

df = pd.read_csv('Customer_ModifiedSampleData.csv')
cols = ['Age','Customer Type']
print(df[cols].describe())
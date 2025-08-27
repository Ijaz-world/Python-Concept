import pandas as pd
import numpy as np

df=pd.read_csv("E:\Python\Project2\Salaries.csv")

print("\n--Shape of dataset--\n")
print("Number of Rows: ",df.shape[0])
print("Number of Columns : ",df.shape[1])

print("\n--Information about Dataset--\n")
print(df.info())

print("\n--Check Null values in the dataset--\n")
print(df.isnull().sum())

print("\n--Drop ID, Notes, Agency, and Status Columns--\n")
df.drop(columns=['Id','Notes','Agency','Status'], inplace=True)
print(df.columns)  #to check either columns drop or not

print("\n-- Find Occurrence of The Employee Names  (Top 5)--\n")
print(df['EmployeeName'].value_counts().head())

print("\n--Find The Number of Unique Job Titles--\n")
print(df['JobTitle'].nunique())

print("\n--Total Number of Job Titles Contain Captain--\n")
print(len(df[df['JobTitle'].str.contains('captain', case=False)]))

print("\n--Display All the Employee Names From Fire Department--\n")
print(df[df['JobTitle'].str.contains('fire', case=False)]['EmployeeName'])

print("\n--Replace 'Not Provided' in EmployeeName' Column to NaN --\n")
print(df['EmployeeName'].replace('Not provided', np.nan, inplace=True))
print(df['EmployeeName'])

print("\n--Drop The Rows Having 5 Missing Values--\n")
df.drop(df[df.isnull().sum(axis=1)==5].index, axis=0, inplace=True)
print(df.isnull().sum(axis=1))

print("\n--Find Job Title of ALBERT PARDINI--\n")
print(df[df['EmployeeName']=='ALBERT PARDINI']['JobTitle'])

print("\n--Display Name of The Person Having The Highest BasePay--\n")
high_pay=df.loc[df['TotalPay'].idxmax()]
print(high_pay['EmployeeName'])

print("\n--Find Average BasePay of All Employee Per Year --\n")
print(df.groupby('Year')['TotalPay'].mean())

print("\n--Find Average BasePay of Employee Having Job Title ACCOUNTANT--\n ")
print(df[df['JobTitle']=='ACCOUNTANT']['TotalPay'].mean())

print("\n--Find top 5 most common jobs--\n")
print(df['JobTitle'].value_counts().head())
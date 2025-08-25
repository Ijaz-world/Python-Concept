import pandas as pd

# data={
#     "Name":["Ijaz","Ahmad","Arbaz","Hassan","Saim","Huzaifa","Anwar","Irzam"],
#     "Age":[22,23,25,24,22,23,60,7],
#     "Salary":[30000,40000,35000,55000,20000,60000,90000,10000],
#     "Performance Score":[88,67,98,55,83,76,91,80]
# }
# df=pd.DataFrame(data)
# print(df)

# print("\n---Adding New column---\n")
# df.insert(3,"Bonus",df['Salary']*0.1) # df.insert(location,"Column name",Some data)
# print(df)

# print("\n---Updating value---\n")
# df.loc[7,'Age']=8    #df.loc[row_index,'column_name']=new value
# df['Salary']=df['Salary']*1.05  #Change whole column values,-->increasing salary by 5%
# print(df)

# print("\n---Removing columns---\n")
# df.drop(columns=['Bonus'], inplace=True) #inplace=true-->return us orginial data after removing, while inplace=false returns us new or copy ddatset
# print(df)

# data={
#     "Name":["Ijaz","Ahmad",None,"Hassan","Saim","Huzaifa","Anwar","Irzam"],
#     "Age":[22,23,None,24,22,23,60,7],
#     "Salary":[30000,40000,None,55000,20000,60000,90000,10000],
#     "Performance Score":[88,67,None,55,83,76,91,80]
# }

# df=pd.DataFrame(data)
# print(df.isnull().sum())  #sum return us count that in which column how much values is missing
# # print("\n---Drop missing values---\n")
# # df.dropna(axis=0, inplace=True)  #axis=0-->row wise, axis=1--> column wise
# # print(df)

# print("\n---filling missing values---\n")
# # df.fillna(11, inplace=True)   #method to replace with still value
# # print(df)
# df['Age'].fillna(df['Age'].mean(), inplace=True) #Will take mean of Age values and fill them with mean value
# df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# df['Performance Score'].fillna(df['Performance Score'].mean(), inplace=True) 
# df['Name'].fillna("Sultan", inplace=True)
# print(df)

data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print("--Before interpolation--")
print(df)

df['Value']=df['Value'].interpolate(method="linear") #interpolation-->fills missing data by estimating value using surrounding values
print("--After Interpolation--")
print(df)

#--Sorting--
#df.sort_values(by="Column_name",ascending=True,inplace=True) --> for 1 column
#df.sort_values(by=["column_name1","col_name2"], ascending=[True, False], inplace=True)-->for mutilple columns

#--Aggregation--
#df['column_name'].mean()
#df['column_name'].sum()
#df['column_name'].min()
#df['column_name'].max()

#--concatenation--
# pd.concate([df_1,df_2], axis=0, ignore_index=True)

customers={
    "ID":[1,2,3],
    "Name":["ijaz","ahmad","ali"]
}
df_1=pd.DataFrame(customers)

orders={
    "ID":[1,2,4],
    "Amount":[550,456,700]
}
df_2=pd.DataFrame(orders)
merge=pd.merge(df_1,df_2, on="ID", how="inner")
print(merge)
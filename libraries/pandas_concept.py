# Pandas is used for data manipulation (cleaning, modification) and data analysis(finding trend, generating sense)

#how to open files of different format to read
import pandas as pd

# obj=pd.read_csv("E:\Python\libraries\sales_data_sample.csv", encoding="latin1") 
# obj=pd.read_excel("E:\Python\libraries\SampleSuperstore.xlsx") -->if not opening then we set encoding to "utf-8" or "latin"
#obj=pd.read_json("E:\Python\libraries\sample_Data.json")
#print(obj)

#--> how to save updated data into files
data={
    "Name":['Ijaz','Ahmad','Ali'],
    "Age":[22,23,24],
    "City":['Toba','Fsd','Lhr']
}
#df=pd.DataFrame(data)
#print(df)
# df.to_csv("Output.csv", index=False)  -->index=False--> remove serial number that comes in data
#df.to_excel("Output.xlsx")
# df.to_json("Output.json", index=False)

df=pd.read_json("E:\Python\libraries\sample_Data.json")
print("Display first 6 rows: \n",df.head(6))  # if 6 not mentioned, automatically show 5 lines
print("Display last  6 rows: \n",df.tail(6))
print(df.info())    #--. it will show us details of dataset
print(df.describe()) #--> tells us descriptive status of numerical data
print("Shape of dataset: ",df.shape)      #--> return us no. of rowns and columns,shape is attribute not a function
print("Column Names: ",df.columns)    #--> tell us name of columns, column is attribute here not a function
print(df["name"])            #---> way to select and display specific column
print(df[["name","price"]])  #--> selecting multiple columns
print("Rows with price>800: \n",df[df['price']>800])   #-->filter rows with price >800
filter_rows=df[(df['price']>800) & (df['category']=="Electronics")] #filter rows using multiple conditions
print("Filtering rows using multilple condition: \n",filter_rows)


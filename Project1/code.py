import pandas as pd

df=pd.read_csv("E:\Python\Project1\Ecommerce Purchases")

print("\n--Displaying 10 rows from Top--\n")
print(df.head(10))

print("\n--Displaying 10 rows from Bottom--\n")
print(df.tail(10))

print("\n--Data-type of each Column--\n")
print(df.dtypes)

print("\n--Checking Null values--\n")
print(df.isnull().sum())

print("\n--Numbers of rows and columns--\n")
print("Rows: ",df.shape[0])          #shape returns tuple like(Rows, columns)-->Rows=0 index AND columns=1 index
print("Columns: ",df.shape[1])

print("\n--Highest and lowest Purchase Price--\n")
print("Highest Price: ",df['Purchase Price'].max())
print("Lowest Price: ",df['Purchase Price'].min())

print("\n--Average Purchase Price--\n")
print(df['Purchase Price'].mean())

print("\n--How many people have French 'fr' as their Language?--\n")
print(len(df[df['Language']=='fr']))

print("\n--Job titles contain engineer--\n")
print(len(df[df['Job'].str.contains('engineer', case=False)]))

print("\n-- Find The Email of the person with the following IP Address: 132.207.160.22--\n")
print(df[df['IP Address']=="132.207.160.22"]['Email'])

print("\n--How many People have Mastercard as their Credit Card Provider and made a purchase above 50?--\n")
print(len(df[(df['CC Provider']=='Mastercard') & (df['Purchase Price']>50)]))

print("\n--Find the email of the person with the following Credit Card Number: 4664825258997302--\n")
print(df[df['Credit Card']==4664825258997302]['Email'])

print("\n-- How many people purchase during the AM and how many people purchase during PM?--\n")
print(df['AM or PM'].value_counts())

print("\n--How many people have a credit card that expires in 2020?--\n")
def func():
    count=0
    for date in df['CC Exp Date']:
        if date.split('/')[1]=='20':
            count+=1
    print(count)
func()
#another way
#print(len(df[df['CC Exp Date'].apply(lambda x:x[3:]=='20')]))

print("\n--What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...--\n")
print(df['Email'].apply(lambda x:x.split('@')[1]).value_counts().head())

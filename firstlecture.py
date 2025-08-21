
# print("Hello Duniya...!","    Going to start PYHTON")

# # Assignment operator:
# num =10
# num +=2  #it will add 2 to the already present value in the variable
# print(num)

# # ---------------------
# # Type Conversion--> it performs automatically (means converting one var to another)
# a=2
# b=5.67
# sum=a+b
# print(sum)

# #type casting (We perform it manually)
# """
# x="4"
# y=3
# sum1=x+y             
# print(sum1)    --> it will show us error because we can't add string type to integer value, for this we perform 
#                     type casting 
# """
# x=int("4")
# y=3             #x="4", y=int(x) --> can also do like this
# sum1=x+y
# print(sum1)

# #Taking input from user
# name= input("Enter your name: ")
# age=  int(input("Enter your age: "))    #here we do type casting because input always use string type
# weight= float(input("Enter your weight: "))

# print()
# print("Your name is: ",name)
# print("Your age is: ",age)
# print("Your weight is: ",weight)

#1st Question
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
sum2=num1+num2
print("Sum is =", sum2)

#2nd Question
square=float(input("Enter the side of square :"))
print("Area of square is: ",square**2)

#3rd Question
float1=float(input("Enter first number :"))
float2=float(input("Enter second number :"))
print("Average is: ", (float1+float2)/2)

#4th Question
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
print(a>=b)
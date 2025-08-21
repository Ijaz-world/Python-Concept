#--> OOP concepts

# class Student:
#     name="ijaz"
# s1=Student()
# print(s1.name)

class Car:
    CEO_name="ijaz"    #--> this is called class attribute because this is common thing, all cars have same ceo, so we don't have need to initialize it in self.
    brand="Honda"
      #2 types of constructor we have: default and parameterized
    def __init__(self,color,brand):        #we can create more than one constructor
        self.car_color=color  #car_color will create at this step,,--> this is object attribue because every car have different color and we have to make this every time 
        self.brand=brand      #obj attr have HIGHER precedence than class attr if we have same
        print("Hi,,,,I am constructor")

    def welcome(self):          #this is a method
        print("Hello Customers from: ",self.brand)

c1=Car("Red","Toyota")
print("color: ",c1.car_color,"\nbrand: ",c1.brand)
print("CEO name: ",c1.CEO_name) #can also write print(Car.CEO_name)
c1.welcome()

#practice question
class Student:

    @staticmethod      #--> called decorator
    def welcome():  #this is a static method in which we don't use object attr 
        print("Hello,")

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi,",self.name,",your average is: ",sum/3)
        
s1=Student("ijaz",[78,88,91])
s1.welcome()
s1.avg()
s1.name="ahmad"
s1.avg()

#Exmaple of private attr or methods
class House:
    def __init__(self,owner,price):
        self.__owner=owner        # __(double underscor) make attr private, and we can only access it within this class
        self.price=price

    def allow(self):
        print(self.__owner)

    def __notAllow():
        print("Hi i am private")

h1=House("ijaz",300000)
print(h1.price)
# print(h1.__owner)      --> it will show us error
print(h1.allow())       #--> it will print owner name becasue we use allow() method within class
# print(h1.__notAllow)   --> show us error because we can't access it outside of class
        
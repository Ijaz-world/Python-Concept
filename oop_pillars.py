#Encapsulation
class Demo:
    city="Toba"

    def welcome(self):
        print("Welcome to toba")
obj1=Demo()
obj1.welcome()     #this is simple example of encapsulation in which we wrap data and methods into 1 class

#Abstraction --> means hiding unnecessary details and showing only important thing

class CCar:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True      #we hide details till it because we only want to show user that car has started
        print("Car started")
c1=CCar()
c1.start()

#Inheritance --> using atttributes and methods from one class(parent) to other(child)
class  Car:
    @staticmethod
    def start():
        print("Car has started..")

    @staticmethod
    def Stop():
      print("Car stoppppp...")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

c1=ToyotaCar("Xli")
print(c1.name)
print(c1.start())
print(c1.Stop())

#Multi level inheritance
class  Car:
    @staticmethod
    def start():
        print("Car has started..")

    @staticmethod
    def Stop():
      print("Car stoppppp...")
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type=type
       
c1=Fortuner("Petrol")
c1.start()

#multiple inheritance         -->one class can inherit properties of more than one class
class Ali:
    a="Hi, i am Ali.."
class Ahmad:
    b="Hi, i am ahmad.."
class father(Ali,Ahmad):
    c="Hi, i am father of ali and ahmad.."

obj1=father()
print(obj1.a)
print(obj1.b)
print(obj1.c)

#use of Super()
class  Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car has started..")

    @staticmethod
    def Stop():
      print("Car stoppppp...")
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)      #--> using this super, we can access car class's obj attr

c1=ToyotaCar("fortuner","Petrol")
print(c1.type)

#practice question
print("--practice question--")
class Emoloyee:
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal
    def showdetails(self):
        print("Role: ",self.role)
        print("Department :",self.dep)
        print("Salary :",self.sal)
class Enginner(Emoloyee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Name: ",self.name)
        print("Age :",self.age)
        super().__init__("Engineer","IT","100000")

obj=Enginner("Ijaz",22)
obj.showdetails()

        

        
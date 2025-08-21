#Functions

def avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    #return avg  -->Optional
avg(88,93,96)

#Homework
number=int(input("Enter a number to check for even and odd: "))

def check(num):
    if(num%2==0):
        print("Number is even")
    else:
        print("Number is odd")
    return num
check(number)
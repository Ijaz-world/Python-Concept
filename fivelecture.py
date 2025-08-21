#while looop

a=int(input("Enter a number to get table: "))
 
i=1
while i<=10:
    print(a*i)
    i+=1

print("enddddd")

print("--------------")

list=[1,2,5,7,8,9,3]
a=7
idx=0
while idx<len(list):
    if(a==list[idx]):
        print("Number found at index: ",idx)

    idx+=1

#for loop
nums=[1,3,4,5,9,1,2]
x=1
idx=0
for el in nums:
    if(el==x):
        print("1 found at index: ",idx)
        break
    idx+=1

for i in range(2,10,2):   #(start,stop,step)
    print(i)

for x in range(10,0,-1):
    print(x)

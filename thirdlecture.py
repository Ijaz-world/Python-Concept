# data=["ijaz",21,78,"Toba"]
# print(data)
# print(data[0],data[2])
# print(data[1:3])   #list slicing
# print(len(data))
# data[2]=87         #Replaces 78 with 87 because list is mutable
# print(data)
# data.append("Male")
# print(data)


# num=[21,34,53,11,32]
# print("List of numbers :",num)
# num.insert(1,100)
# print("After inserting 1 more number :",num)
# num.sort()         #num.sort() didn't return anything that's why we don't use directly in print()
# print("After sort in ascending order :",num)
# num.sort(reverse=True)
# print("After sort in descending order :",num)
# num.reverse()
# print("In reverse order :",num)

# list=[1,2,1,4]
# list.remove(1)     #remove 1 where it finds first
# print(list)
# list.pop(0)        #remove element
# print(list)

# print("------Tuple concept-------")
# tup=(2,4,5,4,3,7)
# print(type(tup))
# print(tup[1:4])
# print(tup.index(4))    #return index where it first occurs
# print(tup.count(3))    #just how much times it occur

#1st question

movies=[]

movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))

print("Your favourite movies are :",movies)

#2nd question
list=[2,3,3,2]

copy_list=list.copy()
copy_list.reverse()

if(list == copy_list):
    print("List is Palindrome")
else:
    print("List is not Palindrome")
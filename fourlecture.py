# #Dictionary 

# info={
#     "name": "Ijaz",
#     "age" : 21,
#     "city": "Toba",
#     "uni":  "Numl",
# }
# print(info)
# print(info["name"])
# print(info["city"])

# info["age"]=22
# info["gender"]="Male"  #adding new key

# print("After updating: ",info)

# #we can also create null dictionary using, dict={}
# student={
#     "name": "Ahmad",
#     "subject": {            #Nested dictionary
#         "eng": 89,
#         "sci": 88,
#         "math": 99
#     }
# }
# print(student)
# print(student["subject"]["math"])
# new_student={
#     "name": "Ali"
# }
# student.update(new_student)      #adding new dict to recent dict
# print(student)

# print("--------Set---------")

# my_set={1,2,3,3,3,4,"ijaz","numl","numl"}
# print(my_set)
# print(len(my_set))         
# #we can create empty set using, collection=set() 
# #********Important= Sets are mutable but elements of set are immutable
# collection=set()
# collection.add(1)
# collection.add(1)
# collection.add(2)
# collection.add("ijaz")
# collection.add((2,4,5))
# print(collection)

# print(my_set.union(collection))
# print(my_set.intersection(collection))

#Practice Questions
print("----1st Question-----")
dict={
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}
print(dict)

print("-----2nd Question-------")
set={"python","java","c++","python","javascript","java","python","java","c++","C"}
print(set)
print("Classroooms needed are: ",len(set))

print("-----3rd Question-----")
subjects={}
a=input("Enter marks of Eng: ")
b=input("Enter marks of Urdu: ")
c=input("Enter marks of Phy: ")
subjects.update({"Eng":a})
subjects.update({"Urdu":b})
subjects.update({"Phy":c})
print("Enter marks are: ",subjects)

print("----4 Question-----")
values={9,"9.0"}
print(values)
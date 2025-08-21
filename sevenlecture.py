f=open("try.txt","r")
data=f.read()           #data=f.read(5) --> give us first 5 character including space
print(data) 
print(type(data))
f.close()  #--> good to close file 
# to print line wise we use --> data=f.read(readline) --> give us first line 

f=open("try.txt","a")  #--> if we use w insead of a, it will erase all data of file and then write from scratch
f.write("\n I am studing in NUML university")
f.close()

#There are some modes that we should we know:
#r+ --> open for reading and writing, points at the start of already present data
#w+ --> open for reading and writing, but it truncate the file means erase all data 
#a+ --> open for reading and writing, points at the end of already present data

#--> another syntax to perform I/O
# with open("try.txt","r") as f:
#     data=f.read()
#       print(data)     #--> no need to close file because with automaticallly close the file

import os        #os is a module, means type of code library where functions are written which we have to use

os.remove("sample.txt")
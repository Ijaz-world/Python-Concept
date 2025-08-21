import numpy as np

arr=np.array([1,2,3,4])
print(arr)
print("slicing: ",arr[0:3])
print(type(arr))       #return type means it is numpy array
print("---------")

arr1=np.array([[1,2,3,4],[5,6,7,8]])    #2D array
print(arr1)
print("After slicing: \n",arr1[0:3,0:3])  #give us elements of every array
print("first array elements: ",arr1[0,0:3])
print(arr1[1,2])    # return index-2 element from index-1 array
#now we see attributes of array
print(np.shape(arr1))    # returns number of rows and columns
print(np.size(arr1))     #return size of array
print(arr1.dtype)        # return us data type
print(arr1.ndim)         #return dimensions, in this case return 2 means rows and columns
print("--------")

b=[[10,20,30],[40,50,60]]
a=np.array(b)
print(a)
print(len(a))       #return us 2 means we have 2 elements, its other thing that we have further elements in element means nested
print(a.shape)
print(np.size(a))
print(a.dtype)  # tell us datatype of array
print(a.astype(float)) #will convert datatype from int to float
print(a.astype(str))   #will convert datatype from int to string
print("--------")
arr1=np.array([[10,20],[20,30]])
arr2=np.array([[10,20],[20,30]])
print("addition: \n",np.add(arr1,arr2))             # can also write print(arr1+arr2)
print("subtraction: \n",np.subtract(arr1,arr2))
print("multiplication: \n",np.multiply(arr1,arr2))
print("divison: ",np.divide(arr1,arr2))
print(np.concatenate([arr1,arr2]))
print(np.concatenate([arr1,arr2], axis=1))     #horizontallly
print(np.hstack((arr1,arr2)))  #--> concatenate horizantally same like axis=1
print(np.vstack((arr1,arr2)))  #--> concatenate vertically same like axis=0

print("---------")
aa=np.array([1,2,3,4,5,6,7,8])
# print(np.array_split(aa,3)) --> split our array into 3 arrays
b=np.array_split(aa,3)
print(b[1])
print(np.append(aa,9))
print(np.insert(aa,1,4))    #array, index, value
print(np.delete(aa,2))
# for 2D array, axis=0 means operation will done on horizontally, and axis=1 means operation done on vertically
print("---------")
arr2=np.array([4,7,3,9,8])
print(np.sort(arr2))
print(np.where(arr2 ==9))
#now we see filter concept--> creating new array from existing array
fa=aa>4         # we can set any condition here
new= aa[fa]
print(new)
print(np.sum(aa))
print(np.min(aa))
print(np.max(aa))
print(np.mean(aa))
print(np.std(aa))     #if its less it indicates its good
#we can also find correaltion coefficient between 2 arrays, if output shows positive values it represnets proportional relationship, if negative then it represnets inversely proportional relationship, 0 means no relationship

print("-----Inserting in 2D array:------")
arr_2d=np.array([[1,2],[3,4]])
print(arr_2d)
new_arr_2d=np.insert(arr_2d,1,[5,6], axis=0)      #axis=0 --> row wise operation
print(new_arr_2d)                                 #axis=1 --> column wise operation
new1_arr_2d=np.insert(arr_2d,1,[5,6], axis=1)
print(new1_arr_2d)

print("---------")
missing_arr=np.array([1,2,np.nan,4,5,np.nan,7])
print(np.isnan(missing_arr))
clean_arr=np.nan_to_num(missing_arr,nan=44)
print(clean_arr)
print("---Infinite values---")
inf_arr=np.array([1,2,np.inf,4,5,-np.inf,7,8])
print(np.isinf(inf_arr))
noinf_arr=np.nan_to_num(inf_arr, posinf=100,neginf=-100)
print(noinf_arr)
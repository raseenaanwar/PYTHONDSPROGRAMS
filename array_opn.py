from array import *
arr1=array('i',[1,2,3,4,5,6])
for i in range(0,len(arr1)):
    print(arr1[i])

#append new elemnt at the end of teh array
n=int(input("Enter item"))
arr1.append(n)
print(arr1)

#reverse the oredr of the items
arr1.reverse()
print(arr1)
print(arr1.buffer_info())
print("total size=: ",arr1.buffer_info()[1]*arr1.itemsize)




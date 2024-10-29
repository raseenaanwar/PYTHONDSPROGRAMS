from array import *
n=int(input("size "))
list1=[int(input("")) for i in range(n)]
arr1=array('i',list1)
list2=[int(input("")) for i in range(n)]
arr1.extend(list2)
print(arr1)

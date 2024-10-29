from array import *
n=int(input("enter size"))
list1=[int(input()) for x in range(n)]
arr2=array('i',list1)
r_no=int(input("Enter the no to remove"))
#SPECIFIED NO
arr2.remove(r_no)
print(arr2)
#SPECIFIED INDEX
arr2.pop(1)
print(arr2)

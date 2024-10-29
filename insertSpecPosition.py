from array import *
n=int(input("sizr "))
list1=[int(input()) for i in range(n)]
arr1=array('i',list1)
no=int(input("enter the no"))
pos=int(input("Enter Posin"))
arr1.insert(pos,no)
print(arr1)

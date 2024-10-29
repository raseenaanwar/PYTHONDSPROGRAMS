# Write a Python program to find out if a given array of integers contains any duplicate elements.
# Return true if any value appears at least twice in the array, and return false if every element is distinct.
from array import *
n=int(input("Enter size"))
list1=[int(input()) for i in range(n)]
arr1=array('i',list1)
set1=set(arr1)
if(len(set1)!=len(arr1)):
    print("False")
else:
    print("True")


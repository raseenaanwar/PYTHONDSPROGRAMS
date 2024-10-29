from array import *
def check(arr1,size):
    for i in range(size-1):
        for j in range(i+1,size):
             if(arr1[i]==arr1[j]):
                    return arr1[i]
    return -1
size=int(input("Enter size "))
list1=[int(input()) for i in range(size)]
arr1=array('i',list1)
print(check(arr1,size))


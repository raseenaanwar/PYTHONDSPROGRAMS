from array import *
#pgm to find no_of occurence each item in an array
n=int(input("enter size"))
list1=[int(input()) for x in range(n)]
arr2=array('i',list1)
flag=-1
for i in range(n-1):
    count=1
    for j in range(i+1,n):
        if(arr2[i]==arr2[j]):
            count+=1
            arr2[j]=flag
    if(arr2[i]!=flag):
        print(f"{arr2[i]} repeats {count} times")

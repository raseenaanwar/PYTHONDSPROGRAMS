import numpy as np
def binarysearch(a,low,high,num):
    if low<=high:
        mid=(low+high)//2
        if a[mid]==num:
            return mid
        elif num<a[mid]:
            return binarysearch(a,low,mid-1,num)
        elif num>a[mid]:
            return binarysearch(a,mid+1,high,num)
    else:
            return -1

size=int(input("size"))
list1=[int(input()) for i in range(size)]
a=np.array(list1)
num=int(input("Enter serac"))
p=binarysearch(a,0,size-1,num)
if(p==-1):
    print("Not found")
else:
    print(f"found at {p+1}")


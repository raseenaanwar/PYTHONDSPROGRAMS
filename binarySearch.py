import numpy as np
def binarySearch(arr1,size1,no):
    l,r=0,size1-1
    while l<=r:
        mid=(l+r)//2
        if no==arr1[mid]:
            return mid
        elif no<arr1[mid]:
            r=mid-1
        else:
            l=mid+1
    return -1

size=int(input("Enter size of the array"))
list_elmn=[]
list_elmn=[int(input(f"Enter elmns at {i+1} position")) for i in range(size)]
arr=np.array(list_elmn)
no=int(input("Enter the elemnt to search"))
pos=binarySearch(arr,size,no)
if(pos!=-1):
    print(f"{no} found at position {pos+1}")
else:
    print(f"{no} not found in the array")

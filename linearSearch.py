import numpy as np
def linearSearch(arr,size,no):
    for i in range(size):
        if no==arr[i]:
            return i
    return -1

size=int(input("Enter size of the array"))
list_elmn=[]
for i in range(size):
    array_elm=int(input(f"Enter elmns at {i+1} position"))
    list_elmn.append(array_elm)
arr=np.array(list_elmn)
no=int(input("Enter the elemnt to search"))
pos=linearSearch(arr,size,no)
if(pos!=-1):
    print(f"{no} found at position {pos+1}")
else:
    print(f"{no} not found in the array")





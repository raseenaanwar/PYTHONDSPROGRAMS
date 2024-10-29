import  numpy as np
def insertItem(arr,size,elmn,pos):
    arr1=np.concatenate((arr[:pos],[elmn],arr[pos:]))
    return arr1
size=int(input("Enter size of the array"))
list_elmn=[]
for i in range(size):
    array_elm=int(input(f"Enter elmns at {i+1} position"))
    list_elmn.append(array_elm)
arr=np.array(list_elmn)
no=int(input("Enter the elemnt to insert"))
pos=int(input("Enter the pos to insert"))
arr1=insertItem(arr,size,no,pos)
print(arr1)

import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
l=len(a)
print(a)
for i in range(l//2):
    a[i],a[l-i-1]=a[l-i-1],a[i]
print(a)

def revArray(a):
    if len(a)==1:
        return a
    return revArray(a[1:])+[a[0]]

list1=[1,2,3,4,5,6,7,8,9]
print(revArray(list1))

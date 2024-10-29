from array import *
size=int(input("Enter size: "))
list1=[int(input()) for i in range(size)]
a=array('i',list1)
l=a[0]
sl=a[1]
for i in range(size-1):
    for j in range(i+1,size):
        if (a[i]*a[j])>(l*sl):
            l,sl=a[i],a[j]
print(f"{l}*{sl}={l*sl}")

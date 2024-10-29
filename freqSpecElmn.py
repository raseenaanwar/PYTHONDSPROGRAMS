import math
from array import *
from cmath import sqrt


# n=int(input("enter size"))
# list1=[int(input()) for x in range(n)]
# arr2=array('i',list1)
# # for i in range(n):
# #     print(f"{arr2[i]} {arr2.count(i)}")
# s=int(input("Enter the elmnt to check freq"))
# print(f"{s} repeats {arr2.count(s)}")
def isPrime(i):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            return 0
    return 1
p=int(input("Enter size"))
sum=0
list1=[int(input() for i in range(p))]
primelist=[]
for i in list1:
    if isPrime(i):
        primelist.append(i)

print(primelist)
# for i in range(p):
#     sum=sum+i
# print(f"sum of numbers from 0 to {i} is {sum}")

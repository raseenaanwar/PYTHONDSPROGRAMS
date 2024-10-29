import math

def isPrime(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1

print("Enter the number")
p=int(input())
if(isPrime(p)):
    print("Prime")
else:
    print("Not")



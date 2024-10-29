import sys
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input("Enter the no"))
print("factorial=",fact(n))
print(sys.getrecursionlimit())

#fibinocci

def fibinRecursion(no):
    if no<=1:
        return no
    else:
        return fibinRecursion(no-1)+fibinRecursion(no-2)
print("***REc****")

print(fibinRecursion(10))

print("***ITEra*****")
def fibin(n):
    seq=[0,1]
    for i in range(n):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

print(fibin(10))



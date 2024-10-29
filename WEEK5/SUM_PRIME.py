def sum_of_prime(list1,n):
    sum_prime=0
    for num in list1:
        if is_prime(num):
            sum_prime+=num
    return sum_prime
def is_prime(num):

    if num<=1:
        return 0
    for i in range(2,(num//2)+1):
        if num%i==0:
            return 0
    print(num)
    return 1
n=int(input("enter size"))
list1=[int(input("Enter numbers")) for i in range(n)]
print(sum_of_prime(list1,n))

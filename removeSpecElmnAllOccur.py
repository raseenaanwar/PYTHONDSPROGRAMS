def delno(list1,no):
    list1=[x for x in list1 if no!=x]
    return list1
n=int(input("Enter size "))
list1=[int(input()) for i in range(n)]
no=int(input("Enter the item which need to delete"))
list1=delno(list1,no)
print(list1)
print(len(list1))

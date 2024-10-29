# n=int(input("Enter size"))
# list1=[int(input(f"Enter {i}th element")) for i in range(n)]
# elmnt=int(input("Enter elmnt tp move to the last position"))
# lst_repeated_elm=[x for x in list1 if x==elmnt]
# lst=[x for x in list1 if x!=elmnt]
# lst.extend(lst_repeated_elm)
# print(lst)
# #print unique elmns
# n=int(input("Enter size"))
# list1=[int(input(f"Enter {i}th element")) for i in range(n)]
# set1=set(list1)
# print(set1)
#to remove all duplicate elmns
list1=[0,2,3,1,2,3,8,5,0]
set1=set(list1)
print("n",set1)

for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            list1.pop(i)
            i-=1

print(list1)


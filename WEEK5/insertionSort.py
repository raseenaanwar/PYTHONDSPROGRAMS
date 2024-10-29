def insertion_sort(list1):
    for i in range(1,len(list1)):
        num_to_sort=list1[i]
        pos=i
        while list1[pos-1]>num_to_sort and pos>0:
            list1[pos]=list1[pos-1]
            pos-=1
        list1[pos]=num_to_sort
        print(list1[pos])
    return list1

n=int(input("Enter size of the list"))
print("Enter elmns in the list")
list1=[int(input()) for i in range(n)]
print(insertion_sort(list1))

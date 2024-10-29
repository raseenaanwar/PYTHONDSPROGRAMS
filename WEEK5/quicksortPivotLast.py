def find_pivot_place(list1,first,last):
    pivot=list1[last]
    left,right=first,last-1
    while True:
        while left<=right and list1[left]>=pivot:
            left+=1
        while left<=right and list1[right]<=pivot:
            right-=1
        if right<left:
           break
        else:
            list1[left],list1[right]=list1[right],list1[left]
    list1[last],list1[left]=list1[left],list1[last]
    return left

def quicksort(list1,first,last):
    if first<last:
        pivot_index=find_pivot_place(list1,first,last)
        quicksort(list1,first,pivot_index-1)
        quicksort(list1,pivot_index+1,last)

n=int(input("Enter size "))
print("Enter the elments")
list1=[int(input()) for i in range(n)]
quicksort(list1,0,n-1)
print("SORTED ARRAY IS")
print(list1)

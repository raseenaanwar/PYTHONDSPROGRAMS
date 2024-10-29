
import statistics
def find_pivot_place(list1,first,last):
    low=list1[first]
    high=list1[last]
    mid=(first+last)//2
    pivot_val=statistics.median([low,list1[mid],high])
    # print("med",pivot_val)
    if pivot_val==low:
        pindex=first
    elif pivot_val==high:
        pindex=last
    else:
        pindex=mid
    list1[last],list1[pindex]=list1[pindex],list1[last]
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

# def bubbleSort(arr1,size):
#
#     for i in range(size):
#         swapped=False
#         for j in range(size-i-1):
#             if(arr1[j]>arr1[j+1]):
#                 arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
#                 swapped=True
#         if swapped is False:
#             break
# size=int(input("Enter the size of the array"))
# print(f"Enter {size} elments to the arry")
# arr1=[int(input()) for i in range(size)]
# bubbleSort(arr1,size)
# print(arr1)

def bubble_sort(arr):
    n=len(arr)
    swapped_flag=False
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped_flag=True
        if swapped_flag is False:
            break
numbers=[43,21,11,34,22]
bubble_sort(numbers)
print("sorted list",numbers)

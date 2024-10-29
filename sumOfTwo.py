import numpy as np
def twoSum(nums, target):
    dict1 = {}
    for i, num in enumerate(nums):
        c= target - num
        # print(complement)
        if c in dict1:
            return [dict1[c], i]
        dict1[num] = i
    return []
size=int(input("Enter size of the array"))
listelm=[int(input()) for i in range(size)]
arr=np.array(listelm)
target=int(input("Enter the target : "))
print(twoSum(arr,target))

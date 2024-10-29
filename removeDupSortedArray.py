l=int(input("Enter size "))
nums=[int(input()) for i in range(l)]
l=len(nums)
for i in range(l-2,-1,-1):
    print(nums[i])
    if nums[i]==nums[i+1]:
        nums.pop(i+1)

print(nums)

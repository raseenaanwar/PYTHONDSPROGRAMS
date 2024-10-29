nums=[2,2,8,5,-88,7,-5,]
value=2
list2=[]
for i in range(len(nums)):
    if i!=value:
        list2.append(i)
print(len(list2))

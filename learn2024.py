# bubblie sort stable algm inplace algm o(n2) complexity
list1=[2,1,8,7,11,3]
for i in range(len(list1)):
    swapped=False
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            swapped=True
    if swapped is False:
        break
print(list1)

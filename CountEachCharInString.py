str1="Hellohgygu8u832hhh"
dict1={}
max_count=0
for char in str1:
    keys=dict1.keys()
    if char in keys:
        dict1[char]+=1
    else:
        dict1[char]=1
list1=[]
count=max(dict1.values())
for keys,values in dict1.items():
    if values==count:
        list1.append(keys)

# print(max(dict1.values()))
print(dict1)
print(f"{list1} repeats {count} times")

# def remove_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     result=""
#     for char in input_string:
#         if char not in vowels:
#             result+=char
#     # result = ''.join([char for char in input_string if char not in vowels])
#     return result
# input_str = "Hello, World!"
# output_str = remove_vowels(input_str)
# print(output_str)  # Hll, Wrld!
nums=[[1,2,3],[4,5,6],[5,62,1]]
outerlist=[]
innerlist=[]
for i in range(len(nums)-1,-1,-1):
    outerlist.append(nums[i])
    innerlist.append(nums[i][::-1])
print(outerlist)
print(innerlist)

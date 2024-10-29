str1="HelloHaihHH"
# new_string=ch=str1[0]
# for i in range(1,len(str1)):
#     if str1[i]==ch:
#         new_string+='$'
#     else:
#         new_string+=str1[i]
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]
print(str1)
a="xyz"
b="abc"
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print(new_a + ' ' + new_b)

# print(new_string)

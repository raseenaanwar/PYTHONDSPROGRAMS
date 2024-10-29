#Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged
str1="hai how are you"
if(len(str1)>=3):
    ch=str1[-2:]
    if(ch=='ing'):
        str1.replace('ing','ly')
    else:
        str1+='ing'
print(str1)
#Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
#If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
str1='she is not  bcbjbd poor'
s1=str1.find('not')
s2=str1.find('poor')
if(s2>s1):
    str1=str1[:s1]+str1[s2+4:]+'good'
print("String is ",str1)

# Write a Python function that takes a list of words
# and return the longest word and the length of the longest one.
n=int(input("Enter size "))
list1=[input() for i in range(n)]
max_len=0
for world in list1:
    if len(world)>max_len:
        max_len=len(world)
        max_str=world
print("string with max length is ",max_str,' with ',max_len)

#Write a Python program to remove the nth index character from a nonempty string.
def removeChar(str1,n):
    firstpart=str1[:n]
    second=str1[n+1:]
    return firstpart+second


str1="hellokfdfkdf"
n=int(input("Enter the position of the character to remove"))
print(removeChar(str1,n))
print("String after removing the characterr", str1[-1:]+str1[1:-1]+str1[:1])

#Write a Python program to count the occurrences of each word in a given sentence.

str1="I love my country, all indian are my brothers and sisters i love my country"
dict1={}
words=str1.split()
print(type(words))
words.sort()
print("words in the sentence are")
print(words)
for word in words:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1

print(dict1)

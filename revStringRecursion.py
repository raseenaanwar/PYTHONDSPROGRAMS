def stringRev(str1):
    if(len(str1)==1):
        return str1
    else:
        return stringRev(str1[1:])+str1[0]

str1=input("Enter the string ")
print(stringRev(str1))

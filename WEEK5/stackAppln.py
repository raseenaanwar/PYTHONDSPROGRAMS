# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid(str):
    stack=[]
    for char in str:
        if char not in ')]}':

            stack.append(char)
        elif stack:
            open_char=stack.pop()
            if(open_char=='(' and char!=')') or (open_char=='[' and char!=']') or(open_char=='{' and char!='}'):
                return False
        else:
            return False

    return False if stack else True

str=input("Enter the Characters")
print(isValid(str))

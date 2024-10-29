def delMidStack(stack):
    l=len(stack)
    mid=l//2
    temp_stack=[]
    for i in range(mid):
        temp_stack.append(stack.pop())

    stack.pop()
    while temp_stack:
        stack.append(temp_stack.pop())
def reversestack(stack):
    temp=[]
    while stack:
        temp.append(stack.pop())
    print(temp)

def delNode(list1,number):
    temp_stack=[]
    flag=0
    for item in list1:
        if item==number:
            flag=1
        if flag!=1:
            temp_stack.append(item)
        print(item)
    while temp_stack:
        list1.append(temp_stack.pop())
    return list1





def sort_stack(stack):
    temp_stack = []

    while stack:
        # Remove the top element from the original stack
        element = stack.pop()

        # Move elements from the temporary stack back to the original stack
        while temp_stack and temp_stack[-1] > element:
            stack.append(temp_stack.pop())

        # Push the current element onto the temporary stack
        temp_stack.append(element)

    return temp_stack[::-1]  # Return the sorted stack in ascending order


list1=[10,20,30,40,11,22,33]
delMidStack(list1)
print(list1)
reversestack(list1)
print(delNode(list1,11))


def stack_push(data):
    stack.append(data)
def stack_pop():
    if(check_empty()!=True):
        return stack.pop()
    else:
        print("Stack is empty")
def check_empty():
    if len(stack)==0:
        return True
def print_top():
    if(check_empty()!=True):
        return stack[-1]
    else:
        print("Stack is empty")

def print_stack():
    if(check_empty()!=True):
        for i in stack:
            print(i)
    else:
        print("Stack is empty")
def sortStack(stack):
    tempStack=[]
    while stack:
        topInputStack=stack.pop()
        while tempStack and tempStack[-1]>topInputStack:
            toptempstack=tempStack.pop()
            stack.append(toptempstack)
        tempStack.append(topInputStack)
    return tempStack

stack=[]
stack_push(20)
stack_push(30)
stack_push(110)
stack_push(220)
# stack_push(10)
print("Elemts in the stack are")
print_stack()
print("popped elemnt is ",stack_pop())
print("Top elmn is ",print_top())
print(sortStack(stack))

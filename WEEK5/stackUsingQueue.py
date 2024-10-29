from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if self.stack:
            return self.stack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
    def printStack(self):
        print(self.stack)

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.printStack()
print("popped ",s1.pop())
s1.printStack()
print("top",s1.top())

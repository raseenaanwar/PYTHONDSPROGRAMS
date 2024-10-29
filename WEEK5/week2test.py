class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.head=None

    def push(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head=node
    def pop(self):
        if self.head is None:
            print("Stack empty")
            return
        p=self.head.data
        self.head=self.head.next
        return p

    def printStack(self):
        if self.head is None:
            print("Stack is Empty ")
            return
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next



s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Elmns in the stack are")
s1.printStack()
print(f"popped item is {s1.pop()}")
print("Elmns in the stack are")
s1.printStack()

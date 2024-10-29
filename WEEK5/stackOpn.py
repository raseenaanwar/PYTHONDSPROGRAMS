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
            print("Stack is Empty")
            return
        removed_node=self.head.data
        self.head=self.head.next
        return removed_node

    def print_stack(self):
        if self.head is None:
            print("Stack Empty")
        else:
            current=self.head
            while current is not None:
                print(current.data,end=" ")
                current=current.next
            print()
    def peekStack(self):
        if self.head is None:
            print("Stack is empty")
        else:
            print("Top elmnet is ",self.head.data)

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(100)
s1.push(200)
s1.print_stack()
print(f"popped elmnt is {s1.pop()}")
print("Elements in stack are")
s1.print_stack()
s1.peekStack()
l

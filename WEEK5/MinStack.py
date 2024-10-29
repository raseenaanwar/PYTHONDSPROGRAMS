class Node:
    def __init__(self,data,mini=None,maxi=None):
        self.data=data
        self.next=None
        self.min=mini
        self.max=maxi
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            node=Node(data,mini=data,maxi=data)
            self.head=node
        else:
            node=Node(data,mini=min(data,self.head.min),maxi=max(data,self.head.max))
            node.next=self.head
            self.head=node
    def pop(self):
        if self.head is None:
            print("Stack empty")
            return
        else:
            p=self.head
            self.head=self.head.next
        return p.data
    def top(self):
        if self.head is not None:
            return self.head.data
    def getMin(self):
        return self.head.min
    def print_stack(self):
        c=self.head
        while c is not None:
            print(c.data,end=" ")
            c=c.next
        print( )
    def getMax(self):
        return self.head.max




s1=Stack()
s1.push(10)
s1.push(20)
s1.push(5)
s1.push(3)
s1.push(12)
print("Elmns in stack are")
s1.print_stack()
print("min=",s1.getMin())
print("popped item is " ,s1.pop())
s1.print_stack()
print("top= ",s1.top())
print("Max =",s1.getMax())

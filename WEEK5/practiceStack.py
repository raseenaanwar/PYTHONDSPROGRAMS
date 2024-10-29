class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.count=0

    def push(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.count+=1
        else:
            node.next=self.head
            self.head=node
            self.count+=1

    def pop(self):
        if self.head is None:
            print("Stack Empty ")
        else:
            print("Popped item is ",self.head.data)
            self.head=self.head.next

    def peek(self):
        if self.head is None:
            print("Stack Empty ")
        else:
            print("Top item is",self.head.data)

    def printStack(self):
        if self.head is None:
            print("Stack Empty ")
        else:
            current=self.head
            while current is not None:
                print(current.data,end=" ")
                current=current.next
            print()


    def middleStack(self):
        sptr=self.head
        fptr=self.head
        while fptr is not None and sptr is not None:
            r=sptr
            sptr=sptr.next
            fptr=fptr.next.next if fptr is not None and fptr.next is not None else None
        return r.data

    def printCount(self):
        print("Size ",self.count)





s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
print("Elmns in stack are")
s1.printStack()
s1.pop()
s1.printStack()
s1.peek()
print("middle elemnt is ",s1.middleStack())
s1.printCount()

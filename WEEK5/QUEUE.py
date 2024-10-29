class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=self.rear=None

    def EnQueue(self,data):
        node=Node(data)
        if self.rear is None:
            self.front=self.rear=node
            return
        self.rear.next=node
        self.rear=self.rear.next

    def DeQueue(self):
        if self.front is None:
            print("Queue is Empty")
            return
        t=self.front.data
        self.front=self.front.next
        return t
    def IsEmpty(self):
        return self.front is None
    def size(self):
        count=0
        current=self.front
        while current is not None:
            count+=1
            current=current.next
        return count
    def printFront(self):
        return self.front.data
    def printRear(self):
        if self.rear is not None:
            return self.rear.data

    def printQueue(self):
        if self.front is None:
            print("Queue is empty")
            return
        current=self.front
        while current is not None:
            print(current.data,end=' ')
            current=current.next
        print()
    def midQueue(self):

q1=Queue()
q1.EnQueue(10)
q1.EnQueue(20)
print('the elmns in the queue are')
q1.printQueue()
print("The Rear elmnt is ",q1.printRear())
q1.EnQueue(100)
q1.EnQueue(200)
print('the elmns in the queue are')
q1.printQueue()
print('size of queue is ',q1.size())
print("removed elmns is",q1.DeQueue())
q1.printQueue()

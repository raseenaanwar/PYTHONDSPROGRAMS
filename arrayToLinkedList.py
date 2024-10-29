class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,list1):
        self.head=Node(list1[0])
        n=self.head
        for x in list1[1:]:
            n.next=Node(x)
            n=n.next

list1=[10,20,30,40,50]
l1=LinkedList(list1)
n=l1.head
while n is not None:
    print(n.data,"-->",end=" ")
    n=n.next

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def insert_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def insert_before(self,before,data):
        current=self.head
        f=False
        while current.next:
            if current.next.data==before:
                f=True
                break
            else:
                current=current.next
        if f:
            new_node=Node(data)
            new_node.next=current.next
            current.next=new_node
        else:
            print()
            print(f" {before} is not in thle ll")

    def insert_after(self,after,data):
        current=self.head
        f=False
        while current.next:
            if current.data==after:
                f=True
                break
            current=current.next
        if f:
            new_node=Node(data)
            new_node.next=current.next
            current.next=new_node
        else:
            print(f"{after} is not in LL")



    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False
    def search_recursive(self,current,data):
        if not current:
            return False
        if current.data==data:
            return True
        return self.search_recursive(current.next,data)
    def printitems(self):
        print()
        if self.head is None:
            print("ll is empty")
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
ll=LL()
ll.insert_start(5)
ll.insert_start(4)
ll.insert_end(99)
ll.printitems()
print()
ll.insert_before(5,100)
ll.printitems()
ll.insert_after(5,1)
ll.printitems()
if ll.search(99):
    print(" found")
else:
    print("not")
print()
if ll.search_recursive(ll.head,123):
    print("found rec")
else:
    print("not")

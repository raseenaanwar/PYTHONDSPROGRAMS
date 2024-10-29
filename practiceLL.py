class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def insert_if_empty(self,data):
        if self.head is  not None:
            print("LL is  not Empty")
        else:
            node=Node(data)
            self.head=node

    def print_list(self):
        if self.head is None:
            print("LL is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data,"-->",end=" ")
                current=current.next

    def insert_at_begin(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=node

    def insert_at_after(self,data,after_no):
        current=self.head
        if current is None:
            print("Linked List is Empty")
            return
        while current is not None:
            if current.data==after_no:
                break
            current=current.next
        if current is None:
            print(f"Node {after_no} is not present in the linked list")
            return
        node=Node(data)
        node.next=current.next
        current.next=node

    def insert_at_befor(self,data,before_no):
        current=self.head
        if current is None:
            print("Linked list Empty")
            return
        if current.data==before_no:
            node=Node(data)
            node.next=current
            self.head=node
            return
        while current.next is not None:
                if current.next.data==before_no:
                    break
                current=current.next
        if current.next is None:
            print("Node is not in LL")
            return
        node=Node(data)
        node.next=current.next
        current.next=node

    def delete_at_begin(self):
        current=self.head
        if current is not None:
            self.head=current.next
        else:
            print("No elmnt to delete")
    def delete_at_end(self):
        current=self.head
        if current is None:
            print("Empty")
        elif current.next is None:
            self.head=None
        else:

            while current.next.next is not None:
                current=current.next
            current.next=None

    def delete_any(self,num):
        current=self.head
        if current is None:
            print("LL is empty")
            return
        if current.data==num:
            self.head=None
            return
        while current.next is  not None:
            if current.next.data==num:
                break
            current=current.next
        if current.next is None:
            print("The number is not in the list")
        else:
            current.next=current.next.next

    def print_rev(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev



l1=LL()
l1.insert_if_empty(10)
l1.insert_at_begin(20)
l1.insert_at_begin(30)
l1.insert_at_end(40)
l1.insert_at_end(60)
l1.insert_at_after(88,20)
l1.insert_at_after(99,30)

l1.insert_at_befor(110,40)
l1.delete_at_begin()
l1.delete_at_begin()
l1.delete_at_end()
l1.insert_at_end(76)
l1.delete_at_end()

print()
l1.delete_any(880)
l1.print_list()
print()
l1.print_rev()
l1.print_list()
print()
l1.insert_at_end(300)
l1.print_list()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None

    def print_node(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.next
            print()
    def insert_at_begin(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=node
    def insert_at_after(self,data,x):
        n=self.head
        node=Node(data)
        while n.next is not None:
            if n.data==x:
                break
            n=n.next
        node.next=n.next
        n.next=node


    def insert_at_before(self,data,x):
        n=self.head
        if n is None:
            print("Linked list is Empty")
            return
        node=Node(data)
        if n.data==x:
            node.next=self.head
            self.head=node
            return
        while n.next is not None:
            if n.next.data==x:
                break
            n=n.next
        if n.next is None:
            print("The Node is not in the Linked lIst")
        else:
            node.next=n.next
            n.next=node

    def insert_empty(self,data):
        if self.head is None:
            node=Node(data)
            self.head=node
        else:
            print("Linked List not Empty")
    def delete_at_begin(self):
        n=self.head
        if n is not None:
            self.head=self.head.next
    def delete_at_end(self):
        n=self.head
        if n is None:
            print("Empty")
        elif n.next is None:
            self.head=None
        else:
            while n.next.next is not None:
                n=n.next
            n.next=None
    def delete_any(self,data):
        n=self.head
        if n is None:
            print("Lilnked List is empty")
            return
        if n.data==data:
            self.head=self.head.next
            return
        while n.next is not None:
            if data==n.next.data:
                break
            n=n.next
        if n.next is None:
            print("Node is absent")
        else:
            n.next=n.next.next


    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=node
    def print_reverse(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def removeDuplicates(self):
        current=self.head
        if current is None:
            print("Ll is empty")
        else:
            list1=[]
            while current.next is not None:
                if current.next.data not in list1:
                    list1.append(current.data)
                    current=current.next
                else:
                    current.next=current.next.next

    def find_middle_node(self):
        if self.head is None:
            print("EMpty")
            return
        s_ptr=self.head
        f_ptr=self.head
        while f_ptr is not None and s_ptr is not None:
            r=s_ptr
            s_ptr=s_ptr.next
            f_ptr=f_ptr.next.next if f_ptr.next is not None else None
        return r
    def is_palin(self):
        list1=[]
        current=self.head
        while current is not None:
            list1.append(current.data)
            current=current.next
        left=0
        right=len(list1)-1
        while left<right:
            if list1[left]!=list1[right]:
                return False
            left+=1
            right-=1
        return True

    def deleteoddposition(self):
        if self.head is None:
            print("Empty")
            return
        current=self.head
        prev=None
        count=1
        while current is not None:
            if count%2!=0:
                if current==self.head:
                    self.head=current.next
                    current=self.head
                else:
                    prev.next=current.next
                    current=prev.next
            else:
                prev=current
                current=current.next
            count+=1

l=LinkedList()
# l.insert_empty(2)
# l.print_node()
# l.insert_at_begin(1)
# l.print_node()
# l.insert_at_end(1)
# l.print_node()
# l.insert_at_after(20,20)
# # l.print_node()
# l.insert_at_before(30,20)
# l.print_node()
l.insert_at_end(30)
l.insert_at_end(23)
l.insert_at_end(34)
l.insert_at_end(30)
l.insert_at_end(20)
print("jjj")
l.print_node()
print("after dup")
l.removeDuplicates()
l.print_node()
# l.insert_at_end(200)
# l.insert_at_end(300)
k=l.find_middle_node()
print("MId")
l.print_node()
# print("mid",k.data)
# if l.is_palin():
#     print("The linked lsit palindrome")
# else:
#     print("Not")
# l.insert_at_end(5)
# l.insert_at_end(6)
# l.insert_at_end(7)
# l.insert_at_end(8)
# l.print_node()
# l.deleteoddposition()
# l.print_node()

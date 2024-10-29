class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None
    def add_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        current=self.head
        while current is not None:
            current=current.next
        current.next=node

        def binarySearch(a,low,high,num):
            if(low<=high):
                mid=(low+high)//2
                if(a[mid]==num):
                    return mid
                elif(num<a[mid]):
                    return(binarySearch(a,low,mid-1,num))
                elif(num>a[mid]):
                    return(binarySearch(a,mid+1,high,num))
                else:
                    return -1

        def revArray(a):
             if len(a)==1:
                 return a
             else:
                 return(revArray(a[1:]))+a[0]

        list1=[1,2,3,4,5,6]
        print(revArray(list1))








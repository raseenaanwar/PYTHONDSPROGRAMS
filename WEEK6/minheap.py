class MinHeap:
    def __init__(self,capacity):
        self.heap=[0]*capacity
        self.capacity=capacity
        self.size=0

    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftChildIndex(self,index):
        return 2*index+1
    def getRightChildIndex(self,index):
        return 2*index+2
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size
    def parent(self,index):
        return self.heap[self.getParentIndex(index)]
    def leftChild(self,index):
        return self.heap[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.heap[self.getRightChildIndex(index)]
    def isFull(self):
        return self.size==self.capacity
    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]
    def insert(self,data):
        if self.isFull():
            raise (" Full")
        self.heap[self.size]=data
        self.size+=1
        self.heapifyUp(self.size-1)
    def heapifyUp(self,index):
        if self.hasParent(index) and self.parent(index)>self.heap[index]:
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))
    def printHeap(self):
        print(self.heap)
    def removeMin(self):
        if self.size==0:
            raise ("Empty")
        data=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self.heapifyDown(0)
        return data
    def heapifyDown(self,index):
        smallest=index
        if self.hasLeftChild(index) and self.heap[smallest]>self.leftChild(index):
            smallest=self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.heap[smallest]>self.rightChild(index):
            smallest=self.getRightChildIndex(index)
        if smallest!=index:
            self.swap(index,smallest)
            self.heapifyDown(smallest)

m1=MinHeap(10)
m1.insert(34)
m1.insert(10)
m1.insert(20)
m1.insert(66)
m1.insert(20)
m1.insert(5)
m1.printHeap()
# m1.removeMin()
m1.printHeap()

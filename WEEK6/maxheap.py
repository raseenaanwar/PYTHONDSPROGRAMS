# class MaxHeap:
#     def __init__(self,capacity):
#         self.heap=[0]*capacity
#         self.capacity=capacity
#         self.size=0
#
#     def getParentIndex(self,index):
#         return (index-1)//2
#     def getLeftChildIndex(self,index):
#         return 2*index+1
#     def getRightChildIndex(self,index):
#         return 2*index+2
#     def hasParent(self,index):
#         return self.getParentIndex(index)>=0
#     def hasLeftChild(self,index):
#         return self.getLeftChildIndex(index)<self.size
#     def hasRightChild(self,index):
#         return self.getRightChildIndex(index)<self.size
#     def parent(self,index):
#         return self.heap[self.getParentIndex(index)]
#     def leftChild(self,index):
#         return self.heap[self.getLeftChildIndex(index)]
#     def rightChild(self,index):
#         return self.heap[self.getRightChildIndex(index)]
#     def isFull(self):
#         return self.size==self.capacity
#     def swap(self,index1,index2):
#         self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]
#     def insert(self,data):
#         if self.isFull():
#             raise (" Full")
#         self.heap[self.size]=data
#         self.size+=1
#         self.heapifyUp(self.size-1)
#     def heapifyUp(self,index):
#         if self.hasParent(index) and self.parent(index)<self.heap[index]:
#             self.swap(self.getParentIndex(index),index)
#             self.heapifyUp(self.getParentIndex(index))
#     def printHeap(self):
#         print(self.heap)
#     def removeMin(self):
#         if self.size==0:
#             raise ("Empty")
#         data=self.heap[0]
#         self.heap[0]=self.heap[self.size-1]
#         self.size-=1
#         self.heapifyDown(0)
#         return data
#     def heapifyDown(self,index):
#         largest=index
#         if self.hasLeftChild(index) and self.heap[largest]<self.leftChild(index):
#             largest=self.getLeftChildIndex(index)
#         if self.hasRightChild(index) and self.heap[largest]<self.rightChild(index):
#             largest=self.getRightChildIndex(index)
#         if largest!=index:
#             self.swap(index,largest)
#             self.heapifyDown(largest)
#
# m1=MaxHeap(10)
# m1.insert(34)
# m1.insert(10)
# m1.insert(20)
# m1.insert(66)
# m1.insert(90)
# m1.insert(5)
# m1.printHeap()
# # print("max= " ,m1.removeMin())
# # m1.printHeap()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
class MaxHeap:
    def __init__(self, capacity):
        self.heap = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def insert(self, data):
        if self.isFull():
            raise Exception("Heap is full")
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def removeMax(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return max_value

    def heapifyUp(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self.swap(parent_index, index)
                index = parent_index
            else:
                break

    def heapifyDown(self, index):
        while index < self.size:
            largest = index
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            if left_index < self.size and self.heap[left_index] > self.heap[largest]:
                largest = left_index
            if right_index < self.size and self.heap[right_index] > self.heap[largest]:
                largest = right_index

            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def printHeap(self):
        print(self.heap[:self.size])

# Example usage
m1 = MaxHeap(10)
m1.insert(34)
m1.insert(10)
m1.insert(20)
m1.insert(66)
m1.insert(90)
m1.insert(5)
m1.printHeap()
m1.removeMax()
m1.printHeap()

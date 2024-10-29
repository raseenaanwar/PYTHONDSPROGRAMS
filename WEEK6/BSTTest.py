class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.data is None:
            self.data=data
            return
        if self.data==data:
            return
        if self.data>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)


    def preorder(self):
#       root--left--right
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
#        left--root--right
        if self.lchild:
            self.lchild.inorder()
        print(self.data,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
#         left--right--root
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data,end=" ")

    def search(self,data):
        if self.data is None:
            print("Empty")
            return
        if self.data==data:
            print(data," Found")
            return
        if self.data>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Not Found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Not Found")
    def findMin(self):
        if self.data is None:
            print("empty")
            return
        current=self
        while current.lchild:
            current=current.lchild
        return current.data
    def findMax(self):
        if self.data is None:
            print("empty")
            return
        if self.rchild is None:
            return self.data
        return self.rchild.findMax()
    def closest_value(self, target):
        closestValue=float('inf')
        closestNode=None
        while self is not None:
            if(closestValue>abs(target-self.data)):
                closestValue=abs(target-self.data)
                closestNode=self.data
            if self.data<target:
                self=self.rchild
            elif self.data>target:
                self=self.lchild
            else:
                # self.data==target
                return self.data
        return closestNode
    def delete(self,data,current):
        if self.data is None:
            print("BST is empty")

        if data>self.data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,current)
            else:
                print("Not Present")
        elif data<self.data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,current)
            else:
                print("Not Present")
        else:
            if self.lchild is None:
                temp=self.rchild
                if data==current:
                    self.data=temp.data
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return temp
            if self.rchild is None:
                temp=self.lchild
                if data==current:
                    self.data=temp.data
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return temp
            node=self.rchild
            while node and node.lchild:
                node=node.lchild
            self.data=node.data
            self.rchild=self.rchild.delete(data,current)
        return self

    def isBST(self,min,max):
        if self is None:
            return True
        if self.data<min or self.data>max:
            return False
        if self.lchild is not None and not self.lchild.isBST(min,self.data-1):
            return False
        if self.rchild is not None and not self.rchild.isBST(self.data+1,max):
            return False
        return True

    def checkBST(self):
        if self.isBST(float('-inf'),float('inf')):
            return True
        else:
            return False
    def treeSum(self):
        if self is None:
            return 0
        else:
            leftsum=self.lchild.treeSum() if self.lchild is not None else 0
            rightsum=self.rchild.treeSum() if self.rchild is not None else 0
            return self.data+leftsum+rightsum

    def treeMax(self):
        if self is None:
            return 0
        else:
            leftmax=self.lchild.treeMax() if self.lchild is not None else 0
            rightmax=self.rchild.treeMax() if self.rchild is not None else 0
        return max(self.data,leftmax,rightmax)
    def treeHeight(self):
        if self is None:
            return 0
        else:
            leftheight=self.lchild.treeHeight() if self.lchild is not None else 0
            rightHeight=self.rchild.treeHeight() if self.rchild is not None else 0
        return 1+max(leftheight,rightHeight)

    def isExists(self,data):
        if self is None:
            return 0
        else:
            inleft=self.lchild.isExists(data) if self.lchild is not None else 0
            inright=self.rchild.isExists(data) if self.rchild is not None else 0
        return root.data==data or inright or inleft
    def reverseTree(self):
        if self is None:
            return
        else:
            self.lchild.reverseTree() if self.lchild is not None else None
            self.rchild.reverseTree() if self.rchild is not None else None
            self.lchild,self.rchild=self.rchild,self.lchild
    # def LCA(self,child1,child2):
    #     print('inside lca')
    #     if self is None:
    #         return None
    #             # if (child1<current.data and child2>current.data) or (child1>current.data and child2<current.data):
    #     #     return current.data
    #     if child1<self.data and child2<self.data:
    #         self.lchild.LCA(child1,child2)
    #     if child1>self.data and child2>self.data:
    #         self.rchild.LCA(child1,child2)
    #     return self.data
    def LCA(self, child1, child2):
        print('inside lca')
        if self is None:
            return None

        # If both child1 and child2 are smaller than root, then LCA lies in left subtree
        if child1 < self.data and child2 < self.data:
            return self.lchild.LCA(child1, child2)

        # If both child1 and child2 are greater than root, then LCA lies in right subtree
        if child1 > self.data and child2 > self.data:
            return self.rchild.LCA(child1, child2)

    # If one key is smaller and one key is greater, this node is the LCA
        return self.data


def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)


root=BST(50)
list1=[30,70,20,40,60,80,10]
for i in list1:
    root.insert(i)

# Finding LCA of 20 and 80
print('LCA of 20 and 80:', root.LCA(20, 80))  # Expected output: 50
print('lca of 20 and 40',root.LCA(10,40))
root.inorder()
# print("count=",count(root))
# print("Inorder")
# root.inorder()
# print()
# root.insert(78)
# print()
# root.inorder()
# print()
# root.search(10)
# if count(root)>1:
#     root.delete(10,root.data)
# else:
#     print("cant perform deletion")
# print("Inorder")
# root.inorder()
# print("postorddr")
# root.postorder()
# print(root.checkBST())
# print("close=",root.closest_value(78))
# print(root.treeSum())
# print("Max==" ,root.treeMax())
# print("Hiegh=",root.treeHeight())
# print(root.isExists(11))
# print()
# root.inorder()
# root.reverseTree()
# print()
# root.inorder()
print()
# print('min',root.findMin())
# print("max",root.findMax())

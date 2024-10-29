class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.data is None:
            self.data=data
            return
        if self.lchild is None:
            self.lchild=BinaryTree(data)
            return
        if self.rchild is None:
            self.rchild=BinaryTree(data)

        elif self.lchild:
            self.lchild.insert(data)
        else:
            self.rchild.insert(data)

    def isBST(self,min,max):
        if self is None:
            return True
        if self.data<min or self.data>max:
            return False
        return self.lchild.isBST(min,self.data-1) and self.rchild.isBST(self.data+1,max)
    def checkBST(self):
        if self.isBST(float('-inf'),float('inf')):
            return True
        else:
            return False

b1=BinaryTree(6)
b1.insert(2)
b1.insert(8)
b1.insert(1)
b1.insert(3)
b1.insert(7)
b1.insert(9)
print(b1.checkBST())

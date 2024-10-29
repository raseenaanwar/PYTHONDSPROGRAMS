class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)



    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def kth_largest(self, k):
        self.counter = 0
        elmns=[]
        def inorder_traversal(node):
            if node is None:
                return None
            right = inorder_traversal(node.right)
            if right is not None:
                return right
            self.counter += 1
            print(node.data)
            elmns.append(node.data)
            if self.counter == k:
                return node.data
            left = inorder_traversal(node.left)
            if left is not None:
                return left
            return None
        print(elmns)
        return inorder_traversal(self.root)


# Example usage
bst = BinarySearchTree()
bst.insert(10)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(8)
bst.insert(12)
bst.insert(16)

k = 5
kth_largest = bst.kth_largest(k)
print(f"The {k}th largest element is: {kth_largest}")

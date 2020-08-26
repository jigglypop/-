class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.parent = None

    def __str__(self):
        return str(self.val)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self.insertKey(self.root, val)
        return self.root is not None

    def insertKey(self, node, val):
        if node is None:
            node = TreeNode(val)
        else:
            # 크면 왼쪽 아니면 오른쪽
            if node.val >= val:
                node.left = self.insertKey(node.left, val)
            else:
                node.right = self.insertKey(node.right, val)
        return node


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

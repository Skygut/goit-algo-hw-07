class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def sumOfValues(self):
        return self._sumOfValues(self.root)

    def _sumOfValues(self, node):
        if not node:
            return 0
        return node.value + self._sumOfValues(node.left) + self._sumOfValues(node.right)


bst = BinarySearchTree()

bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)

total_sum = bst.sumOfValues()

print("Сума всіх значень у дереві:", total_sum)

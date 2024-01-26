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

    def findMax(self):
        return self._findMax(self.root)

    def _findMax(self, node):
        if not node:
            return None
        while node.right:
            node = node.right
        return node.value

    def findMin(self):
        return self._findMin(self.root)

    def _findMin(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node.value


# Створення екземпляра BinarySearchTree
bst = BinarySearchTree()

# Додавання значень у дерево
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(8)
bst.insert(12)
bst.insert(17)
bst.insert(25)

# Знаходження мінімального значення
min_value = bst.findMin()


print("Мінімальне значення в дереві:", min_value)

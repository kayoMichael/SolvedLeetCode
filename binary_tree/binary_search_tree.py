import unittest

"""
Qualities: Every subtree in a Binary Search Tree is also a Binary Search Tree
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BinarySearchTree:
    def __init__(self, root: Node):
        self.root = root

    def find(self, value):
        current = self.root
        result = self._find(current, value)
        return result

    def _find(self, node, value):
        if node is None or node.value == value:
            return node
        elif node.value < value:
            return self._find(node.right, value)
        else:
            return self._find(node.left, value)

    def insert(self, value):
        current = self.root
        self.root = self._insert(current, value)
        return self.root

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree(Node(5))
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)

    def test_find(self):
        self.assertEqual(self.tree.find(5).value, 5)
        self.assertEqual(self.tree.find(3).value, 3)
        self.assertEqual(self.tree.find(7).value, 7)
        self.assertEqual(self.tree.find(2).value, 2)
        self.assertEqual(self.tree.find(4).value, 4)
        self.assertEqual(self.tree.find(6).value, 6)
        self.assertEqual(self.tree.find(8).value, 8)
        self.assertIsNone(self.tree.find(10))

    def test_insert(self):
        self.assertIsNone(self.tree.find(10))
        self.tree.insert(10)
        self.assertEqual(self.tree.find(10).value, 10)
        self.tree.insert(19)
        self.assertEqual(self.tree.find(19).value, 19)


if __name__ == '__main__':
    unittest.TestCase()

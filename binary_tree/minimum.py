import unittest

from binary_search_tree import Node, BinarySearchTree


def find_min_in_value(root):
    min = minimum_value(root)
    return min


def minimum_value(node):
    if node.left is None and node.right is None:
        return node.value
    left = minimum_value(node.left)
    right = minimum_value(node.right)
    return min([left, right, node.value])


class TestMinValue(unittest.TestCase):
    def setUp(self):
        # Creating the binary search tree
        self.tree = BinarySearchTree(Node(5))
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)

    def test_min_value(self):
        self.assertEqual(find_min_in_value(self.tree.root), 2)



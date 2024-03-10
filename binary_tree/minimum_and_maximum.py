import unittest

from binary_search_tree import Node, BinarySearchTree


def find_min_in_value(root):
    min = minimum_value(root)
    return min


def minimum_value(node):
    if node is None:
        return float("inf")
    left = minimum_value(node.left)
    right = minimum_value(node.right)
    return min([left, right, node.value])


def find_minimum_of_bst(node):
    previous = None
    while node is not None:
        previous = node
        node = node.left

    return previous


def maximum_value(node):
    if node is None:
        return float("-inf")
    left = maximum_value(node.left)
    right = maximum_value(node.right)
    return max([left, right, node.value])


def maximum_value_bst(node):
    while node.right is not None:
        node = node.right

    return node


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


if __name__ == "__main__":
    unittest.TestCase()

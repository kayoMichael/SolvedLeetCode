import unittest

from binary_search_tree import Node, BinarySearchTree


# Depth Level Traversal


# Pre-order Root, left, right
def pre_order_traverse(node, result):
    if node is None:
        return

    result.append(node.value)
    pre_order_traverse(node.left, result)
    pre_order_traverse(node.right, result)


# In-order: Left, Root, Right
def in_order_traverse(node, result):
    if node is None:
        return

    in_order_traverse(node.left, result)
    result.append(node.value)
    in_order_traverse(node.right, result)


# Post Order: Left, Right, Root
def post_order_traverse(node, result):
    if node is None:
        return

    post_order_traverse(node.left, result)
    post_order_traverse(node.right, result)
    result.append(node.value)


class TestBinaryTreeTraversal(unittest.TestCase):
    def setUp(self):
        # Creating the binary search tree
        self.tree = BinarySearchTree(Node(5))
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)

    def test_pre_order_traverse(self):
        result = []
        pre_order_traverse(self.tree.root, result)
        expected_result = [5, 3, 2, 4, 7, 6, 8]
        self.assertEqual(result, expected_result)

    def test_in_order_traverse(self):
        result = []
        in_order_traverse(self.tree.root, result)
        expected_result = [2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(result, expected_result)

    def test_post_order_traverse(self):
        result = []
        post_order_traverse(self.tree.root, result)
        expected_result = [2, 4, 3, 6, 8, 7, 5]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

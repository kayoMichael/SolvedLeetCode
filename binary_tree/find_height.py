import unittest

from binary_search_tree import Node, BinarySearchTree


def find_height(node: Node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 0
    return 1 + max(find_height(node.left), find_height(node.right))


class TestBinarySearchTreeMethods(unittest.TestCase):

    def setUp(self):
        # Creating the binary search tree
        self.tree = BinarySearchTree(Node(8))
        self.tree.insert(3)
        self.tree.insert(10)
        self.tree.insert(1)
        self.tree.insert(6)
        self.tree.insert(14)
        self.tree.insert(4)
        self.tree.insert(7)
        self.tree.insert(13)

    def test_find_height(self):
        # Create a sample binary search tree

        # Test the height of the entire tree
        self.assertEqual(find_height(self.tree.root), 3)

        # Test the height of subtrees
        self.assertEqual(find_height(self.tree.root.left), 2)
        self.assertEqual(find_height(self.tree.root.right), 2)
        self.assertEqual(find_height(self.tree.root.left.left), 0)
        self.assertEqual(find_height(self.tree.root.left.right), 1)
        self.assertEqual(find_height(self.tree.root.right.right), 1)
        self.assertEqual(find_height(self.tree.root.left.right.left), 0)
        self.assertEqual(find_height(self.tree.root.left.right.right), 0)
        self.assertEqual(find_height(self.tree.root.right.right.left), 0)


if __name__ == '__main__':
    unittest.main()

import unittest

from binary_search_tree import BinarySearchTree, Node


# Return All the Nodes at distance K
def node_at_level_k(node, distance):
    def recurse_node(root, height, target):
        if root is None:
            return
        if height == 0:
            target.append(root.value)
            return

        recurse_node(root.left, height - 1, target)
        recurse_node(root.right, height - 1, target)

    target_node = []

    recurse_node(node, distance, target_node)
    return target_node


class NodeAtDistanceK(unittest.TestCase):

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

    def test_node_at_k(self):
        self.assertEqual(node_at_level_k(self.tree.root, 3), [4, 7, 13])
        self.assertEqual(node_at_level_k(self.tree.root, 2), [1, 6, 14])
        self.assertEqual(node_at_level_k(self.tree.root, 1), [3, 10])
        self.assertEqual(node_at_level_k(self.tree.root, 0), [8])


if __name__ == '__main__':
    unittest.main()

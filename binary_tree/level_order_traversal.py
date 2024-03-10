import unittest

from binary_search_tree import BinarySearchTree, Node


# Level Order Traversal: By Using Pure Recursion


def level_order_traverse(node):
    def find_height(root):
        if root is None:
            return 0
        return 1 + max(find_height(root.left), find_height(root.right))

    def find_row(root):
        height = find_height(node)
        total = []
        for i in range(1, height + 1):
            target_node = []
            find_k_distance(root, i, target_node)
            total.append(target_node)

        return total

    def find_k_distance(root, distance, target):
        if root is None:
            return
        if distance == 1:
            target.append(root.value)
            return
        find_k_distance(root.left, distance - 1, target)
        find_k_distance(root.right, distance - 1, target)

    return find_row(node)


class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        # Creating the binary search tree
        self.tree = BinarySearchTree(Node(5))
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)

    def test_level_order_traversal(self):
        self.assertEqual(level_order_traverse(self.tree.root), [[5], [3, 7], [2, 4, 6, 8]])


if __name__ == "__main__":
    unittest.TestCase()

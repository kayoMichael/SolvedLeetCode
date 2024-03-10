"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def in_order_traverse(root, in_order):
    if root is None:
        return
    in_order_traverse(root.left, in_order)
    in_order.append(root.val)
    in_order_traverse(root.right, in_order)


def is_valid_bst(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    in_order = []

    in_order_traverse(root, in_order)

    before = in_order[0]
    for i in in_order[1:]:
        if i <= before:
            return False
        before = i

    return True


# O(N) method with range
def is_valid_bst_range(node):
    min_node = float('-inf')
    max_node = float('inf')

    def is_valid(root, minimum, maximum):
        if root is None:
            return True
        elif max_node < root.value or root.value < min_node:
            return False
        return is_valid(root.left, minimum, root.value - 1) and is_valid(root.right, root.value + 1, maximum)

    return is_valid(node)

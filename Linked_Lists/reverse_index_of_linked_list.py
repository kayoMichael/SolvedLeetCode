"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]



Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

"""
import unittest

from linked_list import Node


def reverseBetween(head, left, right):
    current = head

    dummy_head = Node(None)
    dummy_head.next = current

    for i in range(left - 1):
        dummy_head = dummy_head.next

    prev = None
    temp = dummy_head

    dummy_head = dummy_head.next
    first = dummy_head

    for i in range(right - left + 1):
        if i == (right - left):
            final = dummy_head.next
        memo = dummy_head.next
        dummy_head.next = prev
        prev = dummy_head
        dummy_head = memo

    temp.next = prev
    first.next = final

    if left == 1:
        return prev
    else:
        return head


# Time Complexity: O(N)
# Space Complexity: O(1)


class TestReverseBetween(unittest.TestCase):
    def setUp(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        self.head = Node(1)
        self.head.next = Node(2)
        self.head.next.next = Node(3)
        self.head.next.next.next = Node(4)
        self.head.next.next.next.next = Node(5)

    def test_reverse_between(self):
        # After reversal, the linked list should be: 1 -> 4 -> 3 -> 2 -> 5
        first_node = reverseBetween(self.head, 2, 4)
        values = []
        while first_node:
            values.append(first_node.data)
            first_node = first_node.next
        self.assertEqual(values, [1, 4, 3, 2, 5])

    def test_reverse_between_2(self):
        # After reversal, the linked list should be: 5
        first_node = reverseBetween(Node(5), 1, 1)
        values = []
        while first_node:
            values.append(first_node.data)
            first_node = first_node.next
        self.assertEqual(values, [5])

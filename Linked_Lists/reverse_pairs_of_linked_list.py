"""
Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the
values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]



Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100


"""
import unittest
from typing import Optional

from linked_list import Node


def swap_pairs(head: Optional[Node]) -> Optional[Node]:
    if not head or not head.next:
        return head

    return_location = head.next

    prev = None
    current = head
    while current and current.next:
        if prev:
            prev.next = current.next
        prev = current
        temp = current.next.next
        current.next.next = current
        current.next = temp
        current = temp

    return return_location


# Time Complexity: O(N)
# Space Complexity O(1)


class TestReversePairsOfLinkedList(unittest.TestCase):
    def setUp(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        self.head = Node(1)
        self.head.next = Node(2)
        self.head.next.next = Node(3)
        self.head.next.next.next = Node(4)
        self.head.next.next.next.next = Node(5)

    def test_reverse_pairs_of_linked_list(self):
        first_node = swap_pairs(self.head)
        values = []
        current = first_node
        while current is not None:
            values.append(current.data)
            current = current.next
        self.assertEqual(values, [2, 1, 4, 3, 5])


if __name__ == '__main__':
    unittest.main()

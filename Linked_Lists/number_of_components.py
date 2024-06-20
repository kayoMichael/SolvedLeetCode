import unittest
from typing import Optional, List

from linked_list import Node

"""
You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.



Example 1:

Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:

Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.



Constraints:

    The number of nodes in the linked list is n.
    1 <= n <= 104
    0 <= Node.val < n
    All the values Node.val are unique.
    1 <= nums.length <= n
    0 <= nums[i] < n
    All the values of nums are unique.


"""


def num_components(head: Optional[Node], nums: List[int]) -> int:
    connected = 0
    memo = {}
    for num in nums:
        memo[num] = 1

    previous = False
    while head is not None:
        if head.data in memo and not previous:
            connected += 1
            previous = True
        elif head.data not in memo:
            previous = False
        head = head.next
    return connected


# Time Complexity: O(M + N) Where M is the length of Nums and N is the length of Linked List (Simplifies to O(N))
# Space Complexity: O(M)


class TestNumberOfComponents(unittest.TestCase):
    def setUp(self):
        self.linked = Node(0)
        self.linked.next = Node(1)
        self.linked.next.next = Node(2)
        self.linked.next.next.next = Node(3)
        self.linked_2 = Node(0)
        self.linked_2.next = Node(1)
        self.linked_2.next.next = Node(2)
        self.linked_2.next.next.next = Node(3)
        self.linked_2.next.next.next.next = Node(4)
        self.linked_3 = Node(8)
        self.linked_3.next = Node(5)
        self.linked_3.next.next = Node(2)
        self.linked_3.next.next.next = Node(3)

    def test_number_of_components(self):
        self.assertEqual(num_components(self.linked, [0, 1, 3]), 2)
        self.assertEqual(num_components(self.linked_2, [0, 3, 1, 4]), 2)
        self.assertEqual(num_components(self.linked_2, [3, 1, 4, 2]), 1)
        self.assertEqual(num_components(self.linked_3, [3, 2, 5, 8]), 1)
        self.assertEqual(num_components(self.linked_3, [5, 3]), 2)
        self.assertEqual(num_components(self.linked_3, [8, 5, 3]), 2)

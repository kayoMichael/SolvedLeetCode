from linked_list import Node
from linked_list import LinkedList
import unittest
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

与えられた head 、連結リストのヘッドが与えられた場合、その連結リストにサイクルがあるかどうかを判断します。

連結リストにサイクルがある場合、リスト内のあるノードが次のポインタを追い続けることで再び到達できるノードが存在します。内部的には、pos はテールの次のポインタが接続されているノードのインデックスを示すために使用されます。ただし、pos はパラメータとして渡されません。

連結リストにサイクルがある場合は true を返し、それ以外の場合は false を返します。

例 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: 連結リストにサイクルがあり、テールが1番目のノードに接続されています（0-indexed）。

例 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: 連結リストにサイクルがあり、テールが0番目のノードに接続されています。

例 3:
Input: head = [1], pos = -1
Output: false
Explanation: 連結リストにサイクルがありません。

制約条件:

リスト内のノード数は範囲 [0, 104] にあります。
-105 <= Node.val <= 105
pos は連結リスト内の有効なインデックスまたは -1 です。
"""


def has_cycle(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True
    return False

# Time Complexity: O(N)
# Space Complexity: O(N)


# Test
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    # Create nodes
    nodes = [Node(value) for value in values]

    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create a cycle if pos is a valid index
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.head = create_linked_list_with_cycle([3, 2, 0, -4], pos=1)
        self.head_2 = create_linked_list_with_cycle([3, 1, 0, -1, 4, 7, 9], pos=3)
        self.linked_list_3 = LinkedList()
        self.linked_list_3.add_first(3)
        self.linked_list_3.add_first(8)
        self.linked_list_3.add_first(5)
        self.linked_list_3.add_first(2)

    def test_has_cycle(self):
        self.assertTrue(has_cycle(self.head))
        self.assertTrue(has_cycle(self.head_2))
        self.assertFalse(has_cycle(self.linked_list_3.head))


if __name__ == '__main__':
    unittest.main()

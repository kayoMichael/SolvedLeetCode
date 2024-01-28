from linked_list import Node
import unittest

"""
Reverse a Singly Linked List

Given a singly linked list, reverse the order of its nodes.

Example:

Input: 1 -> 2 -> 3 -> 4 -> 5

Output: 5 -> 4 -> 3 -> 2 -> 1

Instructions:

Reverse the order of the nodes in the given singly linked list. Each node contains a value, and there is a reference 
pointing to the next node in the sequence. Modify the pointers to achieve a reversed order.

Input:

    The input is the head of a single linked list.

Output:

    Return the modified linked list with the reversed order of nodes.

Note:
    The reversal should be done in-place, meaning you should modify the existing nodes rather than creating a new linked 
    list.
    The head of the linked list after reversal becomes the new tail.
    The tail of the linked list after reversal becomes the new head.
"""

"""
単一連結リストの反転

単一連結リストが与えられた場合、そのノードの順序を反転させます。

例：

入力: 1 -> 2 -> 3 -> 4 -> 5

出力: 5 -> 4 -> 3 -> 2 -> 1

手順：
    与えられた単一連結リストのノードの順序を反転させます。各ノードには値が含まれ、シーケンス内の次のノードへの参照があります。反転した順序を達成するためにポインタを変更します。

入力：
    入力は単一連結リストのヘッドです。

出力：
    反転されたノードの順序を持つ変更された連結リストを返します。

注意：
    反転はインプレースで行われるべきであり、新しい連結リストを作成するのではなく既存のノードを変更するべきです。
    反転後の連結リストのヘッドは新しいテールとなります。
    反転後の連結リストのテールは新しいヘッドとなります。
"""


def reverse(head):
    current = head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Time Complexity: O(N)
# Space Complexity: O(1)


class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        self.head = Node(1)
        self.head.next = Node(2)
        self.head.next.next = Node(3)
        self.head.next.next.next = Node(4)
        self.head.next.next.next.next = Node(5)

    def test_reverse_linked_list(self):
        first_node = reverse(self.head)
        # After reversal, the linked list should be: 5 -> 4 -> 3 -> 2 -> 1
        values = []
        current = first_node
        while current is not None:
            values.append(current.data)
            current = current.next
        self.assertEqual(values, [5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()


from linked_list import Node
import unittest

"""
Problem: Find the kth Node from the End of a Linked List

You are given a singly linked list. Write a function to find the kth node from the end of the list. Your algorithm 
should iterate through the list only once.

Example:

Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2

Output: 3

Instructions:

Implement a function that takes the head of a singly linked list and an integer k as parameters and returns the kth 
node from the end of the list.

Your algorithm should iterate through the linked list only once.

Note:

Ensure that the input list contains at least k nodes.
"""

"""
問題: 連結リストの末尾からk番目のノードを見つける

単一の連結リストが与えられます。リストの末尾からk番目のノードを見つける関数を書いてください。アルゴリズムはリストを1回だけ反復する必要があります。

例:

入力: 1 -> 2 -> 3 -> 4 -> 5、k = 2

出力: 3

手順:

単一の連結リストのヘッドと整数kをパラメータとして受け取り、リストの末尾からk番目のノードを返す関数を実装してください。

アルゴリズムはリストを1回だけ反復する必要があります。

注意:

入力リストには少なくともk個のノードが含まれていることを確認してください。
"""


def kth_node_from_the_end(head, index):
    slow = head
    fast = head

    for i in range(0, index + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.data

# Time Complexity: O(N)
# Space Complexity: O(N)


class TestKthNodeFromEnd(unittest.TestCase):
    def setUp(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        self.head = Node(1)
        self.head.next = Node(2)
        self.head.next.next = Node(3)
        self.head.next.next.next = Node(4)
        self.head.next.next.next.next = Node(5)

    def test_kth_node_from_end(self):
        self.assertEqual(kth_node_from_the_end(self.head, 0), 5)
        self.assertEqual(kth_node_from_the_end(self.head, 1), 4)
        self.assertEqual(kth_node_from_the_end(self.head, 2), 3)
        self.assertEqual(kth_node_from_the_end(self.head, 3), 2)
        self.assertEqual(kth_node_from_the_end(self.head, 4), 1)


if __name__ == '__main__':
    unittest.main()


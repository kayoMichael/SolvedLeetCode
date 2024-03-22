import unittest
from typing import Optional

from linked_list import Node


def isPalindrome(head: Optional[Node]) -> bool:
    def find_middle(node):
        index = node
        runner = node
        while runner.next is not None and runner.next.next is not None:
            index = index.next
            runner = runner.next.next

        return index

    def reverse_list(node):
        prev = None
        while node is not None:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    middle = find_middle(head)
    middle.next = reverse_list(middle.next)
    current = head
    while head is not None:
        print(head.data)
        head = head.next

    middle = middle.next
    while middle is not None:
        if middle.data != current.data:
            return False
        middle = middle.next
        current = current.next
    return True


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 ->
        self.head = Node(1)
        self.head.next = Node(2)
        self.head.next.next = Node(3)
        self.head.next.next.next = Node(2)
        self.head.next.next.next.next = Node(1)


if __name__ == '__main__':
    # unittest.main()
    head = Node(1)
    head.next = Node(2)
    print(isPalindrome(head))

import unittest

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Singly linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __is_empty(self) -> bool:
        return self.head is None

    # Time Complexity O(1)
    def add_last(self, data):
        new_node = Node(data)
        self.length += 1
        if self.__is_empty():
            self.tail = self.head = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # Time Complexity O(1)
    def add_first(self, data):
        new_node = Node(data)
        self.length += 1
        if self.__is_empty():
            self.head = self.tail = new_node
            return
        second_node = self.head
        self.head = new_node
        self.head.next = second_node

    # Time Complexity O(1)
    def delete_first(self):
        if self.__is_empty():
            raise ValueError("No Such Value Found")
        self.length -= 1
        if self.head is self.tail:
            self.head = self.tail = None
            return
        second_node = self.head.next
        self.head.next = None
        self.head = second_node

    def delete_last(self):
        if self.__is_empty():
            raise ValueError("No Such Value Found")
        self.length -= 1
        if self.head is self.tail:
            self.head = self.tail = None
            return
        current = self.head
        while current:
            if current.next is self.tail:
                break
            current = current.next
        current.next = None
        self.tail = current
        self.tail.next = None

    def index_of(self, item):
        index = 0
        current = self.head
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, item):
        return self.index_of(item) != -1

    def size(self) -> int:
        return self.length

    def convert_to_list(self):
        new_list = []
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        print(f"Head: {self.head.data}")
        print(f"Tail: {self.tail.data}")


class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_add_first(self):
        self.linked_list.add_first(1)
        self.assertEqual(self.linked_list.convert_to_list(), [1])
        self.linked_list.add_first(4)
        self.linked_list.add_first(6)
        self.linked_list.add_first(9)
        self.assertEqual(self.linked_list.convert_to_list(), [9, 6, 4, 1])

    def test_add_last(self):
        self.linked_list.add_last(1)
        self.linked_list.add_last(2)
        self.assertEqual(self.linked_list.convert_to_list(), [1, 2])
        self.linked_list.add_first(3)
        self.linked_list.add_last(3)
        self.assertEqual(self.linked_list.convert_to_list(), [3, 1, 2, 3])

    def test_delete_first(self):
        self.linked_list.add_last(1)
        self.linked_list.add_last(2)
        self.linked_list.delete_first()
        self.assertEqual(self.linked_list.convert_to_list(), [2])

    def test_delete_second(self):
        self.linked_list.add_last(1)
        self.linked_list.add_last(2)
        self.linked_list.add_last(3)
        self.linked_list.delete_last()
        self.assertEqual(self.linked_list.convert_to_list(), [1, 2])

    def test_index_of(self):
        self.linked_list.add_last(1)
        self.linked_list.add_last(2)
        self.linked_list.add_last(3)
        self.assertEqual(self.linked_list.index_of(2), 1)
        self.assertEqual(self.linked_list.index_of(17), -1)

    def test_contains(self):
        self.linked_list.add_last(1)
        self.linked_list.add_last(2)
        self.linked_list.add_last(3)
        self.assertEqual(self.linked_list.contains(2), True)
        self.assertEqual(self.linked_list.contains(17), False)

    def size(self):
        self.linked_list.add_last(1)
        self.linked_list.add_last(2)
        self.linked_list.add_last(3)
        self.assertEqual(self.size, 3)


if __name__ == '__main__':
    unittest.main()

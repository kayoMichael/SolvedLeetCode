import sys
import unittest

from original_queue import Queue

sys.path.insert(0, '..')
from stacks.stacks import Stack


# Reverse Queue with stack
def reverse_queue(queue: Queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    return queue


# Reverse Queue with list acting as a stack
def reverse_queue_list(queue: Queue):
    stack = []
    while not queue.is_empty():
        stack.append(queue.dequeue())

    while len(stack) != 0:
        queue.enqueue(stack.pop())

    return queue


# Time Complexity: O(N)
# Space Complexity: O(N)

class TestReverseQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.queue.enqueue(4)
        self.empty_queue = Queue()
        self.queue_2 = Queue()
        self.queue_2.enqueue(2)
        self.queue_2.enqueue(10)
        self.queue_2.enqueue("2ek")

    def test_queue_reverse(self):
        self.assertEqual(reverse_queue(self.queue).show_queue(), [4, 10, 5, 3, 2])
        self.assertEqual(reverse_queue(self.empty_queue).show_queue(), [])
        self.assertEqual(reverse_queue(self.queue_2).show_queue(), ["2ek", 10, 2])

    def test_queue_reverse_list(self):
        self.assertEqual(reverse_queue_list(self.queue).show_queue(), [4, 10, 5, 3, 2])
        self.assertEqual(reverse_queue_list(self.empty_queue).show_queue(), [])
        self.assertEqual(reverse_queue_list(self.queue_2).show_queue(), ["2ek", 10, 2])


if __name__ == '__main__':
    unittest.main()

import copy
import sys
import unittest

from original_queue import Queue

sys.path.insert(0, '..')
from stacks.stacks import Stack


def queue_reverse(amount, queue: Queue):
    reverse = Stack()
    keep = []
    if queue.size() == 0 or amount == 1 or amount == 0:
        return queue
    for i in range(0, amount):
        reverse.push(queue.dequeue())

    while not queue.is_empty():
        keep.append(queue.dequeue())

    while not reverse.is_empty():
        queue.enqueue(reverse.pop())

    for i in keep:
        queue.enqueue(i)

    return queue


class TestReverseKQueue(unittest.TestCase):
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
        queue = copy.deepcopy(self.queue)
        self.assertEqual(queue_reverse(3, queue).show_queue(), [5, 3, 2, 10, 4])

        self.assertEqual(queue_reverse(3, self.empty_queue).show_queue(), [])

        queue_2 = copy.deepcopy(self.queue_2)
        self.assertEqual(queue_reverse(3, queue_2).show_queue(), ["2ek", 10, 2])

        queue_2 = copy.deepcopy(self.queue_2)
        self.assertEqual(queue_reverse(2, queue_2).show_queue(), [10, 2, "2ek"])

        queue = copy.deepcopy(self.queue)
        self.assertEqual(queue_reverse(4, queue).show_queue(), [10, 5, 3, 2, 4])

        queue = copy.deepcopy(self.queue)
        self.assertEqual(queue_reverse(0, queue).show_queue(), [2, 3, 5, 10, 4])

        queue = copy.deepcopy(self.queue)
        self.assertEqual(queue_reverse(1, queue).show_queue(), [2, 3, 5, 10, 4])


if __name__ == "__main__":
    unittest.main()

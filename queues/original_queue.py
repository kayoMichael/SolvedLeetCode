import sys

sys.path.insert(0, '..')
from stacks.stacks import Stack


# Inspired by Standard Java Queue Interface
class FixSizedQueue:
    def __init__(self, length):
        self.queue = []
        self.length = 0
        self.max_length = length
        self.front = 0
        self.rear = -1

    def is_full(self):
        return self.max_length >= self.length

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.length
        self.length += 1

    def offer(self, item):
        if self.is_full():
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.length
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception
        self.length -= 1
        self.rear -= 1
        front = self.queue[self.front]
        self.queue[self.front] = 0
        self.front += 1
        return front

    def pull(self):
        if self.is_empty():
            return
        self.length -= 1
        self.rear -= 1
        front = self.queue[self.front]
        self.queue[self.front] = 0
        self.front += 1
        return front

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def element(self):
        if self.is_empty():
            raise Exception
        return self.queue[self.front]

    def size(self):
        return self.length

    def is_empty(self):
        return self.size == 0


# python flexible queue
class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        front = self.queue[0]
        del self.queue[0]
        self.length -= 1
        return front

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def show_queue(self):
        return self.queue


# Queue made with Stack
class StackQueue:
    def __init__(self, length):
        self.queue = Stack()
        self.queue_2 = Stack()
        self.length = 0
        self.max_length = 0

    def enqueue(self, item):
        if self.max_length:
            raise OverflowError
        self.queue.push(item)
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception
        while not self.queue.is_empty():
            self.queue_2.push(self.queue.pop())
        front = self.queue_2.pop()
        self.length -= 1
        while not self.queue_2.is_empty():
            self.queue.push(self.queue_2.pop())

        return front

    def peak(self):
        return self.queue.peek()

    def is_full(self):
        return self.length >= self.max_length

    def is_empty(self):
        return self.length == 0

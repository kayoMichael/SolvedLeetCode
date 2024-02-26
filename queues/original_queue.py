# Inspired by Standard Java Queue Interface
class FixSizedQueue:
    def __init__(self, length):
        self.queue = []
        self.length = 0
        self.max_length = length

    def is_full(self):
        return self.max_length >= self.length

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError
        self.queue.append(item)
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception
        front = self.queue[0]
        del self.queue[0]
        self.length -= 1
        return front

    def pull(self):
        if self.is_empty():
            return
        front = self.queue[0]
        del self.queue[0]
        self.length -= 1
        return front

    def offer(self, item):
        if self.is_full():
            return
        self.queue.append(item)
        self.length += 1

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def element(self):
        if self.is_empty():
            raise Exception
        return self.queue[0]

    def size(self):
        return self.length

    def is_empty(self):
        return self.size == 0


class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.length += 1

    def dequeue(self):
        if len(self.queue):
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
        return self.size == 0

    def show_queue(self):
        return self.queue

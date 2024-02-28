class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    # for debugging purposes only
    def __str__(self):
        structure = str(self.stack)
        return structure

class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        return not bool(self.data)
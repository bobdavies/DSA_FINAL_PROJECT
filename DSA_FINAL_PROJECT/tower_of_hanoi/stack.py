class Stack:
    def __init__(self, size, name):
        """Initialize a stack with fixed size and optional name"""
        self.size = size
        self.stack = [None] * size
        self.top = -1
        self.name = name

    def is_empty(self):
        """Check if the stack is empty"""
        return self.top == -1

    def is_full(self):
        """Check if the stack is full"""
        return self.top == self.size - 1

    def push(self, item):
        """Add an item to the top of the stack"""
        if self.is_full():
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise Exception("Stack Underflow")
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def get_items(self):
        """Return list of items currently in the stack"""
        return self.stack[:self.top + 1]

    def __str__(self):
        """Return a string representation of the stack"""
        items = self.stack[:self.top + 1]
        return f"Stack {self.name}: {items}"

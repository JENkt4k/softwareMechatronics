# stack.py
"""
Stack (LIFO)
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.pop())  # 20

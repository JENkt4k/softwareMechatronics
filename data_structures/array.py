# array.py
"""
Simple Array Wrapper
"""

class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Array index out of bounds")

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Array index out of bounds")

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    arr = Array(5)
    arr.set(0, 10)
    print(arr.get(0))
    print(arr)

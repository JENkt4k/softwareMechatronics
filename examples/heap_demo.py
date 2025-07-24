# heap_demo.py
"""
Demo for BinaryHeap (Min-Heap and Max-Heap).
"""

from composites.data_structures.heap import BinaryHeap

def main():
    print("=== Min-Heap Demo ===")
    min_heap = BinaryHeap(min_heap=True)
    for val in [5, 3, 8, 1, 2]:
        print(f"Pushing {val}...")
        min_heap.push(val)
        print("Heap:", min_heap)

    print(f"Peek: {min_heap.peek()}")
    print(f"Pop: {min_heap.pop()}")
    print("Heap after pop:", min_heap)

    print("\\n=== Max-Heap Demo ===")
    max_heap = BinaryHeap(elements=[5, 3, 8, 1, 2], min_heap=False)
    print("Initial heapified:", max_heap)
    max_heap.push(10)
    print("After push(10):", max_heap)
    print("Pop:", max_heap.pop())
    print("Heap after pop:", max_heap)

if __name__ == "__main__":
    main()
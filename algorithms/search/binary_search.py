# binary_search.py
"""
Binary Search Implementation
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 5))  # Expected: 2

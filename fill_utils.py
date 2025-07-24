import os

utils_dir = r"E:\git_slow\SoftwareMechatronics\utils"

utils_files_content = {
    "memoization.py": '''# memoization.py
"""
Memoization decorator for caching function results.
"""

from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


if __name__ == "__main__":
    @memoize
    def fib(n):
        return n if n <= 1 else fib(n - 1) + fib(n - 2)

    print(f"fib(10) = {fib(10)}")  # 55
''',

    "bitmasking.py": '''# bitmasking.py
"""
Bitmasking utilities.
"""

def is_set(mask, pos):
    return (mask & (1 << pos)) != 0

def set_bit(mask, pos):
    return mask | (1 << pos)

def clear_bit(mask, pos):
    return mask & ~(1 << pos)

def toggle_bit(mask, pos):
    return mask ^ (1 << pos)


if __name__ == "__main__":
    mask = 0
    mask = set_bit(mask, 1)
    print(f"After setting bit 1: {bin(mask)}")
    print(f"Is bit 1 set? {is_set(mask, 1)}")
    mask = toggle_bit(mask, 1)
    print(f"After toggling bit 1: {bin(mask)}")
''',

    "benchmarks.py": '''# benchmarks.py
"""
Benchmarking utilities.
"""

import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

def benchmark(func, *args, iterations=1000, **kwargs):
    start = time.perf_counter()
    for _ in range(iterations):
        func(*args, **kwargs)
    end = time.perf_counter()
    avg_time = (end - start) / iterations
    print(f"{func.__name__}: {avg_time:.6f} sec per iteration ({iterations} runs)")
    return avg_time


if __name__ == "__main__":
    @timeit
    def slow_add(a, b):
        time.sleep(0.1)
        return a + b

    slow_add(3, 5)

    def fast_add(a, b):
        return a + b

    benchmark(fast_add, 3, 5, iterations=100000)
'''
}

os.makedirs(utils_dir, exist_ok=True)

for filename, content in utils_files_content.items():
    file_path = os.path.join(utils_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

print(f"Utils created in {utils_dir} with sys.path fix where needed.")

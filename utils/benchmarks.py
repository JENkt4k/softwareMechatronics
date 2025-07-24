# benchmarks.py
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

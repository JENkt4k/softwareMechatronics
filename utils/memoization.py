# memoization.py
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

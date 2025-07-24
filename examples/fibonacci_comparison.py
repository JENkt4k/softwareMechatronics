# fibonacci_comparison.py
"""
Example: Comparing Recursive vs DP Fibonacci
"""

from functools import lru_cache

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

@lru_cache(maxsize=None)
def fib_dp(n):
    if n <= 1:
        return n
    return fib_dp(n - 1) + fib_dp(n - 2)

if __name__ == "__main__":
    n = 10
    print(f"fib_recursive({n}) = {fib_recursive(n)}")
    print(f"fib_dp({n}) = {fib_dp(n)}")

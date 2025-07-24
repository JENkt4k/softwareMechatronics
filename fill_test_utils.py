import os

tests_dir = r"E:\git_slow\SoftwareMechatronics\tests"

test_utils_content = '''# test_utils.py

import unittest
import time
from utils.memoization import memoize
from utils.bitmasking import is_set, set_bit, clear_bit, toggle_bit
from utils.benchmarks import timeit, benchmark


class TestUtils(unittest.TestCase):

    def test_memoize(self):
        call_count = {"calls": 0}

        @memoize
        def slow_add(a, b):
            call_count["calls"] += 1
            return a + b

        self.assertEqual(slow_add(1, 2), 3)
        self.assertEqual(slow_add(1, 2), 3)  # Cached
        self.assertEqual(call_count["calls"], 1)  # Only computed once

    def test_bitmasking(self):
        mask = 0
        mask = set_bit(mask, 2)
        self.assertTrue(is_set(mask, 2))
        mask = clear_bit(mask, 2)
        self.assertFalse(is_set(mask, 2))
        mask = toggle_bit(mask, 1)
        self.assertTrue(is_set(mask, 1))
        mask = toggle_bit(mask, 1)
        self.assertFalse(is_set(mask, 1))

    def test_timeit_and_benchmark(self):
        @timeit
        def dummy_add(a, b):
            return a + b

        result = dummy_add(5, 10)
        self.assertEqual(result, 15)

        # Benchmark test (quick function to ensure timing works)
        def fast_add(a, b):
            return a + b

        avg_time = benchmark(fast_add, 5, 10, iterations=10)
        self.assertGreaterEqual(avg_time, 0)


if __name__ == '__main__':
    unittest.main()
'''

os.makedirs(tests_dir, exist_ok=True)

file_path = os.path.join(tests_dir, "test_utils.py")
with open(file_path, "w") as f:
    f.write(test_utils_content)

print(f"test_utils.py created at {file_path}")

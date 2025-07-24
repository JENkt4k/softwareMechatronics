# kmp_example.py
"""
Example demonstrating KMP string search.
"""

from algorithms.string.kmp import kmp_search

def main():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Pattern found at indices: {matches}")

if __name__ == "__main__":
    main()

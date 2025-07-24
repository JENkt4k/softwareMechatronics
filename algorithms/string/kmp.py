# kmp.py
"""
Knuth-Morris-Pratt (KMP) String Search Algorithm

The KMP algorithm searches for occurrences of a "pattern" P within a main "text" T
by employing the observation that when a mismatch occurs, the pattern itself
contains sufficient information to determine where the next match could begin.
"""

def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for the KMP algorithm.
    :param pattern: Pattern string.
    :return: lps array.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    KMP pattern searching algorithm.
    :param text: Text string.
    :param pattern: Pattern string to search.
    :return: List of starting indices where pattern is found in text.
    """
    if not pattern or not text:
        return []

    lps = compute_lps(pattern)
    result = []

    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(text, pattern)
    print(f"Pattern found at indices: {matches}")

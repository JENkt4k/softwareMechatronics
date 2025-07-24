# edit_distance.py
"""
Edit Distance (Levenshtein Distance) using Dynamic Programming
"""

def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],    # Insert
                                   dp[i - 1][j],    # Remove
                                   dp[i - 1][j - 1]) # Replace
    return dp[m][n]


if __name__ == "__main__":
    s1, s2 = "kitten", "sitting"
    print(f"Edit distance between '{s1}' and '{s2}': {edit_distance(s1, s2)}")

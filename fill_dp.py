import os

# Adjust this to your local path
dp_dir = r"E:\git_slow\SoftwareMechatronics\algorithms\dp"

dp_files_content = {
    "knapsack.py": '''# knapsack.py
"""
0/1 Knapsack Problem using Dynamic Programming
"""

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print(f"Max value: {knapsack(weights, values, capacity)}")
''',

    "edit_distance.py": '''# edit_distance.py
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
''',

    "lis.py": '''# lis.py
"""
Longest Increasing Subsequence (LIS) using Dynamic Programming
"""

def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(f"Length of LIS: {lis(arr)}")
'''
}

os.makedirs(dp_dir, exist_ok=True)

for filename, content in dp_files_content.items():
    file_path = os.path.join(dp_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

print(f"DP algorithms filled in {dp_dir}")

"""
N-Queens Problem using Backtracking
"""

def solve_n_queens(n):
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    def backtrack(row=0):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack()
    return solutions


if __name__ == "__main__":
    n = 8
    sols = solve_n_queens(n)
    print(f"Total solutions for {n}-Queens: {len(sols)}")
    # Print first solution
    if sols:
        print("First solution:", sols[0])

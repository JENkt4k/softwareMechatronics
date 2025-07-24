"""
Sudoku Solver using Backtracking
"""

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in map(str, range(1, 10)):
        if valid(board, num, (row, col)):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = "."
    return False

def valid(board, num, pos):
    # Check row
    if num in board[pos[0]]:
        return False

    # Check column
    if any(board[i][pos[1]] == num for i in range(9)):
        return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                return (i, j)
    return None


if __name__ == "__main__":
    example_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    if solve_sudoku(example_board):
        for row in example_board:
            print(" ".join(row))
    else:
        print("No solution exists.")

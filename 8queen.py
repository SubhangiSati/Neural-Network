def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        if row - i >= 0 and board[row - i][col - i] == 1:
            return False
        if row + i < len(board) and board[row + i][col - i] == 1:
            return False
    return True

def solve_n_queens(board, col, solutions_found):
    if solutions_found[0] >= 2:  # Stop after finding 2 solutions
        return True

    if col >= len(board):
        solutions_found[0] += 1
        print("Solution", solutions_found[0])
        print_solution(board)
        print()
        return False

    found_solution = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, solutions_found):
                found_solution = True
            board[i][col] = 0

    return found_solution

def print_solution(board):
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))

n = 8
chessboard = [[0] * n for _ in range(n)]

solutions_found = [0]
solve_n_queens(chessboard, 0, solutions_found)


def is_safe(board, row, col):
    # Check if it's safe to place a queen at (row, col)
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_n_queens(n):
    solutions = []

    def backtrack(board, col):
        if col == n:
            # All queens are placed, add this solution
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                backtrack(board, col + 1)
                board[col] = -1  # Backtrack

    # Initialize the board with -1 (empty)
    board = [-1] * n
    backtrack(board, 0)
    
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            line = ['.'] * len(solution)
            line[row] = 'Q'
            print(''.join(line))
        print()

# Find and print all solutions for the 8-Queens problem
n = 8
solutions = solve_n_queens(n)
print_solutions(solutions)
print("Total Solutions:", len(solutions))

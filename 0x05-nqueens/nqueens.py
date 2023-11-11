"""Nqueens"""
import sys

def is_safe(board, row, col):
    """Check if a queen can be placed at the given position without attacking any other queen"""
    for i in range(row):
        # Check if there is a queen in the same column or in the diagonals
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n):
    """Base case: If all queens are placed, print the solution"""
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n)
            board[row] = -1

def n_queens(n):
    """Initialize the board as an array of -1's"""
    board = [-1] * n
    solve_n_queens(board, 0, n)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Parse the argument
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        # Solve the N-Queens problem
        n_queens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

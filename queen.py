# Function to initialize the N-Queens board and solve the problem
def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return
        for i in range(n):
            if is_safe(i, col):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions

# Function to print the N-Queens board
def print_board(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))

if __name__ == '__main__':
    n = int(input("Enter the value of n for N-Queens: "))
    
    solutions = solve_n_queens(n)
    
    print(f"Number of solutions for {n}-Queens: {len(solutions)}")
    
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        print_board(solution)
        print()

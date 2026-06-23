def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    if row == n:
        print("Solution Found:")
        print_board(board, n)
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = "Q"

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = "."

    return False


n = int(input("Enter the value of N: "))

board = [["." for _ in range(n)] for _ in range(n)]

if not solve_n_queens(board, 0, n):
    print("No Solution Exists")
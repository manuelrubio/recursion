import math

# Check if the digit at cell (row,col) is valid


def is_valid_candidate(row, col, digit, S):
    # Check conflict in column
    for k in range(0, 9):
        if k != col and digit == S[row][k]:
            return False

    # Check conflict in row
    for k in range(0, 9):
        if k != row and digit == S[k][col]:
            return False

    # Check conflict in box
    box_row = math.floor(row / 3)
    box_col = math.floor(col / 3)
    for k in range(0, 3):
        for m in range(0, 3):
            if (row != 3 * box_row + k
                    and col != 3 * box_col + m):
                if digit == S[3 * box_row + k][3 * box_col + m]:
                    return False

    return True

# Read a sudoku grid from a text file


def read_sudoku(filename):
    file = open(filename, 'r')
    S = [[None] * 9] * 9
    i = 0
    for line in file.readlines():
        S[i] = [int(x) for x in line.split(' ')]
        i = i + 1

    file.close()
    return S

# Print a sudoku grid on the console


def print_sudoku(S):
    for s in S:
        print(*s)


S = read_sudoku('sudoku01_input.txt')  # Some file
solve_sudoku_all_sols(0, 0, S)

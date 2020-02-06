""""Simple Sudoku problem solver using backtracking"""

EMPTY = 0

# The allegedly 'hardest' sudoku problem
sudoku_problem = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]]

"""
sudoku_problem = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku_solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]"""


def is_complete(board):
    return all(all(val is not EMPTY for val in row) for row in board)


def duplicates(arr):
    nums = {}
    for val in arr:
        if val in nums and val is not EMPTY:
            return True
        nums[val] = True
    return False


def find_empty_entry(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:
                return i, j
    return False


def rows_valid(board):
    for row in board:
        if duplicates(row):
            return False
    return True


def columns_valid(board):
    for j in range(len(board[0])):
        col_arr = [board[i][j] for i in range(len(board))]
        if duplicates(col_arr):
            return False
    return True


def blocks_valid(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block_arr = []
            for k in range(3):
                for l in range(3):
                    block_arr.append(board[i + k][j + l])
            if duplicates(block_arr):
                return False
    return True


def currently_valid(board):
    if not rows_valid(board):
        return False
    if not columns_valid(board):
        return False
    if not blocks_valid(board):
        return False
    return True


def solve_sudoku(board):
    if is_complete(board):
        return board

    r, c = find_empty_entry(board)
    for val in range(1, 10):
        board[r][c] = val
        if currently_valid(board):
            result = solve_sudoku(board)
            if is_complete(result):
                return result
        board[r][c] = EMPTY

    return board


def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")
            print(board[i][j], end=" ")
        print()


def main():
    solution = solve_sudoku(sudoku_problem)
    display_board(solution)

    # print("Is the solution the correct solution?")
    # print(solution == sudoku_solution)
    # print("Is the solution valid?")
    # print(currently_valid(sudoku_problem))


if __name__ == "__main__":
    main()

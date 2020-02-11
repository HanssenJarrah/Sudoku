""""Simple Sudoku problem solver using backtracking"""
import pygame, sys
import SudokuGUI

EMPTY = 0

"""
# The allegedly 'hardest' sudoku problem:
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
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]


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


def row_valid(board, row):
    if duplicates(board[row]):
        return False
    return True


def column_valid(board, column):
    col_arr = []
    for row in board:
        col_arr.append(row[column])
    if duplicates(col_arr):
        return False
    return True


def block_valid(board, row, column):
    block_arr = []
    block_r = (row // 3) * 3
    block_c = (column // 3) * 3
    for i in range(block_r, block_r + 3):
        for j in range(block_c, block_c + 3):
            block_arr.append(board[i][j])
    if duplicates(block_arr):
        return False
    return True


def currently_valid(board, row, column):
    if not row_valid(board, row):
        return False
    if not column_valid(board, column):
        return False
    if not block_valid(board, row, column):
        return False
    return True


def solve_sudoku(board):
    if is_complete(board):
        return board

    r, c = find_empty_entry(board)
    for val in range(1, 10):
        board[r][c] = val
        if currently_valid(board, r, c):
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
    SudokuGUI.draw_board()

    solution = solve_sudoku(sudoku_problem)
    display_board(solution)

    # print("Is the solution the correct solution?")
    print(solution == sudoku_solution)

    SudokuGUI.draw_board(solution)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()

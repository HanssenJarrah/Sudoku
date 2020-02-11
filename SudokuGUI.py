import pygame
import math

CELL_SIZE = 64
FONT_SCALE = 0.6
THICK_LINE = 3
THIN_LINE = 1
BG_COLOUR = (255, 255, 255)
FG_COLOUR = (0, 0, 0)
FNT_COLOUR = (0, 0, 0)


def get_cell_pos(row, column):
    x_offset = column * CELL_SIZE + column * THIN_LINE + ((column + 1) // 3) * THICK_LINE - ((column + 1) // 3) * THIN_LINE
    y_offset = row * CELL_SIZE + row * THIN_LINE + ((row + 1) // 3) * THICK_LINE - ((row + 1) // 3) * THIN_LINE
    return x_offset, y_offset


def draw_board(board=None):
    if board == None:
        board = []
    
    # Initialise the board
    pygame.init()
    size = width, height = 9 * CELL_SIZE + 6 * THIN_LINE + 2 * THICK_LINE, 9 * CELL_SIZE + 6 * THIN_LINE + 2 * THICK_LINE
    screen = pygame.display.set_mode(size)
    screen.fill(BG_COLOUR)

    # Draw the lines on the board
    for i in range(0, 8):
        offset = (i + 1) * CELL_SIZE + (i // 3) * THICK_LINE + i * THIN_LINE - (i // 3) * THIN_LINE
        start_pos = offset, 0
        end_pos = offset, height
        if (i + 1) % 3 == 0:
            pygame.draw.line(screen, FG_COLOUR, start_pos, end_pos, THICK_LINE)
            pygame.draw.line(screen, FG_COLOUR, start_pos[::-1], end_pos[::-1], THICK_LINE)
        else:
            pygame.draw.line(screen, FG_COLOUR, start_pos, end_pos, THIN_LINE)
            pygame.draw.line(screen, FG_COLOUR, start_pos[::-1], end_pos[::-1], THIN_LINE)

    if board:
        fnt = pygame.font.SysFont("sans", int(CELL_SIZE * FONT_SCALE))
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                text = fnt.render(str(val), True, FNT_COLOUR)
                offset = int(CELL_SIZE / 2 - text.get_width() / 2), int(CELL_SIZE / 2 - text.get_height() / 2)
                text_pos = get_cell_pos(r, c)
                text_pos = text_pos[0] + offset[0], text_pos[1] + offset[1]
                screen.blit(text, text_pos)

    pygame.display.update()

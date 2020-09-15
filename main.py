import pygame

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Visualizer")


# COLORs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Block:
    def __init__(self, x, y, diff, rows):
        self.x = x * diff
        self.y = y * diff
        self.diff = diff
        self.rows = rows
        self.color = WHITE

    def add_black(self):
        self.color = BLACK

    def remove_color(self):
        self.color = WHITE

    def add_start(self):
        self.color = BLUE

    def add_end(self):
        self.color = RED

    def make_block(self):
        pygame.draw.rect(
            WIN, self.color, (self.x, self.y, self.diff, self.diff))


def make_grid(win, width, rows):
    grid = []
    diff = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(Block(i, j, diff, rows))
    return grid


# Draws lines (Static)
def draw_grid(win, rows, width):
    diff = width//rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * diff), (width, i * diff))
    for j in range(rows):
        pygame.draw.line(win, BLACK, (j * diff, 0), (j * diff, width))


def get_mouse_pos(grid, win, width, rows):
    x, y = pygame.mouse.get_pos()

    diff = width // rows
    row = x // diff
    col = y // diff

    return row, col


def draw(win, width, rows, grid):
    win.fill(WHITE)

    for row in grid:
        for block in row:
            block.make_block()

    draw_grid(win, width, rows)
    pygame.display.update()


def main(win, width):
    running = True
    rows = 60  # No. of rows and columns
    start_node = 0
    end_node = 0

    # To make blocks on the screen
    grid = make_grid(win, width, rows)

    while running:
        draw(win, rows, width, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Mouse left click event
            if pygame.mouse.get_pressed()[0]:
                row, col = get_mouse_pos(grid, win, width, rows)
                spot = grid[row][col]

                if start_node == 0 and spot.color == WHITE:
                    spot.add_start()
                    start_node = 1

                if end_node == 0 and spot.color == WHITE:
                    spot.add_end()
                    end_node = 1

                if spot.color == RED:
                    spot.add_end()

                if spot.color == BLUE:
                    spot.add_start()

                if spot.color == WHITE:
                    spot.add_black()

            # Mouse right click event
            if pygame.mouse.get_pressed()[2]:
                row, col = get_mouse_pos(grid, win, width, rows)
                spot = grid[row][col]

                if spot.color == BLUE:
                    spot.remove_color()
                    start_node = 0
                elif spot.color == RED:
                    spot.remove_color()
                    end_node = 0
                else:
                    spot.remove_color()

        pygame.display.update()

    pygame.quit()


main(WIN, WIDTH)

import pygame

def algorithm(grid, win, draw):
    blocks = [block for row in grid for block in row]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for block in blocks:
            for neighbor in block.neighbors:
                if not neighbor.barrier() or not is_visited():
                    neighbor.set_visited()
                    draw()
        break

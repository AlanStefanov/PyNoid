import pygame

def create_bricks(screen_width, rows, cols):
    brick_width = screen_width // cols
    brick_height = 20
    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick = pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height)
            bricks.append(brick)
    return bricks

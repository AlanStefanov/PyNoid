import pygame

def create_bricks(screen_width, rows, cols):
    brick_width = screen_width // cols
    brick_height = 40  # Altura fija para los ladrillos
    bricks = []
    brick_images = [
        'assets/images/brick-red.png',
        'assets/images/brick-green.png',
        'assets/images/brick-yellow.png',
        'assets/images/brick-grey.png',
        'assets/images/brick-purple.png'
    ]
    for row in range(rows):
        for col in range(cols):
            brick_image = pygame.image.load(brick_images[row % len(brick_images)])
            brick_image = pygame.transform.scale(brick_image, (brick_width, brick_height))
            brick_rect = brick_image.get_rect(topleft=(col * brick_width, row * brick_height))
            bricks.append((brick_image, brick_rect))
    return bricks

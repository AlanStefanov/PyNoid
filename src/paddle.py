import pygame

class Paddle:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/images/paddle-blue.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 10

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # Limitar la paleta dentro de los límites de la pantalla
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))

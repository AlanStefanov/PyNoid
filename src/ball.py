import pygame

class Ball:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/images/ball-blue.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = 5
        self.speed_y = 5

    def move(self, screen_width, screen_height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y
        if self.rect.bottom >= screen_height:
            pass

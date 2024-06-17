import pygame
import sys
from paddle import Paddle
from ball import Ball
from brick import create_bricks

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('PyNoid')
        self.clock = pygame.time.Clock()
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.paddle = Paddle(self.screen_width // 2 - 50, self.screen_height - 40)
        self.ball = Ball(self.screen_width // 2, self.screen_height // 2)
        self.bricks = create_bricks(self.screen_width, 5, 10)

    def show_welcome_screen(self):
        self.screen.fill(self.black)
        welcome_text = self.font.render('Bienvenido a PyNoid', True, self.white)
        instruction_text = self.small_font.render('Presione Enter para comenzar', True, self.white)
        self.screen.blit(welcome_text, (self.screen_width//2 - welcome_text.get_width()//2, self.screen_height//2 - welcome_text.get_height()))
        self.screen.blit(instruction_text, (self.screen_width//2 - instruction_text.get_width()//2, self.screen_height//2 + 20))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False

    def run(self):
        self.show_welcome_screen()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            self.paddle.move(keys, self.screen_width)
            self.ball.move(self.screen_width, self.screen_height)
            if self.ball.rect.colliderect(self.paddle.rect) and self.ball.speed_y > 0:
                self.ball.speed_y = -self.ball.speed_y
            for brick in self.bricks[:]:
                if self.ball.rect.colliderect(brick):
                    self.ball.speed_y = -self.ball.speed_y
                    self.bricks.remove(brick)
            if self.ball.rect.bottom >= self.screen_height:
                running = False
            self.screen.fill(self.black)
            pygame.draw.rect(self.screen, self.white, self.paddle.rect)
            pygame.draw.ellipse(self.screen, self.white, self.ball.rect)
            for brick in self.bricks:
                pygame.draw.rect(self.screen, self.white, brick)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

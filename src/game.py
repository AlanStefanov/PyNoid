import pygame
import sys
from paddle import Paddle
from ball import Ball
from brick import create_bricks

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('PyNoid')
        self.clock = pygame.time.Clock()
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.level = 1
        self.paused = False

        # Cargar sonidos
        self.brick_break_sound = pygame.mixer.Sound('assets/sounds/brick_break.wav')
        self.paddle_hit_sound = pygame.mixer.Sound('assets/sounds/paddle_hit.wav')

        # Cargar fondo
        self.background = pygame.image.load('assets/images/background.png').convert()
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))

        self.setup_level()

    def setup_level(self):
        self.paddle = Paddle(self.screen_width // 2 - 50, self.screen_height - 40)
        self.ball = Ball(self.screen_width // 2, self.screen_height // 2)
        self.bricks = create_bricks(self.screen_width, 5 + self.level, 10)

    def show_welcome_screen(self):
        self.screen.fill(self.black)
        welcome_text = self.font.render('Bienvenido a PyNoid', True, self.white)
        instruction_text = self.small_font.render('Presione Enter para continuar', True, self.white)
        self.screen.blit(welcome_text, (self.screen_width//2 - welcome_text.get_width()//2, self.screen_height//2 - welcome_text.get_height() - 20))
        self.screen.blit(instruction_text, (self.screen_width//2 - instruction_text.get_width()//2, self.screen_height//2 + 20))
        pygame.display.flip()
        self.wait_for_enter()

    def show_tutorial_screen(self):
        self.screen.fill(self.black)
        tutorial_text = [
            "Controles:",
            "Flechas Izquierda/Derecha o A/D: Mover la paleta",
            "Espacio: Pausar/Continuar el juego",
            "Objetivo: Romper todos los ladrillos con la bola",
            "",
            "Presione Enter para comenzar el juego"
        ]
        for i, line in enumerate(tutorial_text):
            line_text = self.small_font.render(line, True, self.white)
            self.screen.blit(line_text, (self.screen_width//2 - line_text.get_width()//2, self.screen_height//2 - 60 + i * 30))
        pygame.display.flip()
        self.wait_for_enter()

    def show_level_complete_screen(self):
        self.screen.fill(self.black)
        level_complete_text = self.font.render(f'Nivel {self.level} Completado!', True, self.white)
        next_level_text = self.small_font.render('Presione Enter para el siguiente nivel', True, self.white)
        self.screen.blit(level_complete_text, (self.screen_width//2 - level_complete_text.get_width()//2, self.screen_height//2 - level_complete_text.get_height()))
        self.screen.blit(next_level_text, (self.screen_width//2 - next_level_text.get_width()//2, self.screen_height//2 + 20))
        pygame.display.flip()
        self.wait_for_enter()

    def show_game_over_screen(self):
        self.screen.fill(self.black)
        game_over_text = self.font.render('Has Perdido', True, self.white)
        retry_text = self.small_font.render('Presione Enter para volver al menú', True, self.white)
        self.screen.blit(game_over_text, (self.screen_width//2 - game_over_text.get_width()//2, self.screen_height//2 - game_over_text.get_height()))
        self.screen.blit(retry_text, (self.screen_width//2 - retry_text.get_width()//2, self.screen_height//2 + 20))
        pygame.display.flip()
        self.wait_for_enter()

    def show_pause_screen(self):
        pause_text = self.font.render('Pausa', True, self.white)
        continue_text = self.small_font.render('Presione Espacio para continuar', True, self.white)
        self.screen.blit(pause_text, (self.screen_width//2 - pause_text.get_width()//2, self.screen_height//2 - pause_text.get_height()))
        self.screen.blit(continue_text, (self.screen_width//2 - continue_text.get_width()//2, self.screen_height//2 + 20))
        pygame.display.flip()

    def wait_for_enter(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False

    def wait_for_space(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False

    def run(self):
        self.show_welcome_screen()
        self.show_tutorial_screen()
        while True:
            running = True
            self.setup_level()
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.paused = not self.paused

                if self.paused:
                    self.show_pause_screen()
                    self.wait_for_space()
                    continue

                keys = pygame.key.get_pressed()
                self.paddle.move(keys, self.screen_width)
                self.ball.move(self.screen_width, self.screen_height)

                # Colisiones de la pelota con la paleta y los ladrillos
                if self.ball.rect.colliderect(self.paddle.rect) and self.ball.speed_y > 0:
                    self.ball.speed_y = -self.ball.speed_y
                    self.paddle_hit_sound.play()

                for brick_image, brick_rect in self.bricks[:]:
                    if self.ball.rect.colliderect(brick_rect):
                        self.ball.speed_y = -self.ball.speed_y
                        self.bricks.remove((brick_image, brick_rect))
                        self.brick_break_sound.play()

                # Verificación de condiciones de fin de juego
                if self.ball.rect.bottom >= self.screen_height:
                    running = False

                if not self.bricks:
                    self.level += 1
                    self.show_level_complete_screen()
                    break

                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.paddle.image, self.paddle.rect)
                self.screen.blit(self.ball.image, self.ball.rect)
                for brick_image, brick_rect in self.bricks:
                    self.screen.blit(brick_image, brick_rect)
                pygame.display.flip()
                self.clock.tick(60)

            self.show_game_over_screen()

if __name__ == '__main__':
    game = Game()
    game.run()

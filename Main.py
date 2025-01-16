import pygame, sys
from settings import *
from stuff import Stuff

class Main:
    """
    Initializes game window, handles the game while True loop, and controls the status of the game such as pulsing.

    Attributes:
        screen (pygame.Surface): 
        clock (pygame.time.Clock): Manages the frame rate of the game loop.
        font (pygame.font.Font): Font object used for rendering text on the screen.
        stuff (Stuff): A Stuff object that handles game-specific logics.
        game_active (bool): Tracks whether the main game is currently active.
        pulsing (bool): Tracks whether the pulsing state is active (pausing the game with a visual overlay).
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.stuff = Stuff()
        self.pulsing = False
    
    def start_screen(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render('Press ENTER to Start', True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
                    self.stuff.create_map()

    def pulse_screen(self):
        surface = pygame.Surface((WIDTH, HEIGHT))
        surface.fill((0, 0, 0))
        surface.set_alpha(150)
        self.screen.blit(surface, (0, 0))
        
        text = self.font.render('Pulsing', True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def death_screen(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("You're dead. Press R to restart, ESC to quit", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.stuff.reset()
                        waiting = False
                        self.stuff.create_map()
                    elif event.key == pygame.K_ESCAPE:
                        self.stuff.reset()
                        waiting = False
                        self.start_screen()

    def run(self):
        self.start_screen()
 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pulsing = not self.pulsing
                    if event.key == pygame.K_k:
                        self.death_screen()
            
            if self.stuff.get_player().get_heart()[0] <= 0:
                self.death_screen()

            if self.pulsing:
                self.pulse_screen()
            else:
                self.screen.fill('white')
                self.stuff.run()
             
                pygame.display.update()

            self.clock.tick(FPS)

if __name__ == '__main__':
    main = Main()
    main.run()

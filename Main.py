import pygame, sys
from settings import *
from stuff import Stuff
from Character import Player

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.stuff = Stuff()
        self.game_active = False
        self.pulsing = False
        self.font = pygame.font.Font(None, 50)
    
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
                    self.game_active = True
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
                        self.stuff.clear_map()
                        waiting = False
                        self.game_active = True
                        self.stuff.create_map()
                    elif event.key == pygame.K_ESCAPE:
                        self.stuff.clear_map()
                        waiting = False
                        self.start_screen()

    def run(self):
        if not self.game_active:
            self.start_screen()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pulsing = not self.pulsing
                    if event.key == pygame.K_k or self.stuff.get_player().get_heart()[0] <= 0:
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

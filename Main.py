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
    
    def start_screen(self):
        font = pygame.font.Font(None,50)
        text = font.render('Press SPACE to Start',True,(255,255,255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    def run(self):
        if not self.game_active:
            self.start_screen()
            self.stuff.create_map()
            self.game_active = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('white')
            self.stuff.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    main = Main()
    main.run()

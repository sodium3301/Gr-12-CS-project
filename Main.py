import pygame, sys
from settings import *
from stuff import Stuff
from Character import Player

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.stuff = Stuff()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.stuff.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    main = Main()
    main.run()


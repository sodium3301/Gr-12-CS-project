import pygame, sys
from settings import *
from stuff import Stuff
from character import Player

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.stuff = Stuff()

        # 33:45 on the video --Lawrence
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()

        # self.create_map()
    
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







import pygame
from settings import *
from tiles import Tile
from Character import Player

class Stuff:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        # Tile((250,250), [self.visible_sprites])
        pass
        #make the map here
        
    def run(self):
        self.visible_sprites.draw(self.display_surface)
        
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('/Users/ian/Desktop/Gr12 CS game/Gr-12-CS-project/graphics/rock.png').convert_alpha
        self.rect = self.image.get_rect(topleft = pos)
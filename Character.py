import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        #super().__init__(groups)
        self.surf = pygame.image.load('graphics/rock.jpg').convert_alpha()
        self.rect = self.surf.get_rect(topleft = pos)
    
    
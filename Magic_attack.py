import pygame

class Magic():
    dmg = 10.0
    scaling = 1.0

    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
    def draw():

    def update():
    
    

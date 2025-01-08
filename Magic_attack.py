import pygame
from Character import Player
from settings import *

class Magic(pygame.sprite.Sprite):
    

    def __init__(self, group):
        self.dmg = 15.0
        self.scaling = 1.0
        self.direction = Player.get_direction()
        self.pos = (Player.rect.x, Player.rect.y)
        self.speed = 1
        super().__init__(group)

        self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = self.pos)
        
    def add_magic_scaling(self, factor):
        self.scaling += factor
        return self.scaling
    
    def get_total_dmg(self):
        self.total_dmg = self.dmg * self.scaling
        return self.total_dmg
    
    def collision(self):
        self.total_dmg = self.dmg * self.scaling
        self.kill()
        return self.total_dmg
    
    def move(self, speed):
        if self.direction == (1,0):
            self.rect.x += speed
        elif self.direction == (-1,0):
            self.rect.x -= speed
        elif self.direction == (0,1):
            self.rect.y += speed
        elif self.direction == (0,-1):
            self.rect.y -= speed

        if self.x > WIDTH or self.y > HEIGHT or self.x < 0 or self.y < 0:
            self.kill()
        

    #def draw():

    #def update():    

projectiles = pygame.sprite.Group()
bolt = Magic(projectiles)
fire = Magic(projectiles)
bolt.add_magic_scaling(0.5)
fire.add_magic_scaling(1.2)

print(projectiles)
    
print(fire.get_total_dmg(), bolt.collision())
fire.add_magic_scaling(0.5)
print(fire.get_total_dmg(), bolt.get_total_dmg())
print(projectiles)
    

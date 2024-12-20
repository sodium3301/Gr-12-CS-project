import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_spirtes):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_spirtes
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction = 0
        
        if keys[pygame.K_LEFT]:
            self.direction.y = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.y = 1
        else:
            self.direction = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            if direction == 'horizontal':
                for sprite in self.obstacle_sprites:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.x > 0:
                            self.rect.bottom = sprite.rect.top
                        if self.direction.x < 0:
                            self.rect.top = sprite.rect.bottom
    
    def update(self):
        self.input()
        self.move(self.speed)

import pygame
from settings import *
from entities import Entity
# from support import import_folder

class Player(Entity):
    def __init__(self, pos, groups, obstacle_spirtes):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5
        self.attacking = False
        self.attack_cool = 400
        self.attack_time = None
        self.direction = pygame.math.Vector2()
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.obstacle_sprites = obstacle_spirtes
    
    def import_player_assets(self):
        character_path = '' #
        self.animations = {'up':[],'down':[],'left':[],'right':[],
                           'up_idle':[],'down_idle':[],'left_idle':[],'right_idle':[],
                           'up_attack':[],'down_attack':[],'left_attack':[],'right_attack':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = '' # import_folder

    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('attack')
        if keys[pygame.K_LCTRL] and not self.attacking:
            self.attacking = True            
            self.attack_time = pygame.time.get_ticks()
            print('magic')

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        if self.attacking:
            self.direction /= 1.5

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cool:
                self.attacking = False

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
    
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_direction(self):
        return self.direction

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status += "_idle"
        
        if self.attacking:
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status += "_attack"
        else:
            if 'attack' in self.status:
                self.status.replace("_attack",'')
        
    def update(self):
        self.input()
        self.cooldown()
        self.get_status()
        # self.animate()
        self.move(self.speed)
import pygame
from settings import *
from entities import Entity
# from Character import Player

class Enemy(Entity):
    def __init__(self, monster_name,pos,groups, obstacle_sprites):
        
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(monster_name)
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft = pos)

        # enemy movment
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        #stat
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.dmg = monster_info['dmg']
        self.attack_type = monster_info['attack_type']
        self.knockback = monster_info['knockback']
        self.attack_radius = monster_info['attack_radius']
        self.agro_radius = monster_info['agro_radius']


    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        p_vec = pygame.math.Vector2(player.rect.center)
        
        distance = (p_vec - enemy_vec).magnitude()
        direction = (p_vec-enemy_vec).normalize()

        if distance > 0:
            direction = (p_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return(distance, direction)

    def import_graphics(self, name):
         self.animation = {'idle':[], 'move':[], 'attack':[]}

    def status(self, player):
        distance = get_player_distance_direction(player)[0]

        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.agro_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def update(self):
        self.status()
        self.move(self.speed)
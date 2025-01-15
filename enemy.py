import pygame
import random
from settings import *
from entity import Entity
from player import Player

class Enemy(Entity):
    def __init__(self, monster_name,pos,groups, obstacle_sprites, damage_player):
        
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'
        self.status = 'idle'

        # graphics setup
        self.import_graphics(monster_name)

        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
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

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        self.damage_player = damage_player

        self.vulnerable = True
        self.hit_time = None
        self. invincibility_dur = 300


    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        p_vec = pygame.math.Vector2(player.rect.center)
        distance = (p_vec - enemy_vec).magnitude()
        direction = (p_vec-enemy_vec).normalize()
        if distance > 0:
            direction = (p_vec-enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return(distance, direction)

    def import_graphics(self, name):
         self.animation = {'idle':[], 'move':[], 'attack':[]}

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius:
            self.status = 'attack'

        elif distance <= self.agro_radius:
            self.status = 'move'
            
        else:
            self.status = 'idle'



    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
                
        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_dur:
                self.vulnerable = True


    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()

                
            else:
                pass
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable=False


    def check_death(self):
        if self.health <= 0:
            self.kill()

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.knockback

    def action(self, player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.dmg)
        
        elif self.status == 'move' :
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    
    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.check_death()
        self.cooldown()

    def enemy_update(self, player):
        self.get_status(player)
        self.action(player)
      

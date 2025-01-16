import pygame
import random
from settings import *
from entity import Entity
from Character import Player

"""
    The `Enemy` class represents an enemy entity in the game world, responsible for simulating hostile AI behavior.

    Purpose:
    - The `Enemy` class provides functionality for enemies to interact with the player and the game environment.
    - It manages enemy behavior such as movement, attacking, and taking damage.
    - It includes systems for tracking the enemy's health, status (idle, move, attack), and cooldowns for attacks and invincibility.

    key features:
    
    dynamic interaction with the player
       - tracks the player's position to determine the enemy's actions (e.g., attacking, moving toward the player, and getting knocked back when being attacked).
       - implements an agro radius for triggering movement and an attack radius for initiating attacks.

    health and damge system
       - tracks the enemy's health and manages damage received from the player.
       - supports invincibility frames to prevent repeated damage within a short timeframe.

    AI Behavior:
       - implements different states such as idle, moving, and attacking, based on the player's position.
       - uses a distance-based approach to determine the appropriate state.

    Knockback mechanics:
       - Handles reactions to player attacks by applying knockback effects when the enemy is hit.

    Scoring:
       - Adds points to the player's score upon the enemy's death.
       - Integrates with the player's scoring system through a callback.

    Integration:
    - The `Enemy` class relies on the `Entity` base class for shared functions like movement.
    - It interacts with the `Player` class to determine distance, apply damage, and update player stats.
    - Utilizes external game settings (`monster_data`) to initialize attributes like health, speed, and damage.

    """


class Enemy(Entity):

    """
    Initializes the `Enemy` instance with its attributes and behaviors.

    instances:
        monster_name (str): The name of the enemy type, used to fetch stats and animations.
        pos (tuple): Initial position of the enemy (x, y).
        groups (list): List of sprite groups the enemy belongs to.
        obstacle_sprites (pygame.sprite.Group): Group of sprites that act as obstacles.
        damage_player (function): Callback function to apply damage to the player.
        add_score (function): Callback function to increment the player's score upon enemy death.
    """
    def __init__(self, monster_name,pos,groups, obstacle_sprites, damage_player, add_score):
        
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'
        self.status = 'idle'

        # graphics setup
        self.import_graphics(monster_name)

        self.image = pygame.image.load('graphics/test/enemy.png').convert_alpha()
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
        self. invincibility_dur = 500

        self.add_score = add_score
  
  

    """ 
    Calculates the distance and direction from the enemy to the player.

    uses enemy vector and player vector to calculate their magnitude and direciton
    """
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


    """ 
    imports graphics for three states(place holder)
    """
    def import_graphics(self, name):
         self.animation = {'idle':[], 'move':[], 'attack':[]}

    """
    used to identify if the distance between the player and enemy would agro the enemey or start attacking
    """
    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius:
            self.status = 'attack'

        elif distance <= self.agro_radius:
            self.status = 'move'
            
        else:
            self.status = 'idle'


    """ 
    deals with cooldown timers for attacks and invincibility periods
    """
    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
                
        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_dur:
                self.vulnerable = True

    """
    Applies damage to the enemy and handles invincibility after being hit.
    """
    def get_damage(self, player, attack_type):
        if self.vulnerable:
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                pass
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable=False

    """
    check if the enemy's health is 0 or below, then it will removed
    """
    def check_death(self):
        if self.health <= 0:
            self.kill()
            self.add_score(1)
      
            
  

    """
    deals knock back to the enemy when got hit
    """
    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.knockback


    """
    Determines the enemy's action (attack, move, or idle) based on its status.
    """
    def action(self, player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.dmg)
        
        elif self.status == 'move' :
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    

    """
    Updates the enemy's behavior and status each frame.
    """
    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.check_death()
        self.cooldown()

    """
    Updates the enemy's status and actions relative to the player.
    """
    def enemy_update(self, player):
        self.get_status(player)
        self.action(player)
      

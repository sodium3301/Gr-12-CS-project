import pygame
from os import walk
from settings import *
from entity import Entity
# from support import import_folder

class Player(Entity):
    '''
    Player class that controls player's status and activities.

    Methods:
    '''
    def __init__(self, groups, obstacle_spirtes, create_attack, destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (MIDPOINT * TILESIZE, MIDPOINT * TILESIZE))
        self.hitbox = self.rect.inflate(-10, -10)
        
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # movement
        self.direction = pygame.math.Vector2()

        # collision
        self.obstacle_sprites = obstacle_spirtes

        # weapon
        self.attacking = False
        self.attack_cool = 400
        self.attack_time = None
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

        # stats
        self.stats = {'heart':6,'energy':60,'attack':10,'magic':4,'speed':5}
        self.heart = self.stats['heart']
        self.energy = self.stats['energy']
        self.speed = self.stats['speed']
        self.exp = 0
    
    def import_folder(path):
        '''
        Helper method for import_player_asset(self)
        '''
        surface_list = []

        for _,__,img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

        return surface_list

    def import_player_assets(self):
        '''
        Loads the full path into self.animations.
        '''
        character_path = 'graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = Player.import_folder(full_path)

    def input(self):
        '''
        Detects input; controls movements and attacks
        '''
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
            self.destroy_attack()
            self.create_attack()
        if keys[pygame.K_LCTRL] and not self.attacking:
            self.attacking = True            
            self.attack_time = pygame.time.get_ticks()

    def cooldown(self):
        '''
        Resets attacking and destroys attack after the cooldown time
        '''
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cool:
                self.attacking = False
                self.destroy_attack()
    
    def animate(self):
        '''
        Animates the main character by lopping over images in self.animation
        '''
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_direction(self):
        '''
        Returns self.direction.
        '''
        return self.direction

    def get_position(self):
        '''
        Returns self.rect.
        '''
        return self.rect

    def get_heart(self):
        '''
        Return current hp and maximum hp
        '''
        return [self.heart, self.stats['heart']]

    def get_status(self):
        '''
        Manipulate self.status, the key for self.animation in animate().
        '''
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
        
        # return self.status

    def update(self):
        self.input()
        self.cooldown()
        self.get_status()
        self.animate()
        self.move(self.speed)
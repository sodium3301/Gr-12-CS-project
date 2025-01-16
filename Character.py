import pygame
from os import walk
from settings import *
from entity import Entity
from support import import_folder

class Player(Entity):
    '''
    Controls the player's image (animation and frames), 
    status (direction + idle or attacking) and activities such as attack and cooldown. 

    Attributes:
        groups (list[str]): The sprite groups the player belongs to.
        image (Surface): Stores the image of the player.
        rect (Rect): The rect of the player.
        hitbox (Rect): The hitbox of the player shrinks compared to rect.
        status (str): The direction, idleness, and whether the player is attacking.
        frame_index (int): The index used to access frames of animation.
        animation_speed (float): The speed which frame_index loops.
        stats (dict[int]): Dictionary holding player's default health, energy, attack, magic, and speed.
        heart (int): Stores current number of hearts of the player.
        energy (int): Stores current energy of the player.
        speed (int): Stores current speed of the player.

    Methods:
        import_player_assets(): Loads the dictionary with frames of surfaces found in the path
        get_x_pos(): Returns self.rect.centerx
        get_y_pos(): Returns self.rect.centery
        input(): Produces basic status and direction (Vector2) by detecting keys pressed
        animate(): Updates self.image with frames of surfaces from self.animatons
        get_direction(): Returns current direction.
        get_heart(): Returns current and max hp.
        get_status(): Produces the full status.
        update(): Updates the position, status, and image of the player.

    '''
    def __init__(self, groups, obstacle_spirtes, create_attack, destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (MIDPOINT * TILESIZE, MIDPOINT * TILESIZE))
        self.hitbox = self.rect.inflate(-10, -10)
        
        # animation
        self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.import_player_assets()

        # movement
        self.attacking = False
        self.attack_cool = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_spirtes

        # weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

        # magic
        # self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None
        #self.switch_duration_cooldown = 200

        # stats
        self.stats = {'heart':20,'energy':60,'attack':10,'magic':4,'speed':5}
        self.heart = self.stats['heart']
        self.energy = self.stats['energy']
        self.speed = self.stats['speed']
        self.exp = 0
    
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_dur = 100

        self.score = 0



    def import_player_assets(self):
        """
        Produce the full path to the set of frames of a status and loads them as surfaces into the dictionary self.animations.
        """
        character_path = 'graphics/player/'

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def get_x_pos(self):
        """
        get_x_pos(): Returns the x position of the center of the player rect.
        """
        return self.rect.centerx
    
    def get_y_pos(self):
        """
        get_y_pos(): Returns the y position of the center of the player rect.
        """
        return self.rect.centery

    def input(self):
        """
        input(): Produce base of self.status and direction (Vector2) by detecting keys like WASD.
        """
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
            style = list(magic_data.keys())[self.magic_index]
            strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
            cost = list(magic_data.values())[self.magic_index]['cost']
            self.create_magic(style, strength, cost)

        if keys[pygame.K_e] and self.can_switch_magic:
            self.can_switch_magic = False
            self.magic_switch_time = pygame.time.get_ticks()
            
            if self.magic_index < len(list(magic_data.keys())) - 1:
                self.magic_index += 1
            else:
                self.magic_index = 0

            self.magic = list(magic_data.keys())[self.magic_index]        

    def cooldown(self):

        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cool:
                self.attacking = False
                self.destroy_attack()

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_dur:
                self.vulnerable = True
                # print(self.vulnerable)
    
    def animate(self):
        """
        Updates self.image with frames of surfaces from self.animatons
        """
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_direction(self):
        """
        Returns current direction as a Vector2.
        """
        return self.direction

    def get_heart(self):
        """
        Returns current hp and max hp as a tuple.
        """
        return [self.heart, self.stats['heart']]

    def get_status(self):
        """
        Adds _idle or _attack to self.status that gained its base from animate() to compose the key to access self.animations.
        """
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
        
    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        # print(base_damage + weapon_damage)
        return base_damage + weapon_damage

    def update(self):
        self.input()
        self.cooldown()
        self.get_status()
        self.animate()
        self.move(self.speed)
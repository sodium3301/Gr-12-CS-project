import pygame

"""
The 'Weapon' class represents a weapon used by the player in the game. It handles the weapon's appearance and placement relative to the player's current position and direction.
"""

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        direction = player.status.split('_')[0]
        self.sprite_type = 'weapon'


        #graphics
        full_path = f'graphics/melee sprites/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        #placement for the weapon
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-64, 16))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(64, 16))     
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(0, -64))  
        elif direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(0, 64))         
        else:
            self.rect = self.image.get_rect(center = player.rect.center)




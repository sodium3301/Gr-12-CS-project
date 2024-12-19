import pygame

class Melee(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        self.dmg = 11.0
        self.scaling = 1.0
        super().__init__(group)

        #self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        #self.rect = self.image.get_rect(topleft = pos)
        
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

    #def draw():         

    #def update():    

# projectiles = pygame.sprite.Group()
# bolt = Melee((0,0), projectiles)
# fire = Melee((0,0), projectiles)
# bolt.add_magic_scaling(0.5)
# fire.add_magic_scaling(1.2)

# print(projectiles)
    
# print(fire.get_total_dmg(), bolt.collision())
# fire.add_magic_scaling(0.5)
# print(fire.get_total_dmg(), bolt.get_total_dmg())
# print(projectiles)
    

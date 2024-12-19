import pygame

class Ranged(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        self.dmg = 11.0
        self.scaling = 1
        super().__init__(group)

        #self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        #self.rect = self.image.get_rect(topleft = pos)
        
    def add_ranged_scaling(self, factor):
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
# arrow = Ranged((0,0), projectiles)
# bullet = Ranged((0,0), projectiles)
# arrow.add_ranged_scaling(0.5)
# bullet.add_ranged_scaling(1.2)

# print(projectiles)
    
# print(arrow.get_total_dmg(), bullet.collision())
# arrow.add_ranged_scaling(0.5)
# print(bullet.get_total_dmg(), arrow.get_total_dmg())
# print(projectiles)
    

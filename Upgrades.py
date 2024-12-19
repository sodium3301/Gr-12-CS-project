import pygame
from Magic_attack import Magic
from Melee_attack import Melee
from Ranged_attack import Ranged

projectiles = pygame.sprite.Group()

bolt = Ranged((0,0), projectiles)
magic = Magic((0,0), projectiles)

print(projectiles)
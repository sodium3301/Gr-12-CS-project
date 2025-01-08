import pygame
from settings import *
from tiles import Tile
from Character import Player
from enemy import Enemy

class Stuff:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        # Player((250,250), [self.visible_sprites])
        for row_index, row in enumerate(worldMap):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacles_sprites)
                if col == 'y':
                    self.enemy = Enemy('monster',(x,y), [self.visible_sprites], self.obstacles_sprites)
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player):
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		for sprite in sorted(self.sprites(),key = lambda sprite:sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

import pygame
from settings import *


"""
The UI class handles the game's user interface, including health display and score rendering.
"""
class UI:
	def __init__(self, player):
		self.display_surface = pygame.display.get_surface()
		self.player = player
		self.full_heart = pygame.transform.scale(pygame.image.load('graphics/full_heart.png').convert_alpha(), (30,30))
		self.half_heart = pygame.transform.scale(pygame.image.load('graphics/half_heart.png').convert_alpha(), (30,30))
		self.empty_heart = pygame.transform.scale(pygame.image.load('graphics/empty_heart.png').convert_alpha(), (30,30))

		self.font = pygame.font.Font(None, 50)
		# 3:12:08


	"""
	Displays the player's score in the bottom-right corner of the screen.
	"""
	def show_score(self, score):
		text_surf = self.font.render('score: ' + str(int(score)), False, text_colour)
		x = self.display_surface.get_size()[0]-20
		y = self.display_surface.get_size()[1]-20

		text_rect = text_surf.get_rect(bottomright = (x, y))

		self.display_surface.blit(text_surf, text_rect)

	def draw_heart(self):
		
		hp = self.player.get_heart()[0]
		max_hp = self.player.get_heart()[1]
		x_start = 20
		y = 10
		space = 35
		full = hp // 2
		half = hp % 2
		empty = (max_hp // 2) - full - half
		count = 0

		for i in range(full):
			x = x_start + count * space
			self.display_surface.blit(self.full_heart, (x, y))
			count += 1
		for i in range(half):
			x = x_start + count * space
			self.display_surface.blit(self.half_heart, (x, y))
			count += 1
		for i in range(empty):
			x = x_start + count * space
			self.display_surface.blit(self.empty_heart, (x, y))
			count += 1

	def display(self, player):

		self.show_score(player.score)

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
	
	def enemy_update(self, player):
		enemy_sprite = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprite:
			enemy.enemy_update(player)
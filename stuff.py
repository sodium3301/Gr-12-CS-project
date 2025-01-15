import pygame

from settings import *
from tiles import Tile
from Character import Player
from enemy import Enemy
from ui import UI
import random
from weapon import Weapon

class Stuff:
	def __init__(self):

		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacles_sprites = pygame.sprite.Group()
		
		# attack sprites
		self.current_attack  =None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		self.ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1  # Custom event for enemy spawning
		pygame.time.set_timer(self.ENEMY_SPAWN_EVENT, 3000)  # Spawn every 3 seconds 
		print(self.ENEMY_SPAWN_EVENT)
		
		self.last_spawn_time = pygame.time.get_ticks()  # Store the initial time
		self.enemy_spawn_delay = 3000

		self.create_map()

		self.ui = UI()

		self.full_heart = pygame.transform.scale(pygame.image.load('graphics/full_heart.png').convert_alpha(), (30,30))
		self.half_heart = pygame.transform.scale(pygame.image.load('graphics/half_heart.png').convert_alpha(), (30,30))
		self.empty_heart = pygame.transform.scale(pygame.image.load('graphics/empty_heart.png').convert_alpha(), (30,30))

	def create_map(self):
		world_map = [['x' if random.random() < 0.02 else '' for _ in range(300)] for _ in range(300)]
		world_map[25][25] = 'p'
		world_map[20][20] = 'y'

		for row_index, row in enumerate(world_map):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x': 
					Tile((x,y), [self.visible_sprites,self.obstacles_sprites])
					pass
				if col == 'p':
					# self.player = Player((x,y), [self.visible_sprites], self.obstacles_sprites, self.create_attack)
					pass

				if col == 'y':
					Enemy(
						'monster',
		   				(x,y),
						[self.visible_sprites, self.attackable_sprites], 
						self.obstacles_sprites)
		self.player = Player((2000,1430), 
					   [self.visible_sprites], 
					   self.obstacles_sprites, 
					   self.create_attack,
					   self.destroy_attack
					   )

	def create_attack(self):
		self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])
	def spawn_enemy(self):
		"""
		Spawns an enemy at a random position around the player.
		"""
		enemy_pos = self.get_random_spawn_position()

		# Create an enemy at the computed position
		Enemy(
			'monster',
			enemy_pos,
			[self.visible_sprites, self.attackable_sprites],
			self.obstacles_sprites
		)
	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def get_random_spawn_position(self, min_distance=200, max_distance=500):
		"""Generate a random position around the player at a given distance range."""
		angle = random.uniform(0, 360)  # Random angle in degrees
		distance = random.randint(min_distance, max_distance)  # Random distance

        # Convert angle to radians
		radians = angle * (3.14159 / 180)

        # Compute the random spawn location
		enemy_x = int(self.player.rect.centerx + distance * pygame.math.Vector2(1, 0).rotate(angle).x)
		enemy_y = int(self.player.rect.centery + distance * pygame.math.Vector2(1, 0).rotate(angle).y)

		return (enemy_x, enemy_y)

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

	def run(self):
		current_time = pygame.time.get_ticks()
		num_enemies = random.randint(3, 5)
		if current_time - self.last_spawn_time >= self.enemy_spawn_delay:
			for i in range(random.randint(3, 5)):
				self.spawn_enemy()
			self.last_spawn_time = current_time 

		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.obstacles_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.draw_heart()
		self.ui.display(self.player)
		pygame.time.set_timer(self.ENEMY_SPAWN_EVENT, 3000)
		# self.spawn_enemy()

		# for event in pygame.event.get():
		# 	print(event)
		# 	if event.type == self.ENEMY_SPAWN_EVENT:
		# 		self.spawn_enemy()
		# 		print('enemy spawn')
	
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


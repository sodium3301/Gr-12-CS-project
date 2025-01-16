import pygame
from settings import *
from Character import Player
from enemy import Enemy
from ui import *
import random
from weapon import Weapon
from map import *
from particles import AnimationPlayer

class Stuff:
	"""
    The `Stuff` class(considered as game class) manages the primary gameplay mechanics. All interaction, player initialization, map creation, enemy spawn and interaction is managed here.

    This class is responsible for:
    - Managing the player character and their interactions with the enemies.
    - Spawning, updating, and managing enemies and their behaviors.
    - Maintaining and rendering the game map, including dynamic tile updates from the map class.
    - Handling combat mechanics, including attacks, collisions, and damage dealing.
    - Tracking and displaying the player's score and health.
    - Managing sprite groups for rendering and collision detection.
    - Providing user interface for display in game information such as health and score.
    - Resetting the game state for restarts or transitions between levels.
    """
	def __init__(self):

		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacles_sprites = pygame.sprite.Group()
		self.score = 0
		
		# attack sprites
		self.current_attack  = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# Weapon 

		self.last_spawn_time = pygame.time.get_ticks()
		self.enemy_spawn_delay = 3000

		self.player = Player([self.visible_sprites], 
					   self.obstacles_sprites, 
					   self.create_attack,
					   self.destroy_attack
					   )
		
		self.create_map()

		self.ui = UI(self.player)

		# particles
		self.animation_player = AnimationPlayer()

	"""
	Creates the game map by initializing the `Map` class and drawing tiles.
	"""
	def create_map(self):
		self.map = Map(self.player, self.visible_sprites, self.obstacles_sprites)
		self.map.draw_map()

	"""
	Resets the game state, including the map, sprites, and player.
	"""
	def reset(self):
		# Clear all existing sprites and states
		self.visible_sprites.empty()
		self.obstacles_sprites.empty()
		self.attack_sprites.empty()
		self.attackable_sprites.empty()
		self.current_attack = None

		# Reinitialize the player
		self.player = Player(
			[self.visible_sprites],  # Add player to visible sprites group
			self.obstacles_sprites,  # Pass obstacle sprites group
			self.create_attack,      # Attack creation callback
			self.destroy_attack      # Attack destruction callback
		)

		# Recreate the map or level
		self.create_map()

		# Reset other game states if needed
		self.last_spawn_time = pygame.time.get_ticks()
		self.ui = UI(self.player)  # Update the UI with the new player

	"""
	generates a weapon attack instance
	"""
	def create_attack(self):
		self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

	"""
	Daniel's method, no idea
	"""
	def create_magic(self,style,strength,cost):
		print(style)
		print(strength)
		print(cost)

	"""
	generates a random spawn position for the enemy to spawn around the player. It will generate a random angle and distance based on the player's current position.
	"""

	def get_random_spawn_position(self, min_distance=200, max_distance=500):
		"""Generate a random position around the player at a given distance range."""
		angle = random.uniform(0, 360)  # Random angle in degrees
		distance = random.randint(min_distance, max_distance)  # Random distance

		# Convert angle to radians
		radians = angle * (3.14159 / 180)

		# Compute the random spawn angle according to player
		enemy_x = int(self.player.rect.centerx + distance * pygame.math.Vector2(1, 0).rotate(angle).x)
		enemy_y = int(self.player.rect.centery + distance * pygame.math.Vector2(1, 0).rotate(angle).y)

		return (enemy_x, enemy_y)


	"""
	check if player is vulnerable, if ture, then the player is able to take damage. After taking damage vulnerable is set to false so the player cannot take damage immediately after that tick,
	timer is then set.
	"""
	def damage_player(self, amount):
		if self.player.vulnerable:
			self.player.heart -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()



	"""
	gets a random position from the get_random_spawn_position method and generates enemies around the player
	"""
	def spawn_enemy(self):
		
		enemy_pos = self.get_random_spawn_position()

		# Create an enemy at the computed position
		
		self.enemy = Enemy(
			'monster',
			enemy_pos,
			[self.visible_sprites, self.attackable_sprites],
			self.obstacles_sprites,
			self.damage_player,
			self.add_score
		)


	"""
	tally up scores 
	"""
	def add_score(self, amount):
		self.player.score += amount
		
	
	"""
	destroy the current weapon attack instance 
	"""
	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None


	"""
	deals with players attack interaction with other attackble sprites
	"""
	def player_attack(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						# target_sprite.kill()
						if target_sprite.sprite_type == 'enemy':
							target_sprite.get_damage(self.player, attack_sprite.sprite_type)



	"""
	getter method for player
	"""
	def get_player(self):
		return self.player

	"""
	Draws the player's health (hearts) on the screen.
	"""
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
		

	"""
	Main game loop for managing updates(especially visible sprites and obstacle sprites), rendering, interaction, drawing map, and generating enemies.
	"""
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
		self.player_attack()

		self.ui.draw_heart()

		self.ui.display(self.player)
		self.map.update()
		self.map.draw_map()
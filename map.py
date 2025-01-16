import pygame
import random
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/tile.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -10)

class Map:
    """ 
    Creates, draws, and manipulates the map, which regenerates on the edges infinitely with a set size and an offset.

    Attributes:
        plot (list[list[str]]): A plot to be mapped.
        offset_x (int): Number of tiles offsetted on x axis.
        offset_y (int): Number of tiles offsetted on y axis.
        player (Player): A reference of the Player object.
        visible_sprites (pygame.sprite.Group): A reference of the visble_sprites Group object.
        obstacles_sprites (pygame.sprite.Group): A reference of the obstacles_sprites Group object.
    
    Methods:
        create_tile(): Randomly returns either 'x' or empty string.
        create_map(): Populates self.plot with create_tile().
        draw_map(): Creates Tile objects on the screen.
        clear_map(): Cleans Tile objects on the screen.
        update(): Updates offset_x and offset_y.
    """

    def __init__(self, player, visible_sprites, obstacles_sprites):
        self.plot = [['' for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.offset_x = 0
        self.offset_y = 0

        self.player = player
        self.visible_sprites = visible_sprites
        self.obstacles_sprites = obstacles_sprites
        self.create_map()
    
    def create_tile(self):
        """
        Returns 'x' 3% of the time or an empty string 97% of the time.
        """
        if random.random() < 0.03:
            return 'x'
        return ''
    
    def create_map(self):
        """
        Populates self.plot except for central tile with create_tile() method.
        """
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if not (i == j and j == MIDPOINT):
                    self.plot[i][j] = self.create_tile()

    def draw_map(self):
        """
        Creates Tile objects in the correct coordinate with scale and offset taken into account.
        """
        for row_index, row in enumerate(self.plot):
             for col_index, col in enumerate(row):
                x = (col_index + self.offset_x) * TILESIZE
                y = (row_index + self.offset_y) * TILESIZE
                if col == 'x': 
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])        
    
    def clear_map(self):
        """
        Clears all Tile objects from the map by emptying sprite groups.
        """
        for sprite in self.visible_sprites:
            if isinstance(sprite, Tile):
                sprite.kill()

        for sprite in self.obstacles_sprites:
            if isinstance(sprite, Tile):
                sprite.kill()

    def update(self):
        """
        Checks if the player goes out of the central tile. 
        If they do, a row / column is added in front and another is dropped behind, and offset is updated.
        """
        # Player is facing up
        self.clear_map()
        if self.player.get_y_pos() <= (MIDPOINT + self.offset_y) * TILESIZE:
            self.plot.pop()
            self.plot.insert(0, [self.create_tile() for _ in range(DIMENSION)])
            self.offset_y -= 1
            print('top')
        # down
        elif self.player.get_y_pos() >= (MIDPOINT + self.offset_y + 1) * TILESIZE:
            self.plot.pop(0)
            self.plot.append([self.create_tile() for _ in range(DIMENSION)])
            self.offset_y += 1
            print('bottom')
        # left
        if self.player.get_x_pos() <= (MIDPOINT + self.offset_x) * TILESIZE:
            for row in self.plot:
                row.pop()
                row.insert(0, self.create_tile())
            self.offset_x -= 1
            print('left')
        # right
        elif self.player.get_x_pos() >= (MIDPOINT + self.offset_x + 1) * TILESIZE:
            for row in self.plot:
                row.pop(0)
                row.append(self.create_tile())
            self.offset_x += 1
            print('right')
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
    def __init__(self, stuff, player, visible_sprites, obstacles_sprites):
        self.plot = [['' for _ in range(DIMENSION)] for _ in range(DIMENSION)]
        self.offset_x = 0
        self.offset_y = 0
        self.midpoint_x = MIDPOINT
        self.midpoint_y = MIDPOINT

        self.stuff = stuff
        self.player = player
        self.visible_sprites = visible_sprites
        self.obstacles_sprites = obstacles_sprites
        self.create_map()
        
    def create_map(self):
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if not (i == j and j == MIDPOINT):
                    self.plot[i][j] = self.create_tile()
                
    def create_tile(self):
        if random.random() < 0.03:
            return 'x'
        return ''

    def draw_map(self):
        for row_index, row in enumerate(self.plot):
             for col_index, col in enumerate(row):
                x = (col_index + self.offset_x) * TILESIZE
                y = (row_index + self.offset_y) * TILESIZE
                if col == 'x': 
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])        

    def get_midpoint(self):
        self.midpoint_x = MIDPOINT + self.offset_x
        self.midpoint_y = MIDPOINT + self.offset_y
        return (self.midpoint_x, self.midpoint_y)
    
    def clear_map(self):
        """
        Clear all tiles from the map by emptying sprite groups.
        """
        for sprite in self.visible_sprites:
            if isinstance(sprite, Tile):
                sprite.kill()  # Removes the tile from all sprite groups

        for sprite in self.obstacles_sprites:
            if isinstance(sprite, Tile):
                sprite.kill()

    def update(self):
        # Player is going up
        self.clear_map()
        if self.player.get_y_pos() <= self.get_midpoint()[1] * TILESIZE:
            self.plot.pop()
            self.plot.insert(0, [self.create_tile() for _ in range(DIMENSION)])
            # self.player.offset('up')
            self.offset_y -= 1
            print('top')
        # down
        if self.player.get_y_pos() >= (self.get_midpoint()[1] + 1) * TILESIZE:
            self.plot.pop(0)
            self.plot.append([self.create_tile() for _ in range(DIMENSION)])
            # self.player.offset('down')
            self.offset_y += 1
            print('bottom')
        # left
        if self.player.get_x_pos() <= self.get_midpoint()[0] * TILESIZE:
            for row in self.plot:
                row.pop()
                row.insert(0, self.create_tile())
            # self.player.offset('left')
            self.offset_x -= 1
            print('left')
        # right
        if self.player.get_x_pos() >= (self.get_midpoint()[0] + 1) * TILESIZE:
            for row in self.plot:
                row.pop(0)
                row.append(self.create_tile())
            # self.player.offset('right')
            self.offset_x += 1
            print('right')

    def get_plot(self):
        return self.plot
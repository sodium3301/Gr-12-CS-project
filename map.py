import pygame
from random import random

class Map():
    def __init__(self):
        self.map = [[]]
    
    def generate_map(self):
        self.map = [[1 if random.random() < 0.02 else 0 for _ in range(500)] for _ in range(500)]
        
    def get_map(self):
        return self.map
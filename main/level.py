#Contains all sprites (player, enemies, map + deals with interactions)

import pygame
from settings import *
from tile import TestRock
from player import TestPlayer


class Level: 
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface() #gets the display surface from anywhere in the code

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    TestRock((x,y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = TestPlayer((x,y), [self.visible_sprites])
    
    def run(self):
        #update and draw game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()

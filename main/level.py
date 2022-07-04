#Contains all sprites (player, enemies, map + deals with interactions)

import pygame
from settings import *
from tile import TestRock
from player import TestPlayer


class Level: 
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface() #gets the display surface from anywhere in the code

        self.visible_sprites = YSortCameraGroup()
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
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group): #class - camera being sorted by the Y co-ordinates
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2 # to get player in middle of screen
        self.half_height = self.display_surface.get_size()[1] // 2 # to get player in middle of screen
        self.offset = pygame.math.Vector2()  # vector gives control of where sprites are drawn
    
    def custom_draw(self,player):

        #getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height


        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
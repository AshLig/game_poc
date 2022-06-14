import pygame, sys 
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init() #starst pygame and initiates other parts of pygame - must use 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #This function takes 2 parameters for the width and height of window, imported variables from settings
        pygame.display.set_caption('game_poc') #names the window of your game, takes a string parameter
        self.clock = pygame.time.Clock() #controlling the FPS rate

        self.level = Level() #created instance of class level 

    def run_game(self):
        while True: #infinite loop
            for event in pygame.event.get(): #loops through events     ///   gets all the possible player input events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #gets rid of while loop
            
            pygame.display.update() #updates the display window
            self.level.run() 
            self.clock.tick(FPS)


if __name__ == '__main__': #checking if this is our main file
    game = Game() #created instance of game class
    game.run_game() #called a method of the class on instance
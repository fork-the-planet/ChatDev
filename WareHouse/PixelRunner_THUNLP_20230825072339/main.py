'''
This is the main file that runs the retro-style endless runner game.
'''
import pygame
from game import Game
def main():
    pygame.init()
    game = Game()
    game.run()
if __name__ == "__main__":
    main()
import pygame as pg
from menu import GameManager

def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    pg.display.set_caption("Run 'n Gun")
    game_manager = GameManager(screen)
    game_manager.run()

if __name__ == "__main__":
    main()   
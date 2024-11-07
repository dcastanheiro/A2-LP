"""Esse módulo importa todas as classes necessárias e inicia o jogo"""

import pygame as pg
from player import Player

pg.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BLACK = (0,0,0)

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Run n Gun')

# framerate
clock = pg.time.Clock()
FPS = 60


player_all_images_folders = {
            "idle":             "assets/Player/idle_right",
            "jump":             "assets/Player/jump_right",
            "jump_down":        "assets/Player/jump_right_down",
            "jump_up":          "assets/Player/jump_right_up",
            "run":              "assets/Player/run_right",
            "crouch":            "assets/Player/shift_right",
            "shoot_jump":       "assets/Player/shoot_jump_right",
            "shoot_jump_down":  "assets/Player/shoot_jump_right_down",
            "shoot_jump_up":    "assets/Player/shoot_jump_right_up",
            "shoot":            "assets/Player/shoot_right",
            "shoot_up":         "assets/Player/shoot_right_up",
            "shoot_run":        "assets/Player/shoot_run_right",
            "shoot_run_up":     "assets/Player/shoot_run_right_up",
            "shoot_shift":      "assets/Player/shoot_shift_right",
            "die":              "assets/Player/die_right"

}


# inicializa as entidades
player = Player(player_all_images_folders, 500, 500, 3)


# Mapa: Cada "#" representa um bloco sólido, e "." é um espaço vazio
map_layout = [
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    ".............#####......",
    "..............#.........",
    ".......#####............",
    ".....###................",
    "########################"
]


run = True
while run:

    for event in pg.event.get():
        # quit game
        if event.type == pg.QUIT:
            run = False


    # preenche a tela
    screen.fill(BLACK)

    # desenha as entidades
    player.draw(screen)

    # atualiza a tela
    pg.display.update()
    clock.tick(FPS)
pg.quit()
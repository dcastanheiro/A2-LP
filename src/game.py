"""Esse módulo importa todas as classes necessárias e inicia o jogo"""

import pygame as pg
from player import Player
from map import Platform

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

# mapa: Cada "#" representa um bloco, e "." é um espaço vazio
map_layout = [
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................"
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    ".............#####..###.........................................................................",
    "..............#.................................................................................",
    ".......#####....................................................................................",
    ".....###...............................#####...................................................",
    "####################################..##########################################################"
]


class Game:
    """
    Classe que administra o funcionamento geral do jogo.
    """
    def __init__(self) -> None:
        pg.init()

        # setando a tela
        self.width = 1200
        self.height = 800
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Run n Gun')

        # inicializando objetos
        self.player = Player(player_all_images_folders, x=300, y=300, vel=2)
        self.platforms = Platform.create_platform(map_layout=map_layout)

        self.clock = None
        self.run = False


    def running(self):
        """Método que inicializa o jogo"""
        self.clock = pg.time.Clock()
        self.run = True
        while self.run:
            self.on_event()
            self.update()
            self.draw()
            self.clock.tick(60)
        pg.quit()

    
    def on_event(self):
        """Metodo responsavel por controlar os eventos do jogo"""
        for event in pg.event.get():
        # quit game
            if event.type == pg.QUIT:
              self.run = False

    def update(self):
        """Metodo para atualizar o jogo"""
        self.player.update()
        for platform in self.platforms:
            platform.update()
        self.check_collision()
        pg.display.update()
        

    def check_collision(self):
        """Metodo responsavel pela colisao entre objetos do mapa"""
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.player.on_collision(platform)
                platform.on_collision(self.player)

    def draw(self):
        """Metodo responsavel por desenhar os objetos na tela"""
        self.screen.fill((0,0,0))
        for platform in self.platforms:
            platform.draw(self.screen)  
        self.player.draw(self.screen)
        pg.display.flip()


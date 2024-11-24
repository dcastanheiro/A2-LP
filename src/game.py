"""Esse módulo importa todas as classes necessárias e inicia o jogo"""

import pygame as pg
from player import Player
from map import Platform, Background
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TILE_SIZE, player_all_images_folders, map_layout, background_layers
from bullet import Bullet

class Game:
    """
    Classe que administra o funcionamento geral do jogo.
    """
    def __init__(self) -> None:
        pg.init()

        # setando a tela
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Run n Gun')

        # inicializar o background em camadas
        self.background = Background(
            background_layers,
            screen_width=self.width,
            screen_height=self.height
        )

        # inicializando objetos
        self.player = Player(player_all_images_folders, x=20, y=30, vel=1)
        self.platforms = Platform.create_platform(map_layout=map_layout, img_path ="assets/Assets_area_2/tileset/platform_0.png")

        # inicializando grupo de sprites
        self.bullet_group = pg.sprite.Group()
        self.platform_group = pg.sprite.Group()

        for platform in self.platforms:
            self.platform_group.add(platform)

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
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
              self.run = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.player.shoot_bullets(self.bullet_group)
                self.player.is_shooting = True
            # elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            #     self.player.is_shooting = False   
            

    def update(self):
        """Metodo para atualizar o jogo"""
        self.background.update()
        self.player.update()
        self.bullet_group.update()
        for platform in self.platforms:
            platform.update()
        self.check_collision()
        self.player._on_out_of_bounds()
        pg.display.update()  
        
    def check_collision(self):
        """Metodo responsavel pela colisao entre objetos do mapa"""
        # colisao do player com plataformas
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.player.on_collision(platform)
                platform.on_collision(self.player)

        # colisao das balas com plataformas
        for bullet in self.bullet_group:
            if pg.sprite.spritecollideany(bullet, self.platform_group):
                bullet.kill()

    def draw_grid(self):
        """Metodo para desenhar o grid na tela."""
        for x in range(0, self.width, TILE_SIZE):
            pg.draw.line(self.screen, (50, 50, 50), (x, 0), (x, self.height))  
        for y in range(0, self.height, TILE_SIZE):
            pg.draw.line(self.screen, (50, 50, 50), (0, y), (self.width, y))

    def draw(self):
        """Metodo responsavel por desenhar os objetos na tela"""
        self.background.draw(self.screen)
        self.draw_grid()
        for platform in self.platforms:
            platform.draw(self.screen)  
        self.player.draw(self.screen)
        self.bullet_group.draw(self.screen)
        pg.display.flip()


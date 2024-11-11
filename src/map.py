"""Modulo dedicado a criacao do mapa"""
import pygame as pg
from settings import TILE_WIDTH, TILE_HEIGHT

class Platform(pg.sprite.Sprite):
    """
    Classe que representa uma plataforma. Apresenta alguns atributos e métodos sobre o comportamento
    e criacao de uma plataforma no mapa.

    Parameters
    ----------
    x:
        Posição do eixo x inicial da plataforma
    y:
        Posição do eixo y inicial da plataforma
    width:
        Largura da plataforma
    height:
        Altura da plataforma
    """

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill((0, 255, 0))  # cor verde para a plataforma
        self.rect = self.image.get_rect(topleft=(x, y))

    @classmethod
    def create_platform(cls, map_layout: list, tile_width=TILE_WIDTH, tile_height=TILE_WIDTH):
        """
        Metodo de criacao da plataforma

        Parameters
        ----------
        map_layout:
                    lista de strings com '#' e '.'
        tile_width:
                    int representando o largura da tile
        tile_height:
                    int representando a altura da tile
        """
        platforms = [] 
        for row_index, row in enumerate(map_layout):
            for col_index, tile in enumerate(row):
                if tile == "#":
                    x = col_index * tile_width
                    y = row_index * tile_height
                    platform = cls(x, y, tile_width, tile_height)
                    platforms.append(platform)

        return platforms  
     
    def draw(self, screen):
        """
        Metodo responsavel por desenhar retangulos na tela

        Parameters
        ----------
        screen:
                pg.Surface representando a tela do jogo
        """
        screen.blit(self.image, self.rect)

    def on_collision(self, other):
        pass

    def update(self):
        pass

    
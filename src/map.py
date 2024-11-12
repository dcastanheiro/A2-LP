"""Modulo dedicado a criacao do mapa"""
import pygame as pg
from settings import TILE_SIZE
from utils import load_tile

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

    def __init__(self, x, y, width, height, img_path):
        super().__init__()
        self.image = load_tile(img_path)
        self.rect = self.image.get_rect(topleft=(x, y))

    @classmethod
    def create_platform(cls, map_layout: list, img_path, tile_width=TILE_SIZE, tile_height=TILE_SIZE) -> list:
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
        
        Returns
        -------
        platforms:
                    lista representando as plataformas do mapa
        """
        platforms = [] 
        for row_index, row in enumerate(map_layout):
            for col_index, tile in enumerate(row):
                if tile == "#":
                    x = col_index * tile_width
                    y = row_index * tile_height
                    platform = cls(x, y, tile_width, tile_height, img_path)
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

    
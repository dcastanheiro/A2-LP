"""Modulo responsavel por criar uma base comum para as entidades do jogo"""

import pygame as pg
import os
from utils import load_image

class Entity(pg.sprite.Sprite):
    """
    Classe que representa uma Entidade. Qualquer coisa que se mexe e possui sprites.
    Parameters
    ----------
    images_folders: dict
        Dicionário de animações onde as chaves são os estados (por exemplo: 'idle', 'run') e os valores são as listas de imagens correspondentes.
    x:
        Posição do eixo x inicial da entidade
    y:
        Posição do eixo y inicial da entidade
    """
    def __init__(self, images_folders: dict, x: int, y: int):
        super().__init__()
        self.state = 'idle'
        self.index = 0
        # carregar imagens de cada estado        
        self.images = {}

        for state, folder in images_folders.items():
            self.images[state] = [
                load_image(os.path.join(folder, img_name))
                for img_name in os.listdir(folder) if img_name.endswith(".png")
            ]

        self.image = self.images[self.state][self.index]
        self.rect = self.image.get_rect(center=(x, y))
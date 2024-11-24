"""Modulo responsavel pela criacao dos inimigos e suas propriedades"""

from player import Entity
from bullet import Bullet

class Enemy(Entity):

    def __init__(self, x: int, y: int, images_folders: dict, bullet: Bullet):
        super().__init__(images_folders, x, y)
        

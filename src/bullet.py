from typing import Any
import pygame as pg
from utils import load_image
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Bullet(pg.sprite.Sprite):
    """
    Preencher
    """
    def __init__(self, x: int, y: int, direction: tuple, img_path: str, speed: int, dmg: int):
        super().__init__()
        self.speed = speed
        self.dmg = dmg
        self.image = load_image(img_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction

    def update(self):
        "Metodo para atualizar a posicao da bala"
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1] 

        # caso saia do limite da tela
        if not (0 <= self.rect.x <= SCREEN_WIDTH) or not (0 <= self.rect.y <= SCREEN_HEIGHT):
            self.kill()  

"""Modulo responsavel pela criacao das balas utilizadas pelo jogador e pelos inimigos"""

from typing import Any
import pygame as pg
from utils import load_image
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Bullet(pg.sprite.Sprite):
    """
    Classe que representa as balas utilizadas no jogo.

    Parameters
    ----------
    x: int
        Posição do eixo x de criacao da bala
    y: int
        Posição do eixo y de criacao da bala
    direction: tuple
        Direção que a bala vai percorrer a tela
    img_path: str
        String representando a o caminho para a imagem da bala
    speed: int
        Velocidade de movimento da bala no ar
    dmg: int
        Dano que a bala inflinge em outras entidades

        
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


class BazookaBullet(Bullet):
    """
    Bala de bazuca, lenta, mas com alto dano
    """
    def __init__(self, x: int, y: int, direction: tuple):
        super().__init__(x, y, direction, "assets/Enemies/bazooka/bazooka_bullet.png", speed=5, dmg=15)


class SniperBullet(Bullet):
    """
    Bala de sniper, rápida, mas com dano moderado
    """
    def __init__(self, x: int, y: int, direction: tuple):
        super().__init__(x, y, direction, "assets/Enemies/sniper/sniper_bullet.png", speed=12, dmg=10)
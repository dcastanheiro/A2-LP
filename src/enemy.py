"""Modulo responsavel pela criacao dos inimigos e suas propriedades"""

from player import Entity
from bullet import Bullet
import pygame as pg
import time
from bullet import BazookaBullet, SniperBullet


class Enemy(Entity):
    """
    Classe base para inimigos no jogo.
    Existem dois tipos de inimigos: Bazuca e Sniper.
    """

    def __init__(self, images_folders: dict, x: int, y: int, health: int, bullet_group: pg.sprite.Group, bullet_type: str, shoot_interval: float):
        """
        Parameters
        ----------
        images_folders: dict
            Dicionário com sprites do inimigo.
        x: int
            Posição inicial no eixo x.
        y: int
            Posição inicial no eixo y.
        health: int
            Vida do inimigo.
        bullet_group: pg.sprite.Group
            Grupo para gerenciar as balas disparadas.
        bullet_type: str
            Tipo de bala disparada pelo inimigo ('bazooka' ou 'sniper').
        shoot_interval: float
            Tempo de espera entre tiros consecutivos.
        """
        super().__init__(images_folders, x, y)
        self.health = health
        self.bullet_group = bullet_group
        self.bullet_type = bullet_type
        self.shoot_interval = shoot_interval
        self.direction = 1
        self.last_shot_time = time.time()

    def set_state(self, new_state: str):
        """
        Altera o estado do inimigo (idle, shoot, etc.).

        Parameters
        ----------
        new_state: str
            Novo estado para o inimigo.
        """
        if self.state != new_state:
            self.state = new_state
            self.index = 0
            self.image = self.images[self.state][self.index]
            self.current_time = 0

    def shoot(self, target_x: int, target_y: int):
        """
        Faz o inimigo disparar balas em direcao a um alvo.

        Parameters
        ----------
        target_x: int
            Posicao x do alvo
        target_y: int
            Posicao y do alvo.
        """
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shoot_interval:
            if self._can_see_player(target_x, target_y):
                # atirar reto
                direction = (self.direction, 0)

                # criar a bala
                if self.bullet_type == "bazooka":
                    bullet = BazookaBullet(self.rect.centerx, self.rect.centery, direction=direction)
                elif self.bullet_type == "sniper":
                    bullet = SniperBullet(self.rect.centerx, self.rect.centery, direction=direction)

                self.bullet_group.add(bullet)
                self.last_shot_time = current_time
    
                self.set_state("shoot")

    def _can_see_player(self, target_x, target_y):
        """
        Verifica se o jogador está na direção e alcance do inimigo.
        """
        max_distance_horizontal = 400
        max_distance_vertical = 10

        # verifica alcance horizontal e vertical
        in_horizontal_range = abs(target_x - self.rect.centerx) <= max_distance_horizontal
        in_vertical_range = abs(target_y - self.rect.centery) <= max_distance_vertical

        if self.direction == 1 and target_x > self.rect.centerx:  # Olhando para a direita
            is_in_direction = True
        elif self.direction == -1 and target_x < self.rect.centerx:  # Olhando para a esquerda
            is_in_direction = True
        else:
            is_in_direction = False

        return in_horizontal_range and in_vertical_range and is_in_direction

    def take_damage(self, amount: int):
        """
        Reduz a vida do inimigo ao receber dano.

        Parameters
        ----------
        amount: int
            Quantidade de dano recebido
        """
        self.health -= amount
        if self.health <= 0:
            self.kill()  

    def update(self, target_x: int, target_y: int):
        """
        Atualiza o estado do inimigo, incluindo a lógica de disparo

        Parameters
        ----------
        target_x: int
            Posição x do alvo.
        target_y: int
            Posição y do alvo.
        """
        self.shoot(target_x, target_y)

        # animacao de atirar
        if self.state == "shoot":
            self.current_time += 0.1
            if self.current_time >= 1:
                self.index = (self.index + 1) % len(self.images[self.state])
                self.image = self.images[self.state][self.index]
                self.current_time = 0

            # voltar para idle como padrao
            if self.index == len(self.images[self.state]) - 1:
                self.set_state("idle")



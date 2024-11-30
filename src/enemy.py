"""Modulo responsavel pela criacao dos inimigos e suas propriedades"""

from player import Entity
from bullet import Bullet
import pygame as pg
import time
from bullet import BazookaBullet, SniperBullet, ArBullet


class Enemy(Entity):
    """
    Classe base para inimigos no jogo.
    Existem dois tipos de inimigos nessa classe: Bazuca e Sniper.
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

    def shoot(self, player_x: int, player_y: int, platforms: pg.sprite.Group):
        """
        Faz o inimigo disparar balas em direcao a um alvo.

        Parameters
        ----------
        player_x: int
            Posicao x do alvo
        player_y: int
            Posicao y do alvo.
        platforms : pg.sprite.Group
            Grupo de obstaculos do jogo
        """
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shoot_interval:
            if self._can_see_player(player_x, player_y, platforms):
                # atirar reto
                direction = (self.direction, 0)

                # criar a bala
                if self.bullet_type == "bazooka":
                    bullet = BazookaBullet(self.rect.centerx, self.rect.centery, direction=direction)
                elif self.bullet_type == "sniper":
                    bullet = SniperBullet(self.rect.centerx, self.rect.centery, direction=direction)
                elif self.bullet_type == "ar":
                    bullet = ArBullet(self.rect.centerx, self.rect.centery, direction=direction)
                else:
                    bullet = None

                if bullet:
                    self.bullet_group.add(bullet)
                    self.last_shot_time = current_time
    
                    self.set_state("shoot")

    def _can_see_player(self, player_x, player_y, platforms):
        """
        Verifica se o jogador está na direção e alcance do inimigo.
        ----------
        player_x : int
            Posicao x do jogador
        player_y : int
            Posicao y do jogador
        platforms : pg.sprite.Group
            Grupo de obstaculos do jogo.
        Returns
        -------
        bool
            Verdadeiro se o inimigo pode ver o jogador, falso caso contrário.   
        """
        max_distance_horizontal = 400
        max_distance_vertical = 10

        # verifica alcance horizontal e vertical
        in_horizontal_range = abs(player_x - self.rect.centerx) <= max_distance_horizontal
        in_vertical_range = abs(player_y - self.rect.centery) <= max_distance_vertical

        if self.direction == 1 and player_x > self.rect.centerx:  # Olhando para a direita
            is_in_direction = True
        elif self.direction == -1 and player_x < self.rect.centerx:  # Olhando para a esquerda
            is_in_direction = True
        else:
            is_in_direction = False

        path_clear = self._is_path_clear(player_x, player_y, platforms)

        return in_horizontal_range and in_vertical_range and is_in_direction and path_clear

    def _is_path_clear(self, player_x, player_y, platforms):
        """
        Verifica se existem plataformas no caminho entre a visão do inimigo e o jogador
        Parameters
        ----------
        player_x : int
            Posicao x do jogador
        player_y : int
            Posicao y do jogador
        platforms : pg.sprite.Group
            Grupo de obstaculos do jogo

        Returns
        -------
        bool
            Verdadeiro se o caminho estiver livre, falso se houver obstaculos
        """

        # cria uma linha imaginária entre o inimigo e o jogador
        start = self.rect.center
        end = (player_x, player_y)

        for platform in platforms:
            if platform.rect.clipline(start, end):  # verifica intersecao da linha com a plataforma
                return False

        return True

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

    def update(self, player_x: int, player_y: int, platforms: pg.sprite.Group):
        """
        Atualiza o estado do inimigo.

        Parameters
        ----------
        player_x: int
            Posição x do alvo.
        player_y: int
            Posição y do alvo.
        platforms: pg.sprite.Group
            Grupo de obstaculos do jogo
            
        """
        if self._can_see_player(player_x, player_y, platforms):
            self.shoot(player_x, player_y, platforms)

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

    def draw(self, screen):
        """
        Módulo responsável por desenhar as sprites do inimigo
        Parameters
        ----------
        screen: pg.Surface
            Superficie onde o jogador será desenhado
        """
        screen.blit(self.image, self.rect)
class ArEnemy(Enemy):
    """
    Classe responsavel pelo inimigo "Ar" que patrulha horizontalmente.
    Implementado fora da classe principal pois possui logicas diferentes.
    """
    def __init__(self, images_folders: dict, x: int, y: int, health: int, bullet_group: pg.sprite.Group, bullet_type: str, shoot_interval: float, patrol_speed: float):
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
        patrol_speed: float
            Velocidade de patrulha horizontal.
        """
        super().__init__(images_folders, x, y, health, bullet_group, bullet_type, shoot_interval)
        self.patrol_speed = patrol_speed
        self.patrolling = True  
        self.flip = False
        self.direction = 1

    def patrol(self, platforms: pg.sprite.Group):
        """
        Movimento do inimigo.
        Parameters
        ----------
        platforms : pg.sprite.Group
            Grupo de plataformas para verificar colisoes
        """
        if self.patrolling:
            # movimentaa horizontalmente
            self.rect.x += int(self.patrol_speed * self.direction)

            if self.state != "walk":
                self.set_state("walk")

            # verificar colisão lateral com plataformas
            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    # mudar direcao ao colidir com a lateral da plataforma
                    self.direction *= -1
                    self.rect.x += int(self.patrol_speed * self.direction)
                    self.flip = not self.flip
                    

    def update(self, player_x: int, player_y: int, platforms: pg.sprite.Group):
        """
        Metodo responsavel por atualizar o estado do inimigo

        Parameters
        ----------
        player_x: int
            Posicao x do alvo.
        player_y: int
            Posicao y do alvo.
        platforms: pg.sprite.Group
            Grupo de plataformas do jogo
        """
        if self._can_see_player(player_x, player_y, platforms):
            # para de andar e atira
            self.patrolling = False
            self.shoot(player_x, player_y, platforms)
        else:
            self.patrolling = True
            self.patrol(platforms)

        # atualiza animacao
        self.current_time += 0.1
        if self.current_time >= 1:
            self.index = (self.index + 1) % len(self.images[self.state])
            self.image = self.images[self.state][self.index]
            self.current_time = 0


    def draw(self, screen):
        """
        Desenha o inimigo na tela
        Parameters
        ----------
        screen: pg.Surface
            Superficie onde o inimigo será desenhado.
        """
        # TODO: consertar sobreposicao de flip do inimigo
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        
"""Modulo dedicado a criacao do personagem principal e seus comportamentos"""

import pygame as pg
import os
import time
from bullet import Bullet
from map import Platform
from settings import PX_SCALE, SCREEN_HEIGHT, SCREEN_WIDTH
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

class Player(Entity):
    """
    Classe que representa o jogador. Apresenta alguns atributos e métodos sobre o jogador.
    Anima o jogador.

    Parameters
    ----------
    images_folders: dict
        Dicionário de animações com estados e imagens correspondentes
    x: int
        Posição do eixo x inicial do jogador
    y: int
        Posição do eixo y inicial do jogador
    vel: int
        Velocidade de movimento do jogador
    """
    def __init__(self, images_folders: dict, x: int, y: int, vel: int):
        super().__init__(images_folders, x, y)
        self.vel_x = vel
        self.dx = 0
        self.direction = (1,0) # quaisquer das 4 direcoes
        self.facing = (1, 0) # direcoes laterais
        self.flip = False
        self.animation_speed = 0.1
        self.current_time = 0
        self.is_moving = False
        self.is_shooting = False
        self.is_crouched = False
        self.is_in_air = False
        self.gravity_up = 0.4  # gravidade na ascendencia do pulo
        self.gravity_down = 0.1 # gravidade na descendencia do pulo
        self.vel_y = 0
        self.jump_count = 0
        self.jump_count_max = 1
        self.jump_pressed = False
        self.bullet_cooldown = 0.05  
        self.last_shot_time = time.time()
     
    
    def movement(self):
        """Módulo responsável pela movimentação do jogador"""
        keys = pg.key.get_pressed()

        self.dx = 0

        # agacha
        if keys[pg.K_s] or keys[pg.K_DOWN] and not self.is_in_air:
            self.set_state('crouch')
            self.is_crouched = True
        else:
            self.is_crouched = False

        # movimentaçao lateral
        if keys[pg.K_a] or keys[pg.K_LEFT] and not self.is_crouched:
            self.dx -= self.vel_x
            self.direction = (-1,0)
            self.facing = (-1,0)
            self.flip = True
            self.is_moving = True
            self.set_state('run')  
        elif keys[pg.K_d] or keys[pg.K_RIGHT]  and not self.is_crouched:
            self.dx += self.vel_x
            self.direction = (1,0)
            self.facing = (1,0)
            self.flip = False
            self.is_moving = True
            self.set_state('run') 

        # se nao estiver se movendo e nao estiver agachado
        elif not self.is_crouched and not self.is_in_air:
            self.set_state('idle')

        # pular
        if keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP] and not self.jump_pressed and not self.is_in_air:
            self._jump()
            self.jump_pressed = True

        # olhar para cima ou para baixo durante o pulo
        if self.is_in_air:
            if keys[pg.K_w] or keys[pg.K_UP]:
                self.set_state('jump_up')
            elif keys[pg.K_s] or keys[pg.K_DOWN]:
                self.set_state('jump_down')

        # resetar o pulo
        if not keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP]:
            self.jump_pressed = False

    # def shoot(self):
    #     """Metodo responsavel pelas movimentacoes e animacoes de tiro do jogador"""
    #     if not self.is_shooting:
    #         return


    #     keys = pg.key.get_pressed()
    #     if self.is_moving and self.is_shooting:
    #         self.set_state('shoot_run')
    #     if self.is_in_air:
    #         if keys[pg.K_w]:
    #             self.set_state('shoot_jump_up')  # tiro enquanto olha para cima no ar
    #         elif keys[pg.K_s]:
    #             self.set_state('shoot_jump_down')  # tiro enquanto olha para baixo no ar
    #         else:
    #             self.set_state('shoot_jump')  # tiro padrao no ar
    #     elif self.is_crouched:
    #         self.set_state('shoot_shift')  # tiro agachado
    #     elif self.is_moving:
    #         if keys[pg.K_w]:
    #             self.set_state('shoot_run_up')  # tiro correndo olhando para cima
    #         else:
    #             self.set_state('shoot_run')  # tiro correndo normal
    #     else:
    #         if keys[pg.K_w]:  
    #             self.set_state('shoot_up') # tiro para cima  parado
    #         else:              
    #             self.set_state('shoot') # tiro normal parado
                
            
    def shoot_bullets(self, bullet_group: pg.sprite.Group):
        """
        Metodo responsavel por lidar com com o tiro de uma bala com um cooldown.
        Parameters
        ----------
        bullet_group: pg.sprite.Group
                Um grupo de sprites para armazenar as balas
        Returns
        -------
        self.bullet_group: pg.sprite.Group
                Um grupo de sprites com as balas ja armazenadas
        """
        self.bullet_group = bullet_group
        current_time = time.time()
        keys = pg.key.get_pressed()

        if current_time - self.last_shot_time >= self.bullet_cooldown:
            # mirando lateralmente
            
            if self.is_in_air:
                if keys[pg.K_w]:  # mirando pra cima no ar
                    self.direction = (0, -1)
                elif keys[pg.K_s]:  # mirando pra baixo no ar
                    self.direction = (0, 1)
            else:
                self.direction = self.facing
                
        # criando a bala
        self.bullet_player = Bullet(x=self.rect.centerx, y=self.rect.centery,
                        direction=self.direction, img_path="assets/Player/player_bullet.png", speed=10, dmg=5)
        self.bullet_group.add(self.bullet_player)  
        self.last_shot_time = current_time 

        return self.bullet_group

    
    def _jump(self):
        "Metodo responsavel pelo movimento de pulo"
        if self.jump_count < self.jump_count_max:
            self.set_state('jump')
            self.vel_y = -10
            self.jump_count += 1
            self.is_in_air = True

    def _on_out_of_bounds(self):
        if self.rect.right > SCREEN_WIDTH:  
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:  
            self.rect.left = 0
        if self.rect.top < 0:   
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:   
            self.rect.bottom = SCREEN_HEIGHT
            self.is_jumping = False

    def on_collision(self, other):
        """Metodo responsavel pela colisao do jogador com obstaculos"""
        if isinstance(other, Platform):
           # tolerancia para diferenciar colisoes horizontais e verticais
            self.__tolerance = 15

            if pg.sprite.collide_rect(self, other):
                # colisao inferior (superior da plataforma)
                if self.vel_y > 0 and abs(self.rect.bottom - other.rect.top) <= self.__tolerance:
                    self.rect.bottom = other.rect.top
                    self.vel_y = 0
                    self.jump_count = 0 
                    self.is_in_air = False
                
                    self.direction = self.facing

                    if self.is_crouched:
                        self.rect.top += 6

                # colisao superior (inferior da plataforma)
                elif self.vel_y < 0 and abs(self.rect.top - other.rect.bottom) <= self.__tolerance:
                    self.rect.top = other.rect.bottom
                    self.vel_y = 0

                # colisao lateral pela direita
                if self.dx > 0 and self.rect.right > other.rect.left and self.rect.left < other.rect.left:
                    if self.rect.bottom > other.rect.top + self.__tolerance and self.rect.top < other.rect.bottom - self.__tolerance:
                        self.rect.right = other.rect.left
                        self.dx = 0

                # colisao lateral pela esquerda
                elif self.dx < 0 and self.rect.left < other.rect.right and self.rect.right > other.rect.right:
                    if self.rect.bottom > other.rect.top + self.__tolerance and self.rect.top < other.rect.bottom - self.__tolerance:
                        self.rect.left = other.rect.right
                        self.dx = 0
                
    def set_state(self, new_state: str):
        """Muda o estado atual da animação (por exemplo, de 'run' para 'idle')."""
        if self.state != new_state:
            self.state = new_state
            self.index = 0
            self.image = self.images[self.state][self.index]
            self.current_time = 0

    def animate(self):
        """Atualiza a animação, trocando o frame atual baseado na velocidade."""
        self.current_time += self.animation_speed
        if self.current_time >= 1:
            self.index = (self.index + 1) % len(self.images[self.state])
            self.image = self.images[self.state][self.index]
            self.current_time = 0

    def update(self):
        """Metodo responsavel por atualizar a animação."""
        self.animate()

        if self.vel_y < 0:  # ascendente
            self.vel_y += self.gravity_up
        elif self.vel_y > 0:  # descendente
            self.vel_y += self.gravity_down
        else:  
            self.vel_y += (self.gravity_up + self.gravity_down) / 2

        # atualiza o movimento
        self.rect.y += self.vel_y
        self.rect.x += self.dx

        # if self.is_shooting:
        #     self.shoot()

    def draw(self, screen):
        """Módulo responsável por desenhar as sprites do jogador"""
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        self.update()
        self.movement()
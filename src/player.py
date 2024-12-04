"""Modulo dedicado a criacao do personagem principal e seus comportamentos"""

import pygame as pg
import os
import time
from bullet import Bullet
from map import Platform
from settings import PX_SCALE, SCREEN_HEIGHT, SCREEN_WIDTH
from utils import load_image
from entity import Entity

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
    def __init__(self, max_life, max_ammo, images_folders: dict, x: int, y: int, vel: int):
        super().__init__(images_folders, x, y)
        self.max_life = max_life
        self.life = max_life
        self.max_ammo = max_ammo
        self.ammo = max_ammo
        self.vel_x = vel
        self.dx = 0
        self.direction = (1,0) # quaisquer das 4 direcoes
        self.facing = (1, 0) # direcoes laterais
        self.flip = False
        self.animation_speed = 0.1
        self.current_time = 0
        self.is_moving = False
        self.is_crouched = False
        self.is_in_air = False
        self.gravity_up = 0.5  # gravidade na ascendencia do pulo
        self.gravity_down = 0.08 # gravidade na descendencia do pulo
        self.vel_y = 0
        self.jump_count = 0
        self.jump_count_max = 1
        self.jump_pressed = False
        self.bullet_cooldown = 0.1
        self.last_shot_time = time.time()
        self.is_reloading = False
        self.last_reload_time = time.time()
        self.reload_cooldown = 1.5
        self.is_dead = False
        self.hit_sound = pg.mixer.Sound("../assets/sounds/hitHurt.wav")
     
    
    def movement(self):
        """Módulo responsável pela movimentação do jogador"""
        if self.is_dead:  
            return

        keys = pg.key.get_pressed()

        self.dx = 0

        # agacha
        if (keys[pg.K_s] or keys[pg.K_DOWN]) and not self.is_in_air:
            self.set_state('crouch')
            self.is_crouched = True
        else:
            self.is_crouched = False

        # movimentaçao lateral
        if (keys[pg.K_a] or keys[pg.K_LEFT]) and not self.is_crouched:
            self.dx -= self.vel_x
            self.direction = (-1,0)
            self.facing = (-1,0)
            self.flip = True
            self.is_moving = True
            self.set_state('run')  
        elif (keys[pg.K_d] or keys[pg.K_RIGHT]) and not self.is_crouched:
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
        if keys[pg.K_SPACE] and not self.jump_pressed and not self.is_in_air:
            self._jump()
            self.jump_pressed = True

        # olhar para cima ou para baixo durante o pulo
        if self.is_in_air:
            if keys[pg.K_w] :
                self.set_state('jump_up')
            elif keys[pg.K_s] :
                self.set_state('jump_down')

        # resetar o pulo
        if not keys[pg.K_SPACE]:
            self.jump_pressed = False

    def shoot_bullets(self, bullet_group: pg.sprite.Group, shoot_sound : pg.mixer.Sound):
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
        if self.ammo > 0 and not self.is_reloading:

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
                                direction=self.direction, img_path="../assets/Player/player_bullet_3.png", speed=10, dmg=5)
                self.bullet_group.add(self.bullet_player)  
                self.last_shot_time = current_time 
                shoot_sound.play()
                self.ammo -= 1
                
        return self.bullet_group
    
    def die(self):
        """
        Logica de morte do jogador.
        """
        if not self.is_dead:
            self.set_state("die")
            self.is_dead = True  

        if self.is_dead:
            self.current_time += 0.1
            if self.current_time >= 1:
                self.index = (self.index + 1) % len(self.images[self.state])
                self.image = self.images[self.state][self.index]
                self.current_time = 0

                if self.index == len(self.images[self.state]) - 1:
                    print("Game Over!")
                    pg.quit()
                    exit()
        return   
            
    def reload(self):
        """Metodo responsavel por gerenciar a recarga de municao do jogador"""
        current_time = time.time()
        keys = pg.key.get_pressed()

        # Iniciar recarga se a tecla for pressionada e as condições forem atendidas
        if (keys[pg.K_r] or self.ammo == 0) and self.ammo < self.max_ammo and not self.is_reloading and current_time - self.last_reload_time >= self.reload_cooldown:
            self.is_reloading = True
            self.ammo = 0
            self.last_reload_time = current_time

        # Continua o processo de recarga se já estiver recarregando
        if self.is_reloading:
            time_per_bullet = self.reload_cooldown / self.max_ammo
            bullets_reloaded = int((current_time - self.last_reload_time) / time_per_bullet)
            
            # Garantir que self.ammo não ultrapasse self.max_ammo
            self.ammo = min(self.max_ammo, bullets_reloaded)

            # Finalizar recarga quando a munição atingir o máximo
            if self.ammo >= self.max_ammo:
                self.ammo = self.max_ammo
                self.is_reloading = False


    def _jump(self):
        "Metodo responsavel pelo movimento de pulo"
        if self.jump_count < self.jump_count_max:
            self.set_state('jump')
            self.vel_y = -10
            self.jump_count += 1
            self.is_in_air = True
            pg.mixer.Sound("../assets/sounds/jump.wav").play()

    def _on_out_of_bounds(self):
        """Metodo responsavel por impedir do jogador sair dos limites da tela"""
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
            self.__tolerance = 18

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
        """Metodo responsavel por atualizar o estado do jogador."""
        if self.life <= 0:
            self.die()
            return
        
        self.animate()
        self.reload()
        if self.vel_y < 0:  # ascendente
            self.vel_y += self.gravity_up
        elif self.vel_y > 0:  # descendente
            self.vel_y += self.gravity_down
        else:  
            self.vel_y += (self.gravity_up + self.gravity_down) / 2

        # atualiza o movimento
        self.rect.y += self.vel_y
        self.rect.x += self.dx

    def draw_hud(self, screen):
        """
        Módulo responsável por desenhar a HUD, que contém vida e munição
        Parameters
        ----------
        screen: pg.Surface
            Superficie onde o jogador será desenhado
        """
        # Define tamanho e coordenadas dos retangulos
        rect_width, rect_height = 100, 20
        health_x, health_y = 20, 20
        ammo_x, ammo_y = 140, 20

        health_ratio = self.life / self.max_life
        ammo_ratio = self.ammo / self.max_ammo
        green_width = int(rect_width * health_ratio)
        yellow_width = int(rect_width * ammo_ratio)

        # Desenha os retangulos
        pg.draw.rect(screen, (0, 0, 0), (health_x - 5, health_y - 5, rect_width + 10, rect_height + 10))
        pg.draw.rect(screen, (200, 0, 0), (health_x, health_y, rect_width, rect_height))
        pg.draw.rect(screen, (0, 100, 0), (health_x, health_y, green_width, rect_height))
        pg.draw.rect(screen, (0, 0, 0), (ammo_x - 5, ammo_y - 5, rect_width + 10, rect_height + 10))
        pg.draw.rect(screen, (200, 200, 0), (ammo_x, ammo_y, yellow_width, rect_height))

        # Escreve a quantidade de vida e munição
        font = pg.font.SysFont(None, 30)
        health_text = font.render(f"{self.life}/{self.max_life}", True, (255, 255, 255))
        health_text_rect = health_text.get_rect(center=(health_x + rect_width / 2, health_y + rect_height / 2 + 1))
        screen.blit(health_text, health_text_rect)
        ammo_text = font.render(f"{self.ammo}/{self.max_ammo}", True, (255, 255, 255))
        ammo_text_rect = health_text.get_rect(center=(10 + ammo_x + rect_width / 2, ammo_y + rect_height / 2 + 1))
        screen.blit(ammo_text, ammo_text_rect)

    def draw(self, screen):
        """
        Módulo responsável por desenhar as sprites do jogador
        Parameters
        ----------
        screen: pg.Surface
            Superficie onde o jogador será desenhado
        """
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        self.update()
        self.movement()
        self.draw_hud(screen)



    
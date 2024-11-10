
import pygame as pg
import os
from map import Platform

PX_SCALE = 1

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

        # TODO: passar a logica do load da imagem para uma funcao propria load_image em utils.py

        for state, folder in images_folders.items():      
            self.images[state] = []
            for img_name in os.listdir(folder):
                if img_name.endswith(".png"):
                    img_path = os.path.join(folder, img_name)
                    image = pg.image.load(img_path).convert_alpha()
                    
                    self.width, self.height = image.get_width(), image.get_height()
                    scaled_image = pg.transform.scale(image, (int(self.width * PX_SCALE), int(self.height * PX_SCALE)))

                    self.images[state].append(scaled_image)

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
    x:
        Posição do eixo x inicial do jogador
    y:
        Posição do eixo y inicial do jogador
    vel:
        Velocidade de movimento do jogador
    """
    def __init__(self, images_folders: dict, x: int, y: int, vel: int):
        super().__init__(images_folders, x, y)
        self.vel_x = vel
        self.dx = 0
        self.direction = 1
        self.flip = False
        self.animation_speed = 0.1
        self.current_time = 0
        self.is_moving = False
        self.is_shooting = False
        self.is_crouched = False
        self.is_jumping = False
        self.gravity_y = 0.75
        self.vel_y = 0
        self.jump_count = 0
        self.jump_count_max = 1
        self.jump_pressed = False
     
    
    def movement(self):
        """Módulo responsável pela movimentação do jogador"""
        keys = pg.key.get_pressed()

        self.dx = 0

        #TODO: impedir que 'a' e 'd' sejam pressionadas enquanto agachado e 
        # dar um delay para reconhece-las (personagem levantar)

        if keys[pg.K_s]:  
            self.set_state('crouch')
            self.is_crouched = True

        elif keys[pg.K_a]:  
            self.dx  -= self.vel_x
            self.direction = -1
            self.flip = True
            self.is_moving = True
            self.set_state('run')  
        elif keys[pg.K_d]:  
            self.dx += self.vel_x
            self.direction = 1
            self.flip = False
            self.is_moving = True
            self.set_state('run') 

        else:
            self.set_state('idle')
            self.is_crouched = False

        if keys[pg.K_SPACE] and not self.jump_pressed:
             self._jump()
             self.jump_pressed = True

        if not keys[pg.K_SPACE]:
            self.jump_pressed = False

    def _jump(self):
        "Metodo responsavel pelo movimento de pulo"
        if self.jump_count < self.jump_count_max:
            self.is_jumping = True
            self.set_state('jump')
            self.vel_y = -11
            self.jump_count += 1

    def on_collision(self, other):
        """Metodo responsavel pela colisao do jogador com outros objetos"""
        if isinstance(other, Platform):
            # colisão inferior (superior da plataforma)
            if self.vel_y > 0:
                self.rect.bottom = other.rect.top
                self.vel_y = 0
                self.jump_count = 0  
                
                # colisao de agachamento
                if self.is_crouched:
                    self.rect.top += 6
            
            # colisão superior (inferior da plataforma)
            elif self.vel_y < 0:
                self.rect.top = other.rect.bottom
                self.vel_y = 0

            #TODO: impedir que o player suba na plataforma ao colidir na direita

            # colisão pela direita
            if self.dx > 0 and self.rect.right > other.rect.left and self.rect.left < other.rect.left:
                self.rect.right = other.rect.left 
                self.dx = 0

            #TODO: implementar colisao pela esquerda

            # colisão pela esquerda
            # elif self.dx < 0:
            #     if self.rect.left < other.rect.right and self.rect.right > other.rect.right:
            #         self.rect.left = other.rect.right
            #         self.dx = 0
            
    def set_state(self, new_state: str):
        """Muda o estado atual da animação (por exemplo, de 'run' para 'idle')."""
        if self.state != new_state:
            self.state = new_state
            self.index = 0

            self.image = self.images[self.state][self.index]
            self.current_time = 0

    def animate(self):
        """Atualiza a animação, trocando o frame atual baseado na velocidade."""
        if self.is_moving:
            self.current_time += self.animation_speed
            if self.current_time >= 1:
                self.index = (self.index + 1) % len(self.images[self.state])
                self.image = self.images[self.state][self.index]
                self.current_time = 0
        else:
            self.image = self.images['idle'][self.index]  

    def update(self):
        """Metodo responsavel por atualizar a animação."""
        self.animate()
        self.vel_y += self.gravity_y
        self.rect.y += self.vel_y
        self.rect.x += self.dx


    def draw(self, screen):
        """Módulo responsável por desenhar as sprites do jogador"""
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        self.update()
        self.movement()


import pygame as pg
import os

GRAVITY = 0.5
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
            self.images[state] = [pg.image.load(os.path.join(folder, img)) for img in os.listdir(folder) if img.endswith(".png")]
        
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
        self.vel = vel
        self.direction = 1
        self.flip = False
        self.animation_speed = 0.2
        self.current_time = 0
        self.is_moving = False
        self.is_shooting = False
        self.is_crouched = False
        self.is_jumping = False
        self.vel_y = 2
        self.jump_count = 0
        self.jump_count_max = 1
     
    
    def movement(self):
        """Módulo responsável pela movimentação do jogador"""
        keys = pg.key.get_pressed()

        if keys[pg.K_s]:  # Agachar
            self.set_state('crouch')
            self.is_crouched = True

        elif keys[pg.K_a]:  
                    self.rect.x -= self.vel
                    self.direction = -1
                    self.flip = True
                    self.is_moving = True
                    self.set_state('run')  
        elif keys[pg.K_d]:  
                    self.rect.x += self.vel
                    self.direction = 1
                    self.flip = False
                    self.is_moving = True
                    self.set_state('run')  
        else:
                    self.set_state('idle')

        
        if keys[pg.K_SPACE]:
            self.is_jumping = True
            self.set_state('jump')
            self.rect.y -= self.vel_y

    
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
        """Método responsável por atualizar a animação."""
        self.animate()

    def draw(self, screen):
        """Módulo responsável por desenhar as sprites do jogador"""
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)
        self.movement()
        self.update()

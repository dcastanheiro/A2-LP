"""Esse módulo importa todas as classes necessárias e inicia o jogo"""

import pygame as pg
from player import Player
from enemy import Enemy, ArEnemy
from map import Platform, Background
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TILE_SIZE, player_all_images_folders, map_layout, background_layers, map_tiles, bazooka_enemy_images_folders, sniper_enemy_images_folders, ar_enemy_images_folders
from bullet import Bullet
warnings.filterwarnings("ignore", category=UserWarning, module="PIL.PngImagePlugin")
class Game:
    """
    Classe que administra o funcionamento geral do jogo.
    """
    def __init__(self, difficulty: str, game_manager) -> None:
        pg.init()
        pg.mixer.init()
        self.difficulty = difficulty
        self.game_manager = game_manager

        # Configura o multiplicador de dano com base na dificuldade
        self.damage_multiplier = {
            "normal": 1.0,
            "hard": 1.5,
            "insane": 2.0
        }.get(self.difficulty, 1.0)

        # setando a tela
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Run n Gun')

        # inicializar o background em camadas
        self.background = Background(
            background_layers,
            screen_width=self.width,
            screen_height=self.height
        )

        # inicializando objetos
        self.player = Player(100, 30, player_all_images_folders, x=20, y=30, vel=1)
        self.platforms = Platform.create_platform(map_layout=map_layout, img_path=map_tiles)

        # criar os grupos de balas dos inimigos
        self.bazooka_bullets = pg.sprite.Group()
        self.sniper_bullets = pg.sprite.Group()
        self.ar_bullets = pg.sprite.Group()

        # criar o grupo dos inimigos
        self.enemies = pg.sprite.Group()

        # cria os inimigos 
        self.bazooka_enemy = Enemy(
            bazooka_enemy_images_folders,
            x=320,
            y=210,
            life=40,
            bullet_group=self.bazooka_bullets,
            bullet_type="bazooka",
            shoot_interval=2,
            damage_multiplier=self.damage_multiplier
        )

        self.bazooka_enemy_2 = Enemy(
            bazooka_enemy_images_folders,
            x=750,
            y=230,
            life=40,
            bullet_group=self.bazooka_bullets,
            bullet_type="bazooka",
            shoot_interval=2,
            damage_multiplier=self.damage_multiplier
        )

        self.bazooka_enemy_3 = Enemy(
            bazooka_enemy_images_folders,
            x=1260,
            y=150,
            life=40,
            bullet_group=self.bazooka_bullets,
            bullet_type="bazooka",
            shoot_interval=2,
            damage_multiplier=self.damage_multiplier,
            flip = True
        )

        self.bazooka_enemy_4 = Enemy(
            bazooka_enemy_images_folders,
            x=1260,
            y=370,
            life=40,
            bullet_group=self.bazooka_bullets,
            bullet_type="bazooka",
            shoot_interval=2,
            damage_multiplier=self.damage_multiplier,
            flip = True
        )

        self.bazooka_enemy_5 = Enemy(
            bazooka_enemy_images_folders,
            x=1270,
            y=630,
            life=40,
            bullet_group=self.bazooka_bullets,
            bullet_type="bazooka",
            shoot_interval=2,
            damage_multiplier=self.damage_multiplier,
            flip=True
        )

        self.bazooka_enemy_6 = Enemy(
            bazooka_enemy_images_folders,
            x=1270,
            y=510,
            life=40,
            bullet_group=self.bazooka_bullets,
            bullet_type="bazooka",
            shoot_interval=2,
            damage_multiplier=self.damage_multiplier,
            flip=True
        )

        self.sniper_enemy_1 = Enemy(
            sniper_enemy_images_folders,
            x=890,
            y=90,
            life=30,
            bullet_group=self.sniper_bullets,
            bullet_type="sniper",
            shoot_interval=1.0,
            damage_multiplier=self.damage_multiplier, 
            flip = True
        )

        self.sniper_enemy_2 = Enemy(
            sniper_enemy_images_folders,
            x=20,
            y=270,
            life=30,
            bullet_group=self.sniper_bullets,
            bullet_type="sniper",
            shoot_interval=1.0,
            damage_multiplier=self.damage_multiplier
        )

        self.sniper_enemy_3 = Enemy(
            sniper_enemy_images_folders,
            x=600,
            y=150,
            life=30,
            bullet_group=self.sniper_bullets,
            bullet_type="sniper",
            shoot_interval=1.0,
            damage_multiplier=self.damage_multiplier
        )

        self.sniper_enemy_4 = Enemy(
            sniper_enemy_images_folders,
            x=520,
            y=230,
            life=30,
            bullet_group=self.sniper_bullets,
            bullet_type="sniper",
            shoot_interval=1.0,
            damage_multiplier=self.damage_multiplier
        )

        self.sniper_enemy_5 = Enemy(
            sniper_enemy_images_folders,
            x=920,
            y=370,
            life=30,
            bullet_group=self.sniper_bullets,
            bullet_type="sniper",
            shoot_interval=1.0,
            damage_multiplier=self.damage_multiplier,
            flip=True
        )

        self.sniper_enemy_6 = Enemy(
            sniper_enemy_images_folders,
            x=255,
            y=470,
            life=30,
            bullet_group=self.sniper_bullets,
            bullet_type="sniper",
            shoot_interval=1.0,
            damage_multiplier=self.damage_multiplier
        )

        self.sniper_enemy_7 = Enemy(
            sniper_enemy_images_folders,
            x=500,
            y=570,
            life=30,
            bullet_group=self.sniper_bullets,
            bullet_type="sniper",
            shoot_interval=1.0,
            damage_multiplier=self.damage_multiplier,
            flip=True
        )

        self.ar_enemy_1 = ArEnemy(
            ar_enemy_images_folders,
            x=600,
            y=145,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )
        
        self.ar_enemy_2 = ArEnemy(
            ar_enemy_images_folders,
            x=890,
            y=305,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )

        self.ar_enemy_3 = ArEnemy(
            ar_enemy_images_folders,
            x=500,
            y=405,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )

        self.ar_enemy_4 = ArEnemy(
            ar_enemy_images_folders,
            x=100,
            y=405,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )

        self.ar_enemy_5 = ArEnemy(
            ar_enemy_images_folders,
            x=200,
            y=665,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )

        self.ar_enemy_6 = ArEnemy(
            ar_enemy_images_folders,
            x=400,
            y=665,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )

        self.ar_enemy_7 = ArEnemy(
            ar_enemy_images_folders,
            x=800,
            y=665,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )

        self.ar_enemy_8 = ArEnemy(
            ar_enemy_images_folders,
            x=800,
            y=505,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,
            damage_multiplier=self.damage_multiplier
        )

        self.ar_enemy_9 = ArEnemy(
            ar_enemy_images_folders,
            x=500,
            y=505,
            life=30,
            bullet_group=self.ar_bullets,
            bullet_type="ar",
            shoot_interval=0.5,
            patrol_speed=1.5,damage_multiplier=self.damage_multiplier)

        self.enemies.add(self.bazooka_enemy, self.bazooka_enemy_2, self.bazooka_enemy_3, self.bazooka_enemy_4, self.bazooka_enemy_5, self.bazooka_enemy_6,
                         self.ar_enemy_1, self.ar_enemy_2, self.ar_enemy_3, self.ar_enemy_4, self.ar_enemy_5, self.ar_enemy_6, self.ar_enemy_7, self.ar_enemy_8, self.ar_enemy_9,
                         self.sniper_enemy_1, self.sniper_enemy_2, self.sniper_enemy_3, self.sniper_enemy_4, self.sniper_enemy_5, self.sniper_enemy_6, self.sniper_enemy_7)

        # inicializando grupo de sprites
        self.bullet_group = pg.sprite.Group()
        self.bullet_enemies_group = pg.sprite.Group()
        self.platform_group = pg.sprite.Group()

        for platform in self.platforms:
            self.platform_group.add(platform)

        self.clock = None
        self.run = False

    def running(self):
        """Método que inicializa o jogo"""
        self.clock = pg.time.Clock()
        self.run = True
        while self.run:
            if self.game_manager.current_screen == "main_menu":  # Checa o estado do jogo
                self.run = False
                break
            self.on_event()
            self.update()
            self.draw()
            self.clock.tick(60)
        pg.quit()

    
    def on_event(self):
        """Metodo responsavel por controlar os eventos do jogo"""
        events = pg.event.get()
        keys = pg.key.get_pressed()
        for event in events:
            if event.type == pg.QUIT:
              self.run = False
            elif (event.type == pg.MOUSEBUTTONDOWN and event.button == 1) or keys[pg.K_c]:
                self.player.shoot_bullets(self.bullet_group, pg.mixer.Sound("../assets/sounds/laserShoot.wav"))
                self.player.is_shooting = True
            else:
                 self.player.is_shooting = False   

    def update(self):
        """Metodo para atualizar o jogo"""
        self.background.update()
        self.player.update()
        self.bullet_group.update()
        self.bullet_enemies_group.update()
        for platform in self.platforms:
            platform.update()

        for enemy in self.enemies:
            enemy.update(self.player.rect.centerx, self.player.rect.centery, self.platform_group)
            self.bullet_enemies_group.add(enemy.bullet_group)

        self.check_collision()
        self.check_bullets_colission()
        self.check_victory()
        self.check_dead()
        self.player._on_out_of_bounds()
        pg.display.update()  
        
    def check_collision(self):
        """Metodo responsavel pela colisao entre objetos do mapa"""
        # colisao do player com plataformas
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                self.player.on_collision(platform)
                platform.on_collision(self.player)

    def check_bullets_colission(self):
        """Metodo responsavel por lidar com as colisões entre balas, inimigos e jogador."""
        # colisao das balas com plataformas
        for bullet in self.bullet_group:
            if pg.sprite.spritecollideany(bullet, self.platform_group):
                bullet.kill()
        for bullet in self.bullet_enemies_group:
            if pg.sprite.spritecollideany(bullet, self.platform_group):
                bullet.kill() 
        
        # colisao das balas do jogador com os inimigos
        for bullet in self.bullet_group:
            for enemy in self.enemies:
                if not enemy.is_dead and bullet.rect.colliderect(enemy.rect):
                    enemy.take_damage(bullet.dmg)
                    bullet.kill()  

        # colisao das balas dos inimigos com o jogador
        for bullet in self.bullet_enemies_group:
            if bullet.rect.colliderect(self.player.rect):
                self.player.life -= bullet.dmg
                self.player.hit_sound.play()
                bullet.kill()  

    def draw_grid(self):
        """Metodo para desenhar o grid na tela."""
        for x in range(0, self.width, TILE_SIZE):
            pg.draw.line(self.screen, (50, 50, 50), (x, 0), (x, self.height))  
        for y in range(0, self.height, TILE_SIZE):
            pg.draw.line(self.screen, (50, 50, 50), (0, y), (self.width, y))

    def draw(self):
        """Metodo responsavel por desenhar os objetos na tela"""
        self.background.draw(self.screen)
        #self.draw_grid()
        for platform in self.platforms:
            platform.draw(self.screen)
        for enemie in self.enemies:
            enemie.draw(self.screen)
        self.player.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.bullet_enemies_group.draw(self.screen)
        pg.display.flip()

    def check_dead(self):
        """
        Verifica se o jogador esta morto e retorna ao menu.
        """
        if self.player.is_dead:
            self.game_manager.change_state("main_menu")

    def check_victory(self):
        """
        Metodo responsavel por cuidar da checagem de vitoria do jogador.
        """
        # verifica se todos os inimigos estão mortos
        all_enemies_dead = all(enemy.is_dead for enemy in self.enemies)

        # verifica se o jogador colidiu com a letra 'e'
        player_collided_with_e = any(
            platform.tile_type == 'e' and self.player.rect.colliderect(platform.rect)
            for platform in self.platforms
        )

        if all_enemies_dead and player_collided_with_e:
            print("Parabéns! Voce venceu o jogo!")
            self.run = False 
             


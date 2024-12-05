"""Modulo responsavel por iniciar o Menu e cuidar da integracao com o jogo"""

import pygame as pg
import sys
import os
from game import Game

pg.init()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Run 'n Gun")

#cores escolhidas para os botões
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
YELLOW = (255, 215, 0)
RED = (255, 0, 0)

#paths que serão úteis pro menu
base_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(base_dir, "..", "assets", "fonts", "PressStart2P-Regular.ttf")
background_path = os.path.join(base_dir, "..", "assets", "Assets_area_1", "Background", "subway_BG.png")
tutorial_path = os.path.join(base_dir, "..", "assets", "tutorial", "tutorial.png")

#carregar a fonte de texto escolhida
if os.path.exists(font_path):
    font = pg.font.Font(font_path, 32)
    small_font = pg.font.Font(font_path, 20)
else:
    font = pg.font.SysFont("arial", 32)
    small_font = pg.font.SysFont("arial", 20)

#carregar o background do menu através do path e da imagem que escolhemos
if os.path.exists(background_path):
    background_image = pg.image.load(background_path)
    background_image = pg.transform.scale(background_image, (screen_width, screen_height))
else:
    background_image = None

#carregar a imagem do tutorial
if os.path.exists(tutorial_path):
    tutorial_image = pg.image.load(tutorial_path)
    tutorial_image = pg.transform.scale(tutorial_image, (screen_width, screen_height))
else:
    tutorial_image = None

#menu principal
class MainMenu:
    """
    Classe responsavel por fazer o design do menu principal
    """

    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        """Metodo responsavel por desenhar o background do menu"""
        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(WHITE)


        #botões do menu
        play_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        tutorial_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 20, 200, 50)
        exit_button = pg.Rect(20, 20, 100, 40)

        pg.draw.rect(screen, WHITE, play_button, 2)
        pg.draw.rect(screen, WHITE, tutorial_button, 2)
        pg.draw.rect(screen, RED, exit_button, 2)

        self.draw_text("Run 'n Gun", font, WHITE, screen_width // 2 - 170, 50)
        self.draw_text("Play", small_font, WHITE, screen_width // 2 - 43, screen_height // 2 - 40)
        self.draw_text("Tutorial", small_font, WHITE, screen_width // 2 - 80, screen_height // 2 + 30)
        self.draw_text("Exit", small_font, RED, 30, 30)
        self.draw_text("CREDITS:", small_font, WHITE, 10, screen_height - 90)
        self.draw_text("Bernardo de Vasconcellos", small_font, WHITE, 10, screen_height - 70)
        self.draw_text("Dilmar Castanheiro", small_font, WHITE, 10, screen_height - 50)
        self.draw_text("Matheus Constantin", small_font, WHITE, 10, screen_height - 30) 
        
    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
                self.game_manager.change_state("game_level")
            
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 + 20 < mouse_y < screen_height // 2 + 70:
                self.game_manager.change_state("tutorial")

            if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                self.game_manager.is_running = False

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        """Metodo responsavel por desenhar o texto do menu"""
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

#dando classe a página do tutorial
class TutorialScreen:
    """
    Classe responsavel por criar os butoes e imagens do tutorial
    """

    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        """Metodo responsavel por desenhar a imagem do tutorial"""
        if tutorial_image:
            screen.blit(tutorial_image, (0, 0))
        else:
            screen.fill(WHITE)
            self.draw_text("Tutorial image not found!", font, RED, screen_width // 2 - 200, screen_height // 2 - 20)

        exit_button = pg.Rect(20, 20, 100, 40)
        pg.draw.rect(screen, RED, exit_button, 2)
        self.draw_text("Exit", small_font, RED, 30, 30)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                self.game_manager.change_state("main_menu")

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        """Metodo responsavel por desenhar o texto do tutorial"""
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

class GameLevel:
    """
    Classe responsavel por lidar com os estados do menu
    """

    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        """Metodo responsavel por desenhar a tela de escolha do mapa"""
        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(WHITE)

        map1_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        exit_button = pg.Rect(20, 20, 100, 40)

        pg.draw.rect(screen, WHITE, map1_button, 2)
        pg.draw.rect(screen, RED, exit_button, 2)

        self.draw_text("Choose the Map", font, WHITE, screen_width // 2 - 215, 50)
        self.draw_text("Exit", small_font, RED, 30, 30)
        self.draw_text("Map 1", small_font, WHITE, screen_width // 2 - 50, screen_height // 2 - 40)
        self.draw_text("Exit", small_font, RED, 30, 30)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
                self.game_manager.change_state("choose_difficulty")

            if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                self.game_manager.change_state("main_menu")

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

#escolha da dificuldade
class ChooseDifficulty:
    """
    Classe responsavel por criar o design dos botoes de dificuldade e interacoes
    """
    
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        """
        Metodo responsavel por desenhar os botoes de dificuldade
        """
        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(WHITE)

        normal_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        hard_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 10, 200, 50)
        insane_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 70, 200, 50)
        exit_button = pg.Rect(20, 20, 100, 40)

        pg.draw.rect(screen, GREEN, normal_button, 2)
        pg.draw.rect(screen, YELLOW, hard_button, 2)
        pg.draw.rect(screen, RED, insane_button, 2)
        pg.draw.rect(screen, RED, exit_button, 2)

        self.draw_text("Difficulty Level", font, WHITE, screen_width // 2 - 230, 50)
        self.draw_text("Normal", small_font, GREEN, screen_width // 2 - 60, screen_height // 2 - 40)
        self.draw_text("Hard", small_font, YELLOW, screen_width // 2 - 40, screen_height // 2 + 20)
        self.draw_text("Insane", small_font, RED, screen_width // 2 - 65, screen_height // 2 + 80)
        self.draw_text("Exit", small_font, RED, 30, 30)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
                self.game_manager.start_game("normal")

            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 + 10 < mouse_y < screen_height // 2 + 60:
                self.game_manager.start_game("hard")

            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 + 70 < mouse_y < screen_height // 2 + 120:
                self.game_manager.start_game("insane")

            if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                self.game_manager.change_state("main_menu")

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        """Metodo responsavel por desenhar o texto da escolha de dificuldade"""
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

#gerenciador de jogo""
class GameManager:
    """
    Classe responsável por fazer integracao do menu com o jogo e inicializar o menu
    """
    def __init__(self):
        self.screen_map = {
            "main_menu": MainMenu(self),
            "tutorial": TutorialScreen(self),
            "game_level": GameLevel(self),
            "choose_difficulty": ChooseDifficulty(self)
        }
        self.current_screen = self.screen_map["main_menu"]
        self.is_running = False
        self.game = None

    def change_state(self, screen_name):
        """
        Metodo responsavel por lidar com o estado do jogo e do menu
        """
        if screen_name in self.screen_map:
            self.current_screen = self.screen_map[screen_name]
    
    def start_game(self, difficulty):
        """
        Inicia o jogo com a dificuldade selecionada.
        """
        self.game = Game(difficulty, self)
        self.is_running = False  

    def run(self):
        self.is_running = True
        clock = pg.time.Clock()
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                self.current_screen.on_event(event)

            self.current_screen.update()
            self.current_screen.draw(screen)
            pg.display.flip()
            clock.tick(30)

        if self.game:
            self.game.running()

        pg.quit()
        sys.exit()

#iniciar o pygame
game_manager = GameManager()
game_manager.run()

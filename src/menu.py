import pygame as pg
import sys

pg.init()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Run 'n gun")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# configurações da fonte que usamos
font_path = 'assets/fonts/PressStart2P-Regular.ttf'
font = pg.font.Font(font_path, 32)
small_font = pg.font.Font(font_path, 20)

class MainMenu:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_text("Run 'n gun", font, WHITE, screen_width // 2 - 120, 50)

        # desenhar os botões "Play" e "Exit"
        play_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        exit_button = pg.Rect(20, 20, 100, 40)

        pg.draw.rect(screen, RED, play_button)
        pg.draw.rect(screen, RED, exit_button)

        self.draw_text("Play", small_font, WHITE, screen_width // 2 - 30, screen_height // 2 - 40)
        self.draw_text("Exit", small_font, WHITE, 40, 30)
        self.draw_text("Bernardo Vasconcelos, Dilmar Castanheiro, Matheus Constantin", small_font, WHITE, 10, screen_height - 30)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            # verificar se o botão "Play" foi clicado
            if  screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
                self.game_manager.change_state("game_level")

            # verificar se o botão "Exit" foi clicado
            if 20 < mouse_x < 120 and 20 < mouse_y < 60:
                self.game_manager.is_running = False

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

class GameLevel:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        screen.fill((0, 0, 0))

        self.draw_text("Escolha o Mapa", font, WHITE, screen_width // 2 - 150, 50)

        # mapa 1
        map1_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        pg.draw.rect(screen, RED, map1_button)
        self.draw_text("Mapa 1", small_font, WHITE, screen_width // 2 - 30, screen_height // 2 - 40)

        # voltar ao menu
        back_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 20, 200, 50)
        pg.draw.rect(screen, RED, back_button)
        self.draw_text("Voltar", small_font, WHITE, screen_width // 2 - 30, screen_height // 2 + 30)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            # verifica se o botão "Mapa 1" foi clicado
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
                self.game_manager.change_state("choose_difficulty")

            # verifica se o botão "Voltar" foi clicado
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 + 20 < mouse_y < screen_height // 2 + 70:
                self.game_manager.change_state("main_menu")

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

class ChooseDifficulty:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_text("Escolha a Dificuldade", font, WHITE, screen_width // 2 - 150, 50)

        # botões de dificuldade
        normal_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        hard_button = pg.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)
        insane_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)

        pg.draw.rect(screen, RED, normal_button)
        pg.draw.rect(screen, RED, hard_button)
        pg.draw.rect(screen, RED, insane_button)

        self.draw_text("Normal", small_font, WHITE, screen_width // 2 - 30, screen_height // 2 - 40)
        self.draw_text("Hard", small_font, WHITE, screen_width // 2 - 30, screen_height // 2 + 10)
        self.draw_text("Insane", small_font, WHITE, screen_width // 2 - 30, screen_height // 2 + 60)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            # verificar se um dos botões de dificuldade foi clicado
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
                print("Dificuldade: Normal")
                self.game_manager.is_running = False
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 < mouse_y < screen_height // 2 + 50:
                print("Dificuldade: Hard")
                self.game_manager.is_running = False
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 + 50 < mouse_y < screen_height // 2 + 100:
                print("Dificuldade: Insane")
                self.game_manager.is_running = False

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

class GameManager:
    def __init__(self):
        self.screen = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Run 'n gun")
        self.screen_map = {
            "main_menu": MainMenu(self),
            "game_level": GameLevel(self),
            "choose_difficulty": ChooseDifficulty(self)
        }

        self.current_screen = self.screen_map["main_menu"]

        self.is_running = False
        self.clock = None

    def change_state(self, screen_name):
        self.current_screen = self.screen_map[screen_name]

    def run(self):
        self.is_running = True
        self.clock = pg.time.Clock()
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                self.current_screen.on_event(event)

            self.current_screen.update()
            self.current_screen.draw(self.screen)

            self.clock.tick(30)

        pg.quit()
        sys.exit()

# Criar uma instância do GameManager e iniciar o jogo
game_manager = GameManager()
game_manager.run()

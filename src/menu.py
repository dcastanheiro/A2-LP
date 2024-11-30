import pygame as pg
import sys
import os

os.environ["SDL_VIDEODRIVER"] = "x11"

pg.init()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Run 'n gun")

# Cores
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
YELLOW = (255, 215, 0)
RED = (255, 0, 0)
DARK_GRAY = (50, 50, 50)

# Determinar caminho dinâmico da fonte
base_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(base_dir, "..", "assets", "fonts", "PressStart2P-Regular.ttf")

# Carregar fontes com fallback
if os.path.exists(font_path):
    font = pg.font.Font(font_path, 32)
    small_font = pg.font.Font(font_path, 20)
else:
    print(f"Fonte não encontrada em {font_path}. Usando fonte padrão do sistema.")
    font = pg.font.SysFont("arial", 32)
    small_font = pg.font.SysFont("arial", 20)

class MainMenu:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def draw(self, screen):
        screen.fill(DARK_GRAY)

        self.draw_text("Run 'n gun", font, WHITE, screen_width // 2 - 200, 50)

        # botões
        play_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        exit_button = pg.Rect(20, 20, 100, 40)

        pg.draw.rect(screen, WHITE, play_button, 2)  # borda branca do botão Play
        pg.draw.rect(screen, RED, exit_button, 2)  # borda branca do botão Exit

        self.draw_text("Play", small_font, WHITE, screen_width // 2 - 30, screen_height // 2 - 40)
        self.draw_text("Exit", small_font, RED, 40, 30)
        self.draw_text("CREDITS:", small_font, WHITE, 10, screen_height - 90)
        self.draw_text("Bernardo de Vasconcellos", small_font, WHITE, 10, screen_height - 70)
        self.draw_text("Dilmar Castanheiro", small_font, WHITE, 10, screen_height - 50)
        self.draw_text("Matheus Constantin", small_font, WHITE, 10, screen_height - 30)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            # verificar se o botão "Play" foi clicado
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
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
        screen.fill(DARK_GRAY)

        self.draw_text("Choose the Map", font, WHITE, screen_width // 2 - 150, 50)

        # Botão para Mapa 1
        map1_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        pg.draw.rect(screen, WHITE, map1_button, 2)
        self.draw_text("Map 1", small_font, WHITE, screen_width // 2 - 50, screen_height // 2 - 40)

        back_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 20, 200, 50)
        pg.draw.rect(screen, RED, back_button, 2)
        self.draw_text("Back", small_font, RED, screen_width // 2 - 50, screen_height // 2 + 30)

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
        screen.fill(DARK_GRAY)
        self.draw_text("Escolha a Dificuldade", font, WHITE, screen_width // 2 - 250, 50)

        # Botões de dificuldade
        normal_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        hard_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 10, 200, 50)
        insane_button = pg.Rect(screen_width // 2 - 100, screen_height // 2 + 70, 200, 50)

        pg.draw.rect(screen, GREEN, normal_button, 2)
        pg.draw.rect(screen, YELLOW, hard_button, 2)
        pg.draw.rect(screen, RED, insane_button, 2)

        self.draw_text("Normal", small_font, GREEN, screen_width // 2 - 50, screen_height // 2 - 40)
        self.draw_text("Hard", small_font, YELLOW, screen_width // 2 - 30, screen_height // 2 + 20)
        self.draw_text("Insane", small_font, RED, screen_width // 2 - 50, screen_height // 2 + 80)

    def on_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()

            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 - 50 < mouse_y < screen_height // 2:
                print("Dificuldade: Normal")
                self.game_manager.is_running = False
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 + 10 < mouse_y < screen_height // 2 + 60:
                print("Dificuldade: Hard")
                self.game_manager.is_running = False
            if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 + 70 < mouse_y < screen_height // 2 + 120:
                print("Dificuldade: Insane")
                self.game_manager.is_running = False

    def update(self):
        pass

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

class GameManager:
    def __init__(self):
        self.screen_map = {
            "main_menu": MainMenu(self),
            "game_level": GameLevel(self),
            "choose_difficulty": ChooseDifficulty(self)
        }
        self.current_screen = self.screen_map["main_menu"]
        self.is_running = False

    def change_state(self, screen_name):
        print(f"Trocando para o estado: {screen_name}")
        if screen_name not in self.screen_map:
            print(f"Erro: '{screen_name}' não encontrado em screen_map!")
        self.current_screen = self.screen_map[screen_name]

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

        pg.quit()
        sys.exit()

game_manager = GameManager()
game_manager.run()

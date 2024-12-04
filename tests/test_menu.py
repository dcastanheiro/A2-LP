import sys
import os
import unittest

# Adiciona o diretório 'src' ao sys.path para garantir que o Python encontre o módulo 'menu'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from menu import GameManager, MainMenu, TutorialScreen, GameLevel, ChooseDifficulty

class TestMenu(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente antes de cada teste."""
        self.game_manager = GameManager()
        self.main_menu = MainMenu(self.game_manager)
        self.tutorial_screen = TutorialScreen(self.game_manager)
        self.game_level = GameLevel(self.game_manager)
        self.choose_difficulty = ChooseDifficulty(self.game_manager)

    def test_game_manager(self):
        """Teste de inicialização do GameManager"""
        self.assertIsInstance(self.game_manager, GameManager)

    def test_main_menu(self):
        """Teste de inicialização do MainMenu"""
        self.assertIsInstance(self.main_menu, MainMenu)

    def test_tutorial_screen(self):
        """Teste de inicialização do TutorialScreen"""
        self.assertIsInstance(self.tutorial_screen, TutorialScreen)

    def test_game_level(self):
        """Teste de inicialização do GameLevel"""
        self.assertIsInstance(self.game_level, GameLevel)

    def test_choose_difficulty(self):
        """Teste de inicialização do ChooseDifficulty"""
        self.assertIsInstance(self.choose_difficulty, ChooseDifficulty)

if __name__ == '__main__':
    unittest.main()


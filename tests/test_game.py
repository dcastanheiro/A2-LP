import unittest
from unittest.mock import MagicMock, patch
import pygame as pg
import sys
import os

# Garante que o diretório src esteja no caminho do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from game import Game
from player import Player
from enemy import Enemy
from map import Platform, Background

class TestGame(unittest.TestCase):

    def setUp(self):
        # Mocka o gerenciador de estado
        self.mock_game_manager = MagicMock()
        self.mock_game_manager.current_screen = "game"

        # Cria uma instância do jogo para testes
        self.game = Game("normal", self.mock_game_manager)

    def test_initialization(self):
        """Testa se a inicialização do jogo ocorre corretamente."""
        self.assertEqual(self.game.difficulty, "normal")
        self.assertEqual(self.game.damage_multiplier, 1.0)
        self.assertTrue(isinstance(self.game.player, Player))
        self.assertTrue(len(self.game.enemies) > 0)
        self.assertTrue(isinstance(self.game.background, Background))

    @patch('pygame.event.get')
    def test_on_event_quit(self, mock_event_get):
        """Testa se o evento QUIT encerra o jogo."""
        mock_event_get.return_value = [pg.event.Event(pg.QUIT, {})]

        self.game.on_event()

        self.assertFalse(self.game.run)

    @patch('pygame.event.get')
    @patch('pygame.key.get_pressed')
    @patch('pygame.mixer.Sound')
    def test_on_event_shoot(self, mock_sound, mock_key_get_pressed, mock_event_get):
        """Testa se o jogador atira corretamente."""
        mock_event_get.return_value = []
        mock_key_get_pressed.return_value = {pg.K_c: True}

        self.game.player.shoot_bullets = MagicMock()

        self.game.on_event()

        self.game.player.shoot_bullets.assert_called_once()

    def test_update(self):
        """Testa se a atualização dos componentes do jogo ocorre corretamente."""
        self.game.background.update = MagicMock()
        self.game.player.update = MagicMock()
        self.game.bullet_group.update = MagicMock()
        self.game.bullet_enemies_group.update = MagicMock()

        for enemy in self.game.enemies:
            enemy.update = MagicMock()

        self.game.update()

        self.game.background.update.assert_called_once()
        self.game.player.update.assert_called_once()
        self.game.bullet_group.update.assert_called_once()
        self.game.bullet_enemies_group.update.assert_called_once()
        for enemy in self.game.enemies:
            enemy.update.assert_called()

    def test_check_dead(self):
        """Testa a funcionalidade de verificar se o jogador está morto."""
        self.game.player.is_dead = True
        self.game.check_dead()
        
        self.mock_game_manager.change_state.assert_called_once_with("main_menu")

    def test_check_victory(self):
        """Testa a funcionalidade de vitória do jogador."""
        for enemy in self.game.enemies:
            enemy.is_dead = True

        platform_mock = MagicMock()
        platform_mock.tile_type = 'e'
        platform_mock.rect.colliderect.return_value = True
        self.game.platforms.append(platform_mock)

        with patch('builtins.print') as mocked_print:
            self.game.check_victory()

            mocked_print.assert_called_once_with("Parabéns! Voce venceu o jogo!")

    def test_check_collision(self):
        """Testa a funcionalidade de verificar colisões."""
        platform_mock = MagicMock()
        platform_mock.rect.colliderect.return_value = True

        self.game.platforms.append(platform_mock)

        self.game.check_collision()

        platform_mock.on_collision.assert_called_once_with(self.game.player)

    def tearDown(self):
        pg.quit()

if __name__ == "__main__":
    unittest.main()

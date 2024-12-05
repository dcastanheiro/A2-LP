import unittest
import pygame as pg
from player import Player
from entity import Entity
from unittest.mock import patch, Mock
from bullet import Bullet

class TestPlayer(unittest.TestCase):

    def setUp(self):
        pg.init()
        pg.display.set_mode((1, 1))
        images_folders = {
            'idle': 'assets/Player/idle_right',
            'run': 'assets/Player/run_right',
            'jump': 'assets/Player/jump_right',
            "die":  "assets/Player/die_right"
        }
        with patch("pygame.mixer.Sound", return_value=Mock()) as mock_sound:
            self.player = Player(100, 30, images_folders, x=100, y=200, vel=5)

    def test_initial_state(self):
        """Testa se os estados do jogador sao coerentes"""
        self.assertEqual(self.player.life, 100)
        self.assertEqual(self.player.ammo, 30)
        self.assertFalse(self.player.is_dead)

    def test_take_damage(self):
        """Testa se o jogador recebe dano"""
        self.player.life -= 50
        self.assertEqual(self.player.life, 50)
        self.player.life -= 60
        self.assertEqual(self.player.life, -10)  

    def test_die(self):
        """Testa se o jogador morre corretamente"""
        self.player.die()
        self.assertTrue(self.player.is_dead)
        self.assertEqual(self.player.state, "die")

    def test_shoot_bullets(self):
        """Testa se o jogador atira corretamente"""
        bullet_group = pg.sprite.Group()
        self.player.shoot_bullets(bullet_group, shoot_sound=pg.mixer.Sound("assets/sounds/laserShoot.wav"))
        self.assertTrue(Bullet)

if __name__ == '__main__':
    unittest.main()
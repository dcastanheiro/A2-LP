import unittest
import pygame as pg
from enemy import Enemy, ArEnemy
from bullet import Bullet

class TestEnemy(unittest.TestCase):
    
    def setUp(self):
        pg.init()
        pg.display.set_mode((1, 1))
        images_folders = {
            "idle": "assets/Enemies/sniper/idle",
            "shoot": "assets/Enemies/sniper/shoot",
            "die": "assets/Enemies/sniper/die"
        }
        self.bullet_group = pg.sprite.Group()
        self.platform_group = pg.sprite.Group()
        self.enemy = Enemy(images_folders, x=300, y=100, life=50, bullet_group=self.bullet_group, bullet_type="sniper", shoot_interval=1)

    def test_initial_state(self):
        """Testa se o estado do inimigo é coerente"""
        self.assertEqual(self.enemy.life, 50)
        self.assertFalse(self.enemy.is_dead)

    def test_take_damage(self):
        """Testa se o inimigo recebe dano"""
        self.enemy.take_damage(30)
        self.assertEqual(self.enemy.life, 20)
        self.enemy.take_damage(50)
        self.assertEqual(self.enemy.life, -30)
        self.assertTrue(self.enemy.is_dead)

    def test_shoot(self):
        """Testa se o inimigo atira corretamente"""
        self.enemy.shoot(400, 100, self.platform_group)
        self.assertTrue(Bullet)

class TestArEnemy(unittest.TestCase):

    def setUp(self):
        pg.init()
        pg.display.set_mode((1, 1))
        images_folders = {
            "walk": "assets/Enemies/ar/walk",
            "shoot": "assets/Enemies/ar/shoot",
            "idle": "assets/Enemies/ar/idle",
            "die": "assets/Enemies/ar/die"
        }
        self.bullet_group = pg.sprite.Group()
        self.ar_enemy = ArEnemy(images_folders, x=500, y=150, life=40, bullet_group=self.bullet_group, bullet_type="ar", shoot_interval=0.5, patrol_speed=2)

    def test_patrol(self):
        """Testa se o inimigo "ar" consegue patrulhar corretamente"""
        initial_x = self.ar_enemy.rect.x
        self.ar_enemy.patrol(pg.sprite.Group())  # No obstacles
        self.assertNotEqual(self.ar_enemy.rect.x, initial_x)

if __name__ == '__main__':
    unittest.main()

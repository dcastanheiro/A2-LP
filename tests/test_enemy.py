import unittest
import sys
import os
import pygame as pg  # Importando o Pygame corretamente
from unittest.mock import patch

# Adiciona o diretório 'src' ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from enemy import Enemy  # Agora a importação deve funcionar corretamente

class TestEnemy(unittest.TestCase):

    @patch('src.utils.load_image')  # Usando o patch corretamente com o caminho atualizado
    @patch('pygame.image.load')  # Simulando a função pygame.image.load
    @patch('os.listdir')  # Usando o patch para simular o retorno de os.listdir
    def test_enemy_init(self, mock_listdir, mock_pygame_load, mock_load_image):
        
        # Mock para o retorno da função os.listdir
        mock_listdir.return_value = ['image1.png', 'image2.png']  # Mock de imagens na pasta

        # Mock para a função load_image, retornando uma superfície do Pygame
        mock_pygame_load.return_value = pg.Surface((50, 50))  # Superfície de 50x50 pixels, simulando uma imagem

        # Criando a instância de Enemy com todos os parâmetros necessários
        enemy = Enemy(
            {'idle': 'path_to_idle_folder'},  # imagens
            100,  # posição x
            100,  # posição y
            life=3,  # quantidade de vida
            bullet_group=None,  # mock do grupo de balas
            bullet_type=None,  # mock do tipo de bala
            shoot_interval=1.0  # intervalo de tempo para atirar
        )

        # Verificando se o Enemy foi inicializado corretamente
        self.assertEqual(enemy.state, 'idle')  # O estado inicial deve ser 'idle'
        self.assertTrue(hasattr(enemy, 'image'))  # Verifica se existe o atributo 'image'
        self.assertTrue(hasattr(enemy, 'rect'))  # Verifica se existe o atributo 'rect'
        self.assertEqual(len(enemy.images['idle']), 2)  # Espera-se que haja 2 imagens no estado 'idle'

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, Mock
from utils import load_image, load_tile
from settings import PX_SCALE, TILE_SIZE
import pygame as pg


class TestUtils(unittest.TestCase):

    @patch("utils.pg.image.load", return_value=Mock())  
    @patch("utils.pg.transform.scale", return_value=Mock())  
    def test_load_tile(self, mock_scale, mock_load):
        """Testa a função load_tile."""
        img_path = "dummy_path/tile.png"

        # configura os métodos do Mock retornado por pg.image.load
        mock_image = mock_load.return_value
        mock_image.get_width.return_value = 100  # Largura simulada
        mock_image.get_height.return_value = 100  # Altura simulada (não é necessário, mas para consistência)

        # Chama a função
        result = load_tile(img_path)

        # verifica se pg.image.load foi chamado com o caminho correto
        mock_load.assert_called_with(img_path)

        # verifica se o resultado é o valor retornado por pg.transform.scale
        self.assertEqual(result, mock_scale.return_value)


if __name__ == "__main__":
    unittest.main()

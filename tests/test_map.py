import unittest
from unittest.mock import Mock, patch
from map import Platform, Background


class TestPlatform(unittest.TestCase):
    @patch("map.load_tile", return_value=Mock())  
    def test_create_platform(self, mock_load_tile):
        """Testa a criação de plataformas com base no layout do mapa."""
        map_layout = [
            "....",
            "..#.",
            ".#..",
        ]
        img_path = {"#": "path/to/tile_image.png"}

        platforms = Platform.create_platform(map_layout, img_path)

        # verifica número de plataformas criadas
        self.assertEqual(len(platforms), 2)

        # verifica se o tile_type está correto
        self.assertEqual(platforms[0].tile_type, "#")
        self.assertEqual(platforms[1].tile_type, "#")

        mock_load_tile.assert_called_with("path/to/tile_image.png")

    @patch("map.load_tile", return_value=Mock())
    def test_platform_collision(self, mock_load_tile):
        """Testa a colisão básica entre plataformas e outros objetos."""
        platform = Platform(0, 0, 64, 64, img_path="dummy_path")
        other_object = Mock()
        platform.on_collision(other_object)

        # verificando erros gerais do metodo
        self.assertTrue(True)

    @patch("map.load_tile", return_value=Mock())
    @patch("map.pg.Surface", return_value=Mock())
    def test_platform_draw(self, mock_surface, mock_load_tile):
        """Testa se a plataforma é desenhada corretamente."""
        platform = Platform(0, 0, 64, 64, img_path="dummy_path")
        screen_mock = Mock()

        platform.draw(screen_mock)

        # verificar se o método `blit` foi chamado corretamente
        screen_mock.blit.assert_called_with(platform.image, platform.rect)


class TestBackground(unittest.TestCase):
    @patch("map.pg.image.load", return_value=Mock())  
    @patch("map.pg.transform.scale", side_effect=lambda img, size: img)  
    def test_background_initialization(self, mock_scale, mock_load):
        """Testa a inicialização do background."""
        layers = ["layer1.png", "layer2.png"]
        screen_width = 800
        screen_height = 600

        background = Background(layers, screen_width, screen_height)

        # verificar se as camadas foram carregadas corretamente
        self.assertEqual(len(background.layers), 2)

        mock_load.assert_any_call("layer1.png")
        mock_load.assert_any_call("layer2.png")

    @patch("map.pg.Surface", return_value=Mock())
    def test_background_draw(self, mock_surface):
        """Testa se o background é desenhado corretamente"""
        layers = [Mock(), Mock()]
        background = Background(layers=[], screen_width=800, screen_height=600)
        background.layers = layers  # Inserir camadas mockadas

        screen_mock = Mock()
        background.draw(screen_mock)

        # verificaa se cada camada foi desenhada na tela
        for layer in layers:
            screen_mock.blit.assert_any_call(layer, (0, 0))


if __name__ == "__main__":
    unittest.main()

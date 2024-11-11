"""Modulo responsavel por implementar funcoes utilitarias do projeto"""

import pygame as pg
import os
from settings import PX_SCALE

def load_image(img_path: str):
    """
    Função para carregar e escalar uma imagem.

    Parameters
    ----------
    img_path: str
        String do caminho para o arquivo de imagem

    Returns
    -------
    scaled_image: Surface
        Imagem do 'path' nas proporcoes corretas
    
    """
    image = pg.image.load(img_path).convert_alpha()
    width, height = image.get_width(), image.get_height()
    scaled_image = pg.transform.scale(image, (int(width * PX_SCALE), int(height * PX_SCALE)))
    return scaled_image
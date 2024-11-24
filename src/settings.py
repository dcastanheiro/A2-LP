"""Modulo responsavel por inicializar as principais configuracoes do jogo"""

PX_SCALE = 1
TILE_SIZE = 20 * PX_SCALE
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# dicionario para sprites do jogador
player_all_images_folders = {
            "idle":             "assets/Player/idle_right",
            "jump":             "assets/Player/jump_right",
            "jump_down":        "assets/Player/jump_right_down",
            "jump_up":          "assets/Player/jump_right_up",
            "run":              "assets/Player/run_right",
            "crouch":            "assets/Player/shift_right",
            "shoot_jump":       "assets/Player/shoot_jump_right",
            "shoot_jump_down":  "assets/Player/shoot_jump_right_down",
            "shoot_jump_up":    "assets/Player/shoot_jump_right_up",
            "shoot":            "assets/Player/shoot_right",
            "shoot_up":         "assets/Player/shoot_right_up",
            "shoot_run":        "assets/Player/shoot_run_right",
            "shoot_run_up":     "assets/Player/shoot_run_right_up",
            "shoot_shift":      "assets/Player/shoot_shift_right",
            "die":              "assets/Player/die_right"

}

# mapa: Cada "#" representa um bloco, e "." é um espaço vazio
map_layout = [
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "..........................##................##..................",
    "..........................##................##..................",
    "..........................##................##..................",
    "###########............##############################........###",
    "..........####......####.........................#####.......###",
    "............##......##.............................#####......##",
    ".............########...........................................",
    "................................................................",
    "................................................................",
    "###...........######............................................",
    "................................................................",
    "....###########....#############################################",
    "................................................................",
    "................................................................",
    ".......###.......###.......###.......###.......###...........###",
    ".......###.......###.......###.......###.......###..............",
    ".......###.......###.......###.......###.......###..............",
    "#########################################################...####",
    "........................................................##.##...",
    "................................................................",
    "................................................................",
    "................................................................",
    "################################################################",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "###########################################################....#",
    "############################################################..##"
]

# lista com as camadas do background
background_layers=[
                "assets/Assets_area_2/backgrounds/nuvens_3.png",  
                "assets/Assets_area_2/backgrounds/nuvens_2.png",  
                "assets/Assets_area_2/backgrounds/nuvens_1.png",
                  
            ]
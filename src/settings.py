"""Modulo responsavel por inicializar as principais configuracoes do jogo"""

PX_SCALE = 1
TILE_SIZE = 20 * PX_SCALE
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60


# dicionario para sprites do jogador
player_all_images_folders = {
            "idle":             "../assets/Player/idle_right",
            "jump":             "../assets/Player/jump_right",
            "jump_down":        "../assets/Player/jump_right_down",
            "jump_up":          "../assets/Player/jump_right_up",
            "run":              "../assets/Player/run_right",
            "crouch":           "../assets/Player/shift_right",
            "shoot_jump":       "../assets/Player/shoot_jump_right",
            "shoot_jump_down":  "../assets/Player/shoot_jump_right_down",
            "shoot_jump_up":    "../assets/Player/shoot_jump_right_up",
            "shoot":            "../assets/Player/shoot_right",
            "shoot_up":         "../assets/Player/shoot_right_up",
            "shoot_run":        "../assets/Player/shoot_run_right",
            "shoot_run_up":     "../assets/Player/shoot_run_right_up",
            "shoot_shift":      "../assets/Player/shoot_shift_right",
            "die":              "../assets/Player/die_right"

}

bazooka_enemy_images_folders = {
    "idle": "../assets/Enemies/bazooka/idle",
    "shoot": "../assets/Enemies/bazooka/shoot",
    "die": "../assets/Enemies/bazooka/die"
}

sniper_enemy_images_folders = {
    "idle": "../assets/Enemies/sniper/idle",
    "shoot": "../assets/Enemies/sniper/shoot",
    "die": "../assets/Enemies/sniper/die"

}

ar_enemy_images_folders = {
    "walk": "../assets/Enemies/ar/walk",
    "shoot": "../assets/Enemies/ar/shoot",
    "idle": "../assets/Enemies/ar/idle",
    "die": "../assets/Enemies/ar/die"
    
}

# mapa: Cada "#" representa um bloco, e "." é um espaço vazio
map_layout = [
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "..........................42................42..................",
    "..........................11................11..................",
    "..........................11................11..................",
    "11111111112............411111111111111111111111111112........411",
    "..........312........415.........................31112.......311",
    "............32......45.............................31112......31",
    ".............31111115..........................................1",
    "........................###......######........................1",
    "...............................................................1",
    "##............######....................42.....................1",
    "..............b....b....................11.....................1",
    "....41111111112....411111111111111111111111111111111111111111111",
    "................................................................",
    "................................................................",
    "2.................1.........1................412..............41",
    "1.................1.........1........1.......111..............11",
    "111111111111111111111111111111111111111111111111111111112...4111",
    "........................................................32......",
    "................................................................",
    "...........###........1..........1..............................",
    "...........b.b........1..........1...........1..................",
    "2..4111111111111111111111111111111111111111111111111111111111111",
    "................................................................",
    "................................................................",
    "........................11.........................11...........",
    "................................................................",
    ".......11.........11....................11......................",
    ".......11.........11............1.................1............#",
    ".......11.........11...........11.................1.............",
    "11111111111111111111111111111111111111111111111111111111112....1",
    "111111111111111111111111111111111111111111111111111111111111ee11"
]

# lista com as camadas do background
background_layers = [
                "../assets/Assets_area_2/backgrounds/nuvens_3.png",  
                "../assets/Assets_area_2/backgrounds/nuvens_2.png",  
                "../assets/Assets_area_2/backgrounds/nuvens_1.png",
            ]

map_tiles = {
    "#": "../assets/Assets_area_2/tileset/platform_0.png",
    "1": "../assets/Assets_area_2/tileset/floor_2.png",
    "2": "../assets/Assets_area_2/tileset/floor_3.png",
    "3": "../assets/Assets_area_2/tileset/floor_4.png",
    "4": "../assets/Assets_area_2/tileset/floor_5.png",
    "5": "../assets/Assets_area_2/tileset/floor_6.png",
    "b": "../assets/Assets_area_2/tileset/barrier.png",
    "e": "../assets/Assets_area_2/tileset/exit.png"

}



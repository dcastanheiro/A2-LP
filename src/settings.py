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
    "..........................##................##..................",
    "..........................##................##..................",
    "..........................##................##..................",
    "11111111112............111111111111111111111111111112........###",
    "..........312........111.........................31112.......###",
    "............32......11.............................31112......##",
    ".............31111111...........................................",
    "........................#........######.........................",
    "................................................................",
    "##............######............................................",
    "..............b....b....................##......................",
    "....#111111111#....#11111111111111111111##1111111111111111111111",
    "................................................................",
    "................................................................",
    "..................#.........#................###..............##",
    "..................#.........#........#.......###..............##",
    "111111111111111111#111111111#11111111#111111####111111112...####",
    "........................................................32..#...",
    "................................................................",
    "...........###........#..........#..............................",
    "...........b.b........#..........#...........#..................",
    "2..1111111111111111111111111111111111111111111111111111111111111",
    "................................................................",
    "................................................................",
    "........................##.........................##...........",
    "................................................................",
    ".......##.........##....................##......................",
    ".......##.........##............#.................#............#",
    ".......##.........##...........##.................#.............",
    "1111111##111111111##11111111111##11111111111111111#11111112....#",
    "############################################################ee##"
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
    "b": "../assets/Assets_area_2/tileset/barrier.png",
    "e": "../assets/Assets_area_2/tileset/exit.png"
}



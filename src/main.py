import pygame # type: ignore
from player import Player # type: ignore

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(100, 7, "assets/player.png", 50, 20, pygame.Rect(400, 25, 20, 50), 400, 25)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.movement()
    player.player_rect()
    screen.fill(WHITE)  # Clear screen
    player.player_drawing(screen)
    pygame.display.flip()

pygame.quit()
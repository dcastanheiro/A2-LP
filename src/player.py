import pygame # type: ignore

class Player:
    def __init__(self, life, velocity, photo, height, width, rect, x, y_position):
        self.life = life
        self.velocity = velocity
        self.photo = photo
        self.height = height
        self.width = width
        self.rect = rect
        self.x_position = x
        self.y_position = y_position

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x < 800 - self.width:
            self.x += self.velocity

    def player_rect(self):
        self.rect = pygame.Rect(self.x, self.y_position, 20, 50)

    def player_drawing(self, screen):
        player_image = pygame.image.load(self.photo)
        screen.blit(player_image, (self.x, self.y_position))
import pygame


from code.consty import WIDTH, HEIGHT, PLAYER_SPEED


class Player:

    def __init__(self):

        self.image = pygame.image.load("assets/player.png")

        self.x = WIDTH // 2
        self.y = HEIGHT - 80

    def move(self, keys):

        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED

        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED

    def draw(self, screen):

        screen.blit(self.image,(self.x,self.y))
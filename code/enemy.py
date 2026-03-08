import pygame
import random


from code.consty import WIDTH, ENEMY_SPEED


class Enemy:

    def __init__(self):

        self.image = pygame.image.load("assets/enemy.png")

        self.x = random.randint(0, WIDTH-40)
        self.y = -50

    def update(self):

        self.y += ENEMY_SPEED

    def draw(self, screen):

        screen.blit(self.image,(self.x,self.y))
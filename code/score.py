import pygame

from code.consty import C_WHITE


class Score:

    def __init__(self):

        self.score = 0
        self.font = pygame.font.SysFont("arial",30)

    def add(self):

        self.score += 10

    def draw(self,screen):

        text = self.font.render(f"Score: {self.score}",True,C_WHITE)
        screen.blit(text,(10,10))
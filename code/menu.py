import pygame

from code.consty import C_WHITE, C_BLACK


class Menu:

    def __init__(self,screen):

        self.screen = screen
        self.font_big = pygame.font.SysFont("arial",50)
        self.font_small = pygame.font.SysFont("arial",25)

    def draw(self):

        self.screen.fill(C_BLACK)

        title = self.font_big.render("SUMMIT STRIKE",True,C_WHITE)

        start = self.font_small.render("ENTER - Start Game",True,C_WHITE)

        controls1 = self.font_small.render("A / D - Move",True,C_WHITE)
        controls2 = self.font_small.render("SPACE - Shoot",True,C_WHITE)
        controls3 = self.font_small.render("ESC - Exit",True,C_WHITE)

        self.screen.blit(title,(230,150))
        self.screen.blit(start,(300,250))

        self.screen.blit(controls1,(320,350))
        self.screen.blit(controls2,(320,380))
        self.screen.blit(controls3,(320,410))
import pygame


from code.consty import BULLET_SPEED, C_WHITE


class Bullet:

    def __init__(self,x,y):

        self.x = x
        self.y = y

    def update(self):

        self.y -= BULLET_SPEED

    def draw(self,screen):

        pygame.draw.rect(screen,C_WHITE,(self.x,self.y,5,10))
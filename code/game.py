import pygame

from code.consty import C_WHITE, C_BLACK, HEIGHT, FPS, WIDTH, C_RED
from code.menu import Menu
from code.player import Player
from code.enemy import Enemy
from code.bullet import Bullet
from code.score import Score

class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Summit Strike")

        self.clock = pygame.time.Clock()

        self.menu = Menu(self.screen)

        self.player = Player()
        self.enemies = []
        self.bullets = []

        self.score = Score()

        self.spawn_timer = 0

        self.state = "menu"

    def reset(self):

        self.player = Player()
        self.enemies = []
        self.bullets = []
        self.score.score = 0

    def run(self):

        running = True

        while running:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if self.state == "menu":

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            self.state = "play"

                elif self.state == "play":

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_SPACE:
                            self.bullets.append(
                                Bullet(self.player.x+20,self.player.y)
                            )

                elif self.state == "gameover":

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            self.reset()
                            self.state = "play"

            if self.state == "menu":
                self.menu.draw()

            elif self.state == "play":
                self.update_game()

            elif self.state == "gameover":
                self.draw_gameover()

            pygame.display.update()

        pygame.quit()

    def update_game(self):

        self.screen.fill(C_BLACK)

        self.spawn_timer += 1

        if self.spawn_timer > 60:
            self.enemies.append(Enemy())
            self.spawn_timer = 0

        keys = pygame.key.get_pressed()

        self.player.move(keys)

        for bullet in self.bullets:
            bullet.update()

        for enemy in self.enemies:
            enemy.update()

            if enemy.y > HEIGHT:
                self.state = "gameover"

        for enemy in self.enemies[:]:
            for bullet in self.bullets[:]:

                if bullet.x > enemy.x and bullet.x < enemy.x+40 and bullet.y > enemy.y and bullet.y < enemy.y+40:

                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)

                    self.score.add()

        self.player.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        self.score.draw(self.screen)

    def draw_gameover(self):

        self.screen.fill(C_BLACK)

        font = pygame.font.SysFont("arial",50)
        font2 = pygame.font.SysFont("arial",25)

        text = font.render("GAME OVER",True,C_RED)

        restart = font2.render("ENTER - Restart",True,C_WHITE)

        score_text = font2.render(f"Score: {self.score.score}",True,C_WHITE)

        self.screen.blit(text,(270,200))
        self.screen.blit(score_text,(340,300))
        self.screen.blit(restart,(320,350))
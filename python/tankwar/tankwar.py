import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("坦克大战")
    bg_color = (0,0,0)
    tank = Tank(screen)
    bullets = Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    tank.moving_right = True
                elif event.key == pygame.K_LEFT:
                    tank.moving_left = True
                elif event.key == pygame.K_UP:
                    tank.moving_up = True
                elif event.key == pygame.K_DOWN:
                    tank.moving_down = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen,tank)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    tank.moving_right = False
                elif event.key == pygame.K_LEFT:
                    tank.moving_left = False
                elif event.key == pygame.K_UP:
                    tank.moving_up = False
                elif event.key == pygame.K_DOWN:
                    tank.moving_down = False
        tank.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        screen.fill(bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullets()
        tank.blitme()
        pygame.display.flip()
class Tank():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("E:/File/python/tankwar/images/tank.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = 200
        self.rect.bottom = self.screen_rect.bottom
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
class Bullet(Sprite):
    def __init__(self,screen,tank):
        super(Bullet,self).__init__()
        self.screen = screen
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,0,0)
        self.bullet_speed_factor = 1.5
        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.rect.centerx = tank.rect.centerx
        self.rect.centery = tank.rect.top
        self.y = float(self.rect.y)
    def update(self):
        self.y -= self.bullet_speed_factor
        self.rect.y = self.y
    def draw_bullets(self):
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)
run_game()
import pygame as pg


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.image = pg.image.load("assets/enemies/enemy_1_r_m.png").convert_alpha()
        self.shadow = pg.image.load("assets/shadows/enemy_1_shadow_m.png").convert_alpha()

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.shadow, (self.x + 6, self.y + 6))
        screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y > 800

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

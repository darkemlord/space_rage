import pygame as pg


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pg.image.load("assets/effects/vulcan_1.png").convert_alpha()

    def update(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y < 0

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

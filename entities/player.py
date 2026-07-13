import pygame as pg


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.images = {
            "straight": pg.image.load("assets/player/player_b_m.png").convert_alpha(),
            "left": pg.image.load("assets/player/player_b_l1.png").convert_alpha(),
            "right": pg.image.load("assets/player/player_b_r2.png").convert_alpha()
        }
        self.shadows_images = {
            "straight": pg.image.load("assets/shadows/player_shadow_m.png").convert_alpha(),
            "left": pg.image.load("assets/shadows/player_shadow_l1.png").convert_alpha(),
            "right": pg.image.load("assets/shadows/player_shadow_r2.png").convert_alpha()
        }
        self.shadow = self.shadows_images["straight"]

    def handle_input(self, keys):
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.x += self.speed
        if keys[pg.K_UP]:
            self.y -= self.speed
        if keys[pg.K_DOWN]:
            self.y += self.speed
        if keys[pg.K_LEFT]:
            self.image = self.images["left"]
            self.shadow = self.shadows_images["left"]
        elif keys[pg.K_RIGHT]:
            self.image = self.images["right"]
            self.shadow = self.shadows_images["right"]
        else:
            self.image = self.images["straight"]
            self.shadow = self.shadows_images["straight"]

        # limit player movement to the screen boundaries
        self.x = max(0, min(self.x, 700 - 64))
        self.y = max(0, min(self.y, 800 - 64))

    def draw(self, screen):
        screen.blit(self.shadow, (self.x + 6, self.y + 6))
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

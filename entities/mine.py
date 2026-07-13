import pygame as pg


class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.frames = []
        for i in range(1, 10):
            filename = f"assets/mines/mine_1_{i:02d}.png"
            self.frames.append(pg.image.load(filename).convert_alpha())
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 5
        self.image = self.frames[self.frame_index]
        self.shadow = pg.image.load("assets/shadows/mine_1_shadow_01.png").convert_alpha()

    def update(self):
        self.y += self.speed
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            self.image = self.frames[self.frame_index]

    def draw(self, screen):
        screen.blit(self.shadow, (self.x + 6, self.y + 6))
        screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y > 800

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

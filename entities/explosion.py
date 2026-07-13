import pygame as pg


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frames = []
        for i in range(1, 12):
            filename = f"assets/explosions/explosion_1_{i:02d}.png"
            self.frames.append(pg.image.load(filename).convert_alpha())
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 3
        self.image = self.frames[self.frame_index]

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.frame_index += 1
            if self.frame_index < len(self.frames):
                self.image = self.frames[self.frame_index]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_finished(self):
        return self.frame_index >= len(self.frames)

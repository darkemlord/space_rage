import pygame as pg
import random


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.images = {
            "left2": pg.image.load("assets/enemies/enemy_1_r_l2.png").convert_alpha(),
            "left1": pg.image.load("assets/enemies/enemy_1_r_l1.png").convert_alpha(),
            "straight": pg.image.load("assets/enemies/enemy_1_r_m.png").convert_alpha(),
            "right1": pg.image.load("assets/enemies/enemy_1_r_r1.png").convert_alpha(),
            "right2": pg.image.load("assets/enemies/enemy_1_r_r2.png").convert_alpha()
        }
        self.shadows_images = {
            "left2": pg.image.load("assets/shadows/enemy_1_shadow_l2.png").convert_alpha(),
            "left1": pg.image.load("assets/shadows/enemy_1_shadow_l1.png").convert_alpha(),
            "straight": pg.image.load("assets/shadows/enemy_1_shadow_m.png").convert_alpha(),
            "right1": pg.image.load("assets/shadows/enemy_1_shadow_r1.png").convert_alpha(),
            "right2": pg.image.load("assets/shadows/enemy_1_shadow_r2.png").convert_alpha()
        }
        self.vx = 0
        self.is_chaser = random.random() < 0.5 # 50% chance to be a chaser 
        self.chase_timer = 0
        self.chase_delay = 30 # frames to wait before changing direction when chasing
        self.vx_to_frame = {
            -2: "left2",
            -1: "left1",
             0: "straight",
             1: "right1",
             2: "right2"
        }
        frame_key = self.vx_to_frame[self.vx]
        self.image = self.images[frame_key]
        self.shadow = self.shadows_images[frame_key]


    def update(self, player_x):
        self.y += self.speed

        if self.is_chaser:
            self.chase_timer += 1
            if self.chase_timer >= self.chase_delay:
                self.chase_timer = 0
                diff = player_x - self.x
                if diff < -40:
                    self.vx = -2
                elif diff < -5:
                    self.vx = -1
                elif diff > 40:
                    self.vx = 2
                elif diff > 5:
                    self.vx = 1
                else:
                    self.vx = 0

        self.x += self.vx
        self.x = max(0, min(self.x, 700 - 64))

        frame_key = self.vx_to_frame[self.vx]
        self.image = self.images[frame_key]
        self.shadow = self.shadows_images[frame_key]



    def draw(self, screen):
        screen.blit(self.shadow, (self.x + 6, self.y + 6))
        screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y > 800

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

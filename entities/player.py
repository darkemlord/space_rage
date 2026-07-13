import pygame as pg


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.images = {
            "straight": pg.image.load("assets/player/player_b_m.png").convert_alpha(),
            "left1": pg.image.load("assets/player/player_b_l1.png").convert_alpha(),
            "left2": pg.image.load("assets/player/player_b_l2.png").convert_alpha(),
            "right1": pg.image.load("assets/player/player_b_r1.png").convert_alpha(),
            "right2": pg.image.load("assets/player/player_b_r2.png").convert_alpha()
        }
        self.shadows_images = {
            "straight": pg.image.load("assets/shadows/player_shadow_m.png").convert_alpha(),
            "left1": pg.image.load("assets/shadows/player_shadow_l1.png").convert_alpha(),
            "left2": pg.image.load("assets/shadows/player_shadow_l2.png").convert_alpha(),
            "right1": pg.image.load("assets/shadows/player_shadow_r1.png").convert_alpha(),
            "right2": pg.image.load("assets/shadows/player_shadow_r2.png").convert_alpha()
        }
        self.shadow = self.shadows_images["straight"]
        self.bank_frames = ["left2", "left1", "straight", "right1", "right2"]
        self.bank_index = 2 # Start with the straight image
        self.bank_timer = 0
        self.bank_delay = 4 # each 4 frames of loop, change the image to the next one in the bank_frames 

    def handle_input(self, keys):
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.x += self.speed
        if keys[pg.K_UP]:
            self.y -= self.speed
        if keys[pg.K_DOWN]:
            self.y += self.speed
        self.bank_timer += 1
        if self.bank_timer >= self.bank_delay:
            self.bank_timer = 0
            if keys[pg.K_LEFT] and self.bank_index > 0:
                self.bank_index -= 1
            elif keys[pg.K_RIGHT] and self.bank_index < 4:
                self.bank_index += 1
            elif not keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and self.bank_index != 2:
                if self.bank_index < 2:
                    self.bank_index += 1
                else:
                    self.bank_index -= 1

        current_frame = self.bank_frames[self.bank_index]
        self.image = self.images[current_frame]
        self.shadow = self.shadows_images[current_frame]

        # limit player movement to the screen boundaries
        self.x = max(0, min(self.x, 700 - 64))
        self.y = max(0, min(self.y, 800 - 64))

    def draw(self, screen):
        screen.blit(self.shadow, (self.x + 6, self.y + 6))
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

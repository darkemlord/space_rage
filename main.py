import pygame as pg
import random

from entities.player import Player
from entities.bullet import Bullet
from entities.enemy import Enemy
from entities.mine import Mine
from entities.explosion import Explosion

pg.init()

screen = pg.display.set_mode((700, 800))
pg.display.set_caption("My Game")

clock = pg.time.Clock()
running = True

# background_image
bg = pg.image.load("assets/backgrounds/BG.png").convert()

# player_image
player = Player(700 // 2 - 32, 800 - 100)
bullets = []
enemies = []
spawn_timer = 0
spawn_interval = 60
explosions = []
mines = []
mine_spawn_timer = 0
mine_spawn_interval = 180

# fonts and text
font = pg.font.SysFont(None, 36)
score = 0
lives = 3
game_over = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bullets.append(Bullet(player.x + 29, player.y - 10))  # Adjust bullet position to be centered on the player
    # Handle player movement
    keys = pg.key.get_pressed()
    if not game_over:
        player.handle_input(keys)

    screen.blit(bg, (0, 0))  # Draw the background image
    player.draw(screen)  # Draw the player image

    # Update and draw bullets
    for bullet in bullets:
        bullet.update()
    bullets_to_keep = []
    for bullet in bullets:
        if not bullet.is_off_screen():
            bullets_to_keep.append(bullet)
            bullet.draw(screen)  # Draw the bullet image
    bullets = bullets_to_keep

    # Update and draw enemies
    if not game_over:
        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            enemies.append(Enemy(random.randint(0, 700 - 64), -64))  # Spawn enemy at random x position
        for enemy in enemies:
            enemy.update(player.x)  # Pass player's x position for chasing behavior
        enemies_to_keep = []
        for enemy in enemies:
            if not enemy.is_off_screen():
                enemies_to_keep.append(enemy)
                enemy.draw(screen)  # Draw the enemy image
        enemies = enemies_to_keep

    # Update and draw mines
    if not game_over:
        mine_spawn_timer += 1
        if mine_spawn_timer >= mine_spawn_interval:
            mine_spawn_timer = 0
            mines.append(Mine(random.randint(0, 700 - 48), -48))  # Spawn mine at random x position
        for mine in mines:
            mine.update()
        mines_to_keep = []
        for mine in mines:
            if not mine.is_off_screen():
                mines_to_keep.append(mine)
                mine.draw(screen)  # Draw the mine image
        mines = mines_to_keep

    # enemies and bullets collision detection
    enemies_alive = []
    bullets_remaining = bullets[:]

    for enemy in enemies:
        enemy_rect = enemy.get_rect()
        hit = False
        for bullet in bullets_remaining:
            if enemy_rect.colliderect(bullet.get_rect()):
                hit = True
                bullets_remaining.remove(bullet)  # Remove the bullet that hit the enemy
                explosions.append(Explosion(enemy.x, enemy.y))  # Create an explosion at the enemy's position
                score += 10  # Increase score when an enemy is hit
                break
        if not hit:
            enemies_alive.append(enemy)  # Keep the enemy if it wasn't hit
    enemies = enemies_alive
    bullets = bullets_remaining  # Update the bullets list to only include remaining bullets

    # player and enemies collision detection
    if not game_over:
        player_rect = player.get_rect()

        enemies_survived = []
        for enemy in enemies:
            if player_rect.colliderect(enemy.get_rect()):
                lives -= 1  # Decrease lives when player collides with an enemy
                explosions.append(Explosion(enemy.x, enemy.y))  # Create an explosion at the enemy
            else:
                enemies_survived.append(enemy)  # Keep the enemy if it didn't collide with the player
        enemies = enemies_survived

        mines_survived = []
        for mine in mines:
            if player_rect.colliderect(mine.get_rect()):
                lives -= 1  # Decrease lives when player collides with a mine
                explosions.append(Explosion(mine.x, mine.y))  # Create an explosion at the mine
            else:
                mines_survived.append(mine)  # Keep the mine if it didn't collide with the player
        mines = mines_survived

        if lives <= 0:
            game_over = True  # Set game over state when lives reach zero

    # Update and draw explosions
    for explosion in explosions:
        explosion.update()
    explosions_to_keep = []
    for explosion in explosions:
        if not explosion.is_finished():
            explosions_to_keep.append(explosion)
            explosion.draw(screen)  # Draw the explosion image
    explosions = explosions_to_keep

    # Draw score and lives
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 40))

    if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        text_x = 700 // 2 - over_text.get_width() // 2
        text_y = 800 // 2 - over_text.get_height() // 2
        screen.blit(over_text, (text_x, text_y))

    pg.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

# hi rosty
import pygame, sys
import random

# initialize pygame
pygame.init()

# set up some constants
WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
PLAYER_SPEED = 20
BULLET_SIZE = 20
BULLET_SPEED = 10
BULLET_COLOR = (255, 0, 0)

# set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set up the player and bullet lists
player = pygame.Rect(WIDTH / 2, HEIGHT - PLAYER_SIZE * 2, PLAYER_SIZE, PLAYER_SIZE)
bullets = []
# game loop
bullets = []
enemies = []
last_bullet_shot = pygame.time.get_ticks()
bullets_per_second = 1
while True:
    # cap the frame rate
    pygame.time.delay(30)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # move the player left and right
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    # move the bullets
    for b in bullets:
        b.y -= BULLET_SPEED
        if b.y < 0:
            bullets.remove(b)

    # create a new bullet
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_time - last_bullet_shot > 60 / bullets_per_second:
        bullet_x = player.x + PLAYER_SIZE / 2 - BULLET_SIZE / 2
        bullet_y = player.y + PLAYER_SIZE / 2 - BULLET_SIZE / 2
        bullets.append(pygame.Rect(bullet_x, bullet_y, BULLET_SIZE, BULLET_SIZE))
        last_bullet_shot = current_time

    # add new enemies
    if random.random() < 0.05:
        enemy_x = random.randint(0, WIDTH - PLAYER_SIZE)
        enemy_y = 0
        enemies.append(pygame.Rect(enemy_x, enemy_y, PLAYER_SIZE, PLAYER_SIZE))

    # move the enemies
    for e in enemies:
        e.y += PLAYER_SPEED
        if e.y > HEIGHT:
            enemies.remove(e)

    # fill the screen with black
    screen.fill((0, 0, 0))

    # draw the player
    pygame.draw.rect(screen, (255, 255, 255), player)

    # draw the bullets as blue circles
    for b in bullets:
        pygame.draw.ellipse(screen, (0, 0, 255), b)

    # draw the enemies as red rectangles
    for e in enemies:
        pygame.draw.rect(screen, BULLET_COLOR, e)

    # update the display
    pygame.display.flip()
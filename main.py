import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Side-Scrolling Platformer")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# World settings
WORLD_WIDTH = 6000
GRAVITY = 0.8
JUMP_FORCE = -15

# Player
player = pygame.Rect(100, 500, 50, 60)
player_vel_x = 0
player_vel_y = 0
player_speed = 5
on_ground = False

# Platforms
platforms = [
    pygame.Rect(0, SCREEN_HEIGHT - 40, WORLD_WIDTH, 40),
    pygame.Rect(300, 450, 200, 20),
    pygame.Rect(600, 350, 200, 20),
    pygame.Rect(950, 300, 150, 20),
    pygame.Rect(1300, 400, 300, 20),
    pygame.Rect(1700, 300, 300, 20),
    pygame.Rect(2200, 350, 350, 20),
    pygame.Rect(2700, 300, 150, 20),
    pygame.Rect(3000, 350, 200, 20),
    pygame.Rect(3300, 300, 250, 20),
    pygame.Rect(3650, 200, 250, 20),
    pygame.Rect(4000, 300, 300, 20),
    pygame.Rect(4400, 250, 100, 20),
    pygame.Rect(4700, 350, 200, 20),
    pygame.Rect(5000, 300, 250, 20),
    pygame.Rect(5300, 400, 150, 20),
    pygame.Rect(5600, 350, 200, 20),
    pygame.Rect(5900, 300, 50, 20)
]

# Enemies
enemies = [
    {"rect": pygame.Rect(1, 520, 40, 40), "dir": 1, "range": (1, 300)},
    {"rect": pygame.Rect(300, 410, 40, 40), "dir": -1, "range": (300, 500)},
    {"rect": pygame.Rect(950, 260, 40, 40), "dir": 1, "range": (950, 1100)},
    {"rect": pygame.Rect(1700, 260, 40, 40), "dir": -1, "range": (1700, 2000)},
    {"rect": pygame.Rect(2200, 310, 40, 40), "dir": 1, "range": (2200, 2550)},
    {"rect": pygame.Rect(2700, 260, 40, 40), "dir": -1, "range": (2700, 2850)},
    {"rect": pygame.Rect(3300, 260, 40, 40), "dir": 1, "range": (3300, 3550)},
    {"rect": pygame.Rect(4000, 260, 40, 40), "dir": -1, "range": (4000, 4300)},
    {"rect": pygame.Rect(4400, 210, 40, 40), "dir": 1, "range": (4400, 4500)},
    {"rect": pygame.Rect(5000, 260, 40, 40), "dir": -1, "range": (5000, 5250)},
    {"rect": pygame.Rect(5300, 360, 40, 40), "dir": 1, "range": (5300, 5450)},
    {"rect": pygame.Rect(5600, 310, 40, 40), "dir": -1, "range": (5600, 5750)},
]

# Camera offset
scroll_x = 0

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Input
    keys = pygame.key.get_pressed()
    player_vel_x = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_vel_x = -player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_vel_x = player_speed

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and on_ground:
                player_vel_y = JUMP_FORCE
                on_ground = False

    # Apply gravity
    player_vel_y += GRAVITY

    # Move player
    player.x += player_vel_x
    player.y += player_vel_y

    # Horizontal camera scroll logic
    if player.centerx - scroll_x > SCREEN_WIDTH // 2:
        scroll_x = player.centerx - SCREEN_WIDTH // 2
    if player.centerx - scroll_x < 200:
        scroll_x = player.centerx - 200
    scroll_x = max(0, min(scroll_x, WORLD_WIDTH - SCREEN_WIDTH))

    # Collision detection with platforms
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if player_vel_y > 0 and player.bottom <= platform.bottom:
                player.bottom = platform.top
                player_vel_y = 0
                on_ground = True

    # Enemy movement
    for enemy in enemies:
        enemy["rect"].x += enemy["dir"] * 2
        if enemy["rect"].x < enemy["range"][0] or enemy["rect"].x > enemy["range"][1]:
            enemy["dir"] *= -1

    # Check player collision with enemies
    for enemy in enemies:
        if player.colliderect(enemy["rect"]):
            player.x, player.y = 100, 500
            player_vel_y = 0
            scroll_x = 0

    # Draw platforms
    for platform in platforms:
        draw_rect = platform.copy()
        draw_rect.x -= scroll_x
        pygame.draw.rect(screen, GREEN, draw_rect)

    # Draw enemies
    for enemy in enemies:
        draw_enemy = enemy["rect"].copy()
        draw_enemy.x -= scroll_x
        pygame.draw.rect(screen, RED, draw_enemy)

    # Draw player
    player_draw = player.copy()
    player_draw.x -= scroll_x
    pygame.draw.rect(screen, BLUE, player_draw)

    pygame.display.flip()

pygame.quit()
sys.exit()

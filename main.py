import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Side-Scrolling Platformer")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)

# World settings
WORLD_WIDTH = 3100  # total level width
GRAVITY = 0.8
JUMP_FORCE = -15

# Player
player = pygame.Rect(100, 500, 50, 60)
player_vel_x = 0
player_vel_y = 0
player_speed = 5
on_ground = False

# Platforms (can add more)
platforms = [
    pygame.Rect(0, SCREEN_HEIGHT - 40, WORLD_WIDTH, 40),  # Ground
    pygame.Rect(300, 450, 200, 20),
    pygame.Rect(600, 350, 200, 20),
    pygame.Rect(950, 300, 150, 20),
    pygame.Rect(1300, 400, 300, 20),
    pygame.Rect(1700, 300, 300, 20),
    pygame.Rect(2200, 350, 350, 20),
    pygame.Rect(2700, 300, 150, 20),
    pygame.Rect(3000, 350, 200, 20)
]

# Camera offset
scroll_x = 0

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    player_vel_x = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_vel_x = -player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_vel_x = player_speed
    if keys[pygame.K_SPACE] and on_ground:
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

    # Clamp scroll to world bounds
    scroll_x = max(0, min(scroll_x, WORLD_WIDTH - SCREEN_WIDTH))

    # Collision detection
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if player_vel_y > 0 and player.bottom <= platform.bottom:
                player.bottom = platform.top
                player_vel_y = 0
                on_ground = True

    # Draw platforms (apply scroll)
    for platform in platforms:
        draw_rect = platform.copy()
        draw_rect.x -= scroll_x
        pygame.draw.rect(screen, GREEN, draw_rect)

    # Draw player
    player_draw = player.copy()
    player_draw.x -= scroll_x
    pygame.draw.rect(screen, BLUE, player_draw)

    pygame.display.flip()

pygame.quit()
sys.exit()

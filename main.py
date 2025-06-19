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
GOLD = (255, 215, 0)
MAGENTA = (250, 50, 250)

# Sounds
level_complete_sound = pygame.mixer.Sound("level-win-6416.mp3")
player_dead = pygame.mixer.Sound("086398_game-die-81356.mp3")
background_music = pygame.mixer.Sound("suspence-background-25609.mp3")
background_music.play(-1)

# World settings
WORLD_WIDTH = 6000
GRAVITY = 0.8
JUMP_FORCE = -15

# Level data
levels = [
    {
        "platforms": [
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
        ],
        "enemies": [
            {"rect": pygame.Rect(1, 520, 40, 40), "dir": 1, "range": (1, 300)},
            {"rect": pygame.Rect(300, 410, 40, 40), "dir": -1, "range": (300, 460)},
            {"rect": pygame.Rect(950, 260, 40, 40), "dir": 1, "range": (950, 1060)},
            {"rect": pygame.Rect(1700, 260, 40, 40), "dir": -1, "range": (1700, 1960)},
            {"rect": pygame.Rect(2200, 310, 40, 40), "dir": 1, "range": (2200, 2500)},
            {"rect": pygame.Rect(2700, 260, 40, 40), "dir": -1, "range": (2700, 2810)},
            {"rect": pygame.Rect(3300, 260, 40, 40), "dir": 1, "range": (3300, 3510)},
            {"rect": pygame.Rect(4000, 260, 40, 40), "dir": -1, "range": (4000, 4260)},
            {"rect": pygame.Rect(4700, 310, 40, 40), "dir": -1, "range": (4700, 4860)},
            {"rect": pygame.Rect(5000, 260, 40, 40), "dir": -1, "range": (5000, 5210)},
            {"rect": pygame.Rect(5300, 360, 40, 40), "dir": 1, "range": (5300, 5410)},
            {"rect": pygame.Rect(5600, 310, 40, 40), "dir": -1, "range": (5600, 5750)}
        ],
        "goal": pygame.Rect(WORLD_WIDTH - 100, 200, 50, 100)
    },
    {
        "platforms": [
            pygame.Rect(0, SCREEN_HEIGHT - 40, WORLD_WIDTH, 40),
            pygame.Rect(200, 450, 150, 20),
            pygame.Rect(500, 400, 200, 20),
            pygame.Rect(800, 350, 250, 20),
            pygame.Rect(1200, 300, 200, 20),
            pygame.Rect(1500, 250, 300, 20),
            pygame.Rect(2000, 350, 250, 20),
            pygame.Rect(2300, 300, 200, 20),
            pygame.Rect(2600, 400, 200, 20),
            pygame.Rect(2900, 350, 300, 20),
            pygame.Rect(3300, 300, 150, 20),
            pygame.Rect(3600, 250, 200, 20),
            pygame.Rect(3900, 300, 200, 20),
            pygame.Rect(4200, 350, 200, 20),
            pygame.Rect(4500, 300, 250, 20),
            pygame.Rect(4900, 250, 200, 20),
            pygame.Rect(5200, 350, 250, 20),
            pygame.Rect(5500, 300, 200, 20)
        ],
        "enemies": [
            {"rect": pygame.Rect(200, 410, 40, 40), "dir": 1, "range": (200, 310)},
            {"rect": pygame.Rect(800, 310, 40, 40), "dir": -1, "range": (800, 1010)},
            {"rect": pygame.Rect(1500, 210, 40, 40), "dir": 1, "range": (1500, 1760)},
            {"rect": pygame.Rect(2300, 260, 40, 40), "dir": -1, "range": (2300, 2460)},
            {"rect": pygame.Rect(2600, 360, 40, 40), "dir": -1, "range": (2600, 2760)},
            {"rect": pygame.Rect(3300, 260, 40, 40), "dir": 1, "range": (3300, 3410)},
            {"rect": pygame.Rect(4500, 260, 40, 40), "dir": -1, "range": (4500, 4710)},
            {"rect": pygame.Rect(5200, 310, 40, 40), "dir": 1, "range": (5200, 5410)},
        ],
        "goal": pygame.Rect(WORLD_WIDTH - 100, 180, 50, 100)
    },
    {
    "platforms": [
    pygame.Rect(0, SCREEN_HEIGHT - 40, WORLD_WIDTH, 40),
    pygame.Rect(300, 450, 350, 20),
    pygame.Rect(550, 350, 150, 20),
    pygame.Rect(800, 300, 200, 20),
    pygame.Rect(1100, 350, 100, 20),
    pygame.Rect(1400, 350, 300, 20),
    pygame.Rect(1800, 300, 250, 20),
    pygame.Rect(2200, 300, 200, 20),
    pygame.Rect(2600, 350, 200, 20),
    pygame.Rect(2900, 350, 200, 20),
    pygame.Rect(3300, 350, 100, 20),
    pygame.Rect(3600, 300, 250, 20),
    pygame.Rect(3900, 400, 150, 20),
    pygame.Rect(4200, 350, 250, 20),
    pygame.Rect(4500, 400, 300, 20),
    pygame.Rect(4900, 350, 200, 20),
    pygame.Rect(5200, 300, 250, 20),
    pygame.Rect(5500, 250, 150, 20)
],
"enemies": [
    {"rect": pygame.Rect(300, 410, 40, 40), "dir": 1, "range": (300, 610)},
    {"rect": pygame.Rect(800, 260, 40, 40), "dir": -1, "range": (800, 960)},
    {"rect": pygame.Rect(1400, 310, 40, 40), "dir": 1, "range": (1400, 1660)},
    {"rect": pygame.Rect(2200, 260, 40, 40), "dir": -1, "range": (2200, 2360)},
    {"rect": pygame.Rect(2900, 310, 40, 40), "dir": -1, "range": (2900, 3060)},
    {"rect": pygame.Rect(3300, 310, 40, 40), "dir": 1, "range": (3300, 3360)},
    {"rect": pygame.Rect(4500, 360, 40, 40), "dir": -1, "range": (4500, 4760)},
    {"rect": pygame.Rect(5200, 260, 40, 40), "dir": 1, "range": (5200, 5410)},
],
"goal": pygame.Rect(WORLD_WIDTH - 100, 180, 50, 100)
}
]

current_level_index = 0

def load_level(index):
    level = levels[index]
    return level["platforms"].copy(), [enemy.copy() for enemy in level["enemies"]], level["goal"].copy()

# Game state
player = pygame.Rect(100, 500, 50, 60)
player_vel_x = 0
player_vel_y = 0
player_speed = 5
on_ground = False
scroll_x = 0
level_complete = False

platforms, enemies, goal = load_level(current_level_index)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(MAGENTA)

    keys = pygame.key.get_pressed()
    player_vel_x = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_vel_x = -player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_vel_x = player_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and on_ground:
                player_vel_y = JUMP_FORCE
                on_ground = False

    player_vel_y += GRAVITY
    player.x += player_vel_x
    player.y += player_vel_y

    if player.centerx - scroll_x > SCREEN_WIDTH // 2:
        scroll_x = player.centerx - SCREEN_WIDTH // 2
    if player.centerx - scroll_x < 200:
        scroll_x = player.centerx - 200
    scroll_x = max(0, min(scroll_x, WORLD_WIDTH - SCREEN_WIDTH))

    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if player_vel_y > 0 and player.bottom <= platform.bottom:
                player.bottom = platform.top
                player_vel_y = 0
                on_ground = True

    for enemy in enemies:
        enemy["rect"].x += enemy["dir"] * 2
        if enemy["rect"].x < enemy["range"][0] or enemy["rect"].x > enemy["range"][1]:
            enemy["dir"] *= -1

    for enemy in enemies:
        if player.colliderect(enemy["rect"]):
            player.x, player.y = 100, 500
            player_vel_y = 0
            scroll_x = 0
            player_dead.play()

    if player.colliderect(goal):
        level_complete = True

    for platform in platforms:
        draw_rect = platform.copy()
        draw_rect.x -= scroll_x
        pygame.draw.rect(screen, GREEN, draw_rect)

    for enemy in enemies:
        draw_enemy = enemy["rect"].copy()
        draw_enemy.x -= scroll_x
        pygame.draw.rect(screen, RED, draw_enemy)

    goal_draw = goal.copy()
    goal_draw.x -= scroll_x
    pygame.draw.rect(screen, GOLD, goal_draw)

    player_draw = player.copy()
    player_draw.x -= scroll_x
    pygame.draw.rect(screen, BLUE, player_draw)

    if level_complete:
        level_complete_sound.play()
        current_level_index += 1
        if current_level_index >= len(levels):
            font = pygame.font.SysFont(None, 80)
            text = font.render("GAME COMPLETE!", True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 40))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        else:
            platforms, enemies, goal = load_level(current_level_index)
            player.x, player.y = 100, 500
            player_vel_y = 0
            scroll_x = 0
            level_complete = False

    pygame.display.flip()

pygame.quit()
sys.exit()

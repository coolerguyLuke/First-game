import pygame
import math

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.width = 40
        self.height = 50
        self.on_ground = False

    def update(self, line_start, line_end, line_thickness):
        # Gravity
        if not self.on_ground:
            self.vel.y += 0.5  # gravity

        # Move
        self.pos += self.vel

        # Collision with line (platform)
        bottom_center = (self.pos.x + self.width // 2, self.pos.y + self.height)
        dist = point_line_distance(*bottom_center, *line_start, *line_end)
        # Check if player's feet are close enough to the line to "stand" on it
        if dist <= line_thickness // 2 + 2 and self.vel.y >= 0 and bottom_center[0] >= min(line_start[0], line_end[0]) and bottom_center[0] <= max(line_start[0], line_end[0]):
            self.on_ground = True
            self.vel.y = 0
            self.pos.y = line_start[1] - self.height  # Snap to line
        else:
            self.on_ground = False

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 200, 0), (self.pos.x, self.pos.y, self.width, self.height))

def point_line_distance(px, py, x1, y1, x2, y2):
    line_mag = math.hypot(x2 - x1, y2 - y1)
    if line_mag == 0:
        return math.hypot(px - x1, py - y1)
    u = ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / (line_mag ** 2)
    u = max(min(u, 1), 0)
    ix = x1 + u * (x2 - x1)
    iy = y1 + u * (y2 - y1)
    return math.hypot(px - ix, py - iy)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(200, 100)
line_start = (0, 400)
line_end = (700, 400)
line_thickness = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.vel.x = -3
    elif keys[pygame.K_RIGHT]:
        player.vel.x = 3
    else:
        player.vel.x = 0
    if keys[pygame. K_SPACE] and player.on_ground:
        player.vel.y = -10  # Jump

    player.update(line_start, line_end, line_thickness)

    screen.fill((30, 30, 30))
    pygame.draw.line(screen, (255, 255, 255), line_start, line_end, line_thickness)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
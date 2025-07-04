import pygame

from utils import point_line_distance


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


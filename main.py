import pygame
import sys

from player import Player

def reset_player():
    return Player(200, 100)

# TODO: replace state strings with enum
STATE_PLAYING = "playing"
STATE_DEAD = "dead"

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

state = STATE_PLAYING
falling_velocity = 0.5

player = reset_player()

# TODO: replace with class
line_start = (100, 500)
line_end = (1100, 500)
line_thickness = 5
line_y = 500

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # TODO: figure out if this makes sense
        if state == STATE_DEAD and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = STATE_PLAYING
                player = reset_player()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vel.x = -3
            elif event.key == pygame.K_RIGHT:
                player.vel.x = 3

            if event.key == pygame.K_SPACE and player.on_ground:
                player.vel.y = -10  # Jump
        else:
            player.vel.x = 0

    screen.fill((30, 30, 30))

    if state == STATE_PLAYING:
        player.update(line_start, line_end, line_thickness)

        # Draw floor
        pygame.draw.rect(screen, (100, 240, 100), (0, line_y, 800, 50))

        player.draw(screen)

        # TODO: replace player_radius with some member from the Player class instance player
        # Check if player fell off the floor
        if player.pos.y - (player.height // 2) > 600:
            state = STATE_DEAD

    elif state == STATE_DEAD:
        # Draw death screen
        font = pygame.font.SysFont(None, 72)
        text = font.render("You Died!", True, (255, 50, 50))
        subtext = font.render("Press SPACE to restart", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 200))
        screen.blit(subtext, (screen.get_width() // 2 - subtext.get_width() // 2, 300))

    pygame.display.flip()
    clock.tick(60)

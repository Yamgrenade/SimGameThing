#hello world
import pygame
import sys
import time
from map_stuff.game_map import GameMap


def draw_grid(screen, g_map, size):
    for x in range(g_map.width):
        for y in range(g_map.height):
            if g_map.is_blocked(x, y):
                rect = pygame.Rect(x*size, y*size, size, size)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)
            else:
                rect = pygame.Rect(x * size, y * size, size, size)
                pygame.draw.rect(screen, (0, 0, 0), rect, 0)


def draw_entities(screen, entities):
    for entity in entities:
        pygame.draw.circle(screen, entity.color, (entity.x * 20 + 10, entity.y * 20 + 10), 5)  # have to *20 because it doesn't know how big tiles are


def main():
    
    screen_width = 800
    screen_height = 800
    tile_size = 20
    turn_length = .5  # Iteration length in seconds

    # Map constants, including height, width, and tile size in pixels.
    map_width = screen_width // tile_size
    map_height = screen_height // tile_size

    entities = []

    g_map = GameMap(map_width, map_height)
    g_map.initialize_tiles()
    g_map.place_animals(10,4, entities)

    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((0, 0, 0)) # Fill with Black

    while True:

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:                                # On Escape key ...
                break                                    # leave the game loop.
            else:
                print(key)
            '''    
            elif key == 32:                              # Space bar steps through iterations
                for entity in entities:
                    if entity.ai:
                        entity.ai.take_turn(g_map, entities)
            
            else:
                print(key)
            '''
        time.sleep(turn_length)
        for entity in entities:
            if entity.ai:
                entity.ai.take_turn(g_map, entities)

        draw_grid(screen, g_map, tile_size)
        draw_entities(screen, entities)
        pygame.display.flip()

    # We've escaped the game loop
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

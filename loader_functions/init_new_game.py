import tcod as libtcod
from game_messages import MessageLog
from random import randint
from animals import animals
import copy

from map_stuff.game_map import GameMap


def get_constants():
    window_title = "Sim \"Game\" Prototype 1.0v1 0 Alponanona woah!"

    screen_width = 40
    screen_height = 40

    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    map_width = 40
    map_height = 40

    turn_length = .5
    num_rabbits = 10
    num_wolves = 4


    colors = {
        "dark_wall": libtcod.Color(0, 0, 100),
        "dark_ground": libtcod.Color(50, 50, 150),
        "light_wall": libtcod.Color(130, 110, 50),
        "light_ground": libtcod.Color(200, 180, 50),
    }

    constants = {
        "window_title": window_title,
        "screen_width": screen_width,
        "screen_height": screen_height,
        "bar_width": bar_width,
        "panel_height": panel_height,           # Some old stuff in here like panel specs. might still be handy if we
        "panel_y": panel_y,                     # can figure it out.
        "message_x": message_x,
        "message_width": message_width,
        "message_height": message_height,
        "map_width": map_width,
        "map_height": map_height,
        "colors": colors,
        "turn_length": turn_length,
        "num_rabbits": num_rabbits,
        "num_wolves": num_wolves,
    }

    return constants


def get_game_variables(constants):
    game_map = GameMap(constants["map_width"], constants["map_height"])
    game_map.initialize_tiles()

    message_log = MessageLog(
        constants["message_x"], constants["message_width"], constants["message_height"]
    )

    entities = []

    return entities, game_map, message_log


def place_animals(constants, entities, game_map):
    for n in range(constants["num_rabbits"]):
        x = randint(1, constants["map_width"] - 1)
        y = randint(1, constants["map_height"] - 1)

        if not any([entity for entity in entities if entity.x == x and entity.y == y]) and not game_map.is_blocked(x, y):
            animal_instance = None
            for name, animal in animals.items():
                if name == 'rabbit':
                    animal_instance = copy.deepcopy(animal)
                    animal_instance.place(x, y)
                    break

            entities.append(animal_instance)

    for n in range(constants["num_wolves"]):
        x = randint(1, constants["map_width"] - 1)
        y = randint(1, constants["map_height"] - 1)

        if not any([entity for entity in entities if entity.x == x and entity.y == y]):
            animal_instance = None
            for name, animal in animals.items():
                if name == 'wolf':
                    animal_instance = copy.deepcopy(animal)
                    animal_instance.place(x, y)
                    break

            entities.append(animal_instance)

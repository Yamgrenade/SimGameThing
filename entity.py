import math
from render_functions import RenderOrder

'''
Generic Entity class. Will just be animals for now, as far as I can tell.
Additional attributes that might be useful:
render order
components for behavior
'''


class Entity:
    def __init__(self, x, y, char, color, name, blocks=False, ai=None, render_order=RenderOrder.PLACEHOLDER):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.ai = ai
        self.render_order = render_order

        if self.ai:
            self.ai.owner = self

    # move the entity by the specified dx, dy
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_towards(self, target_x, target_y, game_map, entities):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        if not (game_map.is_blocked(self.x + dx, self.y + dy) or
                get_blocking_entities_at_location(entities, self.x + dx, self.y + dy)):
            self.move(dx, dy)

    def distance(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def place(self, x, y):
        self.x = x
        self.y = y
        return self


def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity

    return None

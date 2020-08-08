from random import randint

'''
Walk randomly or hold still. Placeholder for actual ai. Needs entity code to work.
'''
class RandomWalker:
    def take_turn(self, game_map, entities):
        walker = self.owner

        random_x = self.owner.x + randint(0, 2) - 1
        random_y = self.owner.y + randint(0, 2) - 1

        if random_x != self.owner.x and random_y != self.owner.y:
            walker.move_towards(random_x, random_y, game_map, entities)

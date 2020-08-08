from entity import Entity
from components.ai import RandomWalker

animals = {
    'rabbit': Entity(-1, -1, 'r', (100, 50, 10), 'rabbit', blocks=True, ai=RandomWalker()),
    'wolf': Entity(-1, -1, 'w', (200, 0, 0), 'wolf', blocks=True, ai=RandomWalker())
}

# x, y, char, color, name, blocks=False, ai=None

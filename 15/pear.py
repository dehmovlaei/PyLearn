import random
from stuff import Stuff

class Pear(Stuff):
    def __init__(self, game):
        super().__init__('15/pear.png')
        self.width = 44
        self.height = 44
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.change_x = 0
        self.change_y = 0
        self.score = 2
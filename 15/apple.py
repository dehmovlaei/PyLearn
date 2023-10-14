import random
from stuff import Stuff

class Apple(Stuff):
    def __init__(self, game):
        super().__init__('15/apple.png')
        self.width = 33
        self.height = 33
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.change_x = 0
        self.change_y = 0
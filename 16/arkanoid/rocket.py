import arcade

class Rocket(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width//2
        self. center_y = 45
        self.change_x 
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.speed = 4
        self.score = 0
        self.game_width = game.width

    def move(self):
        if self.change_x == -1 and self.center_x > 0:
            self.center_x -= self.speed
        elif self.change_x == 1 and self.center_x < self.game_width:
            self.center_x += self.speed
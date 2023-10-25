import arcade

class Rocket(arcade.Sprite):
    def __init__(self, game):
        super().__init__('16/arkanoid/rocket.png')
        self.center_x = game.width//2
        self. center_y = 45
        self.change_x 
        self.change_y = 0
        self.width = 150
        self.height = 40
        self.speed = 4
        self.score = 0
        self.angle = 360
        self.game_width = game.width

    def move(self):
        if self.change_x == -1 and self.center_x > 0+85:
            self.center_x -= self.speed
        elif self.change_x == 1 and self.center_x < self.game_width-85:
            self.center_x += self.speed
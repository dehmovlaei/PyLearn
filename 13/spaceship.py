import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.center_x = game.width // 2
        self.center_y = 45
        self.width = 55
        self.height = 55
        self.speed = 20

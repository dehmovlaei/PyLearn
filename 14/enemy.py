import random
import arcade
class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(':resources:images/space_shooter/playerShip1_orange.png')
        self.center_x = random.randint(55, game.width)
        self.center_y = game.height + 24
        self.width = 55
        self.height = 55
        self.speed = 2
        self.angle = 180
        self.destruction_sound = arcade.load_sound(':resources:sounds/lose1.wav',False)

    def move(self):
        self.center_y -= self.speed
        self.speed += 0.01

    def destruction(self):
        arcade.play_sound(self.destruction_sound)
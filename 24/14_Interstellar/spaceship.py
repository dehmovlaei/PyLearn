import arcade
from bullet import Bullet
class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.center_x = game.width // 2
        self.center_y = 45
        self.change_x
        self.change_y = 0
        self.width = 55
        self.height = 55
        self.speed = 8
        self.game_width = game.width
        self.bullet_list = []
        self.fire_sound = arcade.load_sound(':resources:sounds/laser2.wav',False)
        self.destruction_sound = arcade.load_sound(':resources:sounds/lose3.wav',False)
    
    def move(self):
        if self.change_x == -1 and self.center_x > 0:
            self.center_x -= self.speed
        elif self.change_x == 1 and self.center_x < self.game_width:
            self.center_x += self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
        arcade.play_sound(self.fire_sound)

    def destruction(self):
        arcade.play_sound(self.destruction_sound)
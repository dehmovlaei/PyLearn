import random
import arcade
from spaceship import Spaceship

class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(':resources:images/space_shooter/playerShip1_orange.png')
        self.center_x = random.randint(55, game.width)
        self.center_y = game.height + 24
        self.width = 55
        self.height = 55
        self.speed = 5
        self.angle = 180

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280, height=720, title='Interstellar Game 2023')
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.background = arcade.load_texture('13/NightSky.webp')
        self.me = Spaceship(self)
        self.oppo = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.oppo.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.me.center_x -= self.me.speed
        elif symbol == 100:
            self.me.center_x += self.me.speed

    def on_update(self, delta_time: float):
        self.oppo.center_y -= self.oppo.speed

window = Game()
arcade.run()
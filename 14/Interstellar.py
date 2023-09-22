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
        self.speed = 2
        self.angle = 180
    def move(self):
        self.center_y -= self.speed

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280, height=720, title='Interstellar Game 2023')
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.background = arcade.load_texture('13/NightSky.webp')
        self.me = Spaceship(self)
        self.oppos = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()

        for oppo in self.oppos:
            oppo.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()

        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.me.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.me.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.me.change_x = 0
        elif symbol == arcade.key.SPACE:
            self.me.fire()
    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0

    def on_update(self, delta_time: float):
        
        self.me.move()

        for bullet in self.me.bullet_list:
            bullet.move()
        
        if random.randint(1, 100) == 6:
            self.new_oppos = Enemy(self)
            self.oppos.append(self.new_oppos)
        
        for oppo in self.oppos:
            oppo.move()

        for oppo in self.oppos:
            if arcade.check_for_collision(self.me, oppo):
                 print('GAME OVER 💀')
                 exit(0)

        for oppo in self.oppos:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(oppo, bullet):
                    self.oppos.remove(oppo)
                    self.me.bullet_list.remove(bullet)

        for oppo in self.oppos:
            if oppo.center_y < 0:
                self.oppos.remove(oppo)

window = Game()
arcade.run()
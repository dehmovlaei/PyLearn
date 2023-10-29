import arcade
from rocket import Rocket
from ball import Ball
from block import Block
from life import Life
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=800, title='arkanoid 🔵🔵🔵', center_window=True)
        self.background = arcade.load_texture(':resources:images/backgrounds/abstract_1.jpg')
        self.rocket = Rocket(self)
        self.sprite_list = arcade.SpriteList()
        self.ball = Ball(self)
        self.blocks = []
        self.x = 25
        self.y = 600
        self.x_left = 0
        self.life = []
     
        for _ in range(3):
            self.new_life = Life(self.x_left)
            self.x_left += 45
            self.life.append(self.new_life)

        self.color = [arcade.color.BABY_BLUE, arcade.color.BABY_BLUE_EYES, arcade.color.WHITE,
                        arcade.color.PINK, arcade.color.AMERICAN_ROSE
                        ]

        for i in range(5):
            for _ in range(11):
                self.block = Block(self.x, self.y, self.color[i])
                self.blocks.append(self.block)
                self.x += 55                
            self.y += 35
            self.x = 25
    
    def game_over(self):
        self.blocks = []
        self.life = []
        del self.ball
        del self.rocket
        arcade.set_background_color(arcade.color.WHITE)
        self.background = arcade.load_texture('16/arkanoid/GameOver.jpg')
        print('GAME OVER 💀')

    def on_draw(self):
       
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

        if self.life:
            for block in self.blocks:
                block.draw()
            
            self.rocket.draw()
            self.ball.draw()
            for life in self.life:
                life.draw()
            arcade.draw_text(f'SCORE: {self.rocket.score}', 5, 780, arcade.color.AMERICAN_ROSE, 15, 2,'left',('calibri', 'calibri'), True)
            
        arcade.finish_render

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.rocket.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.rocket.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.rocket.change_x = 0

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        
        if self.rocket.width-75 < x < self.width-self.rocket.width+75:
            self.rocket.center_x = x

    def on_update(self, delta_time: float):
        if self.life:
            self.ball.move()
            self.rocket.move()
            
            if self.ball.center_x < 2 or self.ball.center_x > self.width-2:
                self.ball.change_x *= -1

            if self.ball.center_y > self.height:
                self.ball.change_y *= -1
            
            if arcade.check_for_collision(self.rocket, self.ball):
                self.ball.change_y *= -1

            for count, block in enumerate(self.blocks):
                if arcade.check_for_collision(self.ball, block):
                    self.ball.change_y *= -1
                    self.ball.speed += 0.2
                    self.rocket.score += 1
                    self.rocket.speed += 0.1
                    del self.blocks[count]

            if self.ball.center_y < 0:
                print('OOps !!!')
                del self.ball
                self.new_life.lose_life()
                self.life.pop()
                self.ball = Ball(self)
            if not self.life:
                self.game_over()
        
if __name__ == '__main__':
     game = Game()
     arcade.run()
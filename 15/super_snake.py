import arcade
from apple import Apple
from pear import Pear
from shit import Shit
from snake import Snake            
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 500, height = 500, title = 'SUPER SNAKE 🐍 V1',center_window = True)
        arcade.set_background_color(arcade.color.KHAKI)
        self.background = arcade.load_texture('15/GameOver.jpg')
        self.game_over = False
        self.score = 0
        self.food = []
        self.init_food()
        self.snake = Snake(self)

    def init_food(self):
        self.food.append(Apple(self))
        self.food.append(Pear(self))
        self.food.append(Shit(self))
    
    def on_draw(self):
        arcade.start_render()
        if self.game_over == True:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        else:
            for food in self.food:
                food.draw()
            self.snake.draw()
        arcade.draw_text(f'SCORE:{self.score}', 395, 480, arcade.color.ALABAMA_CRIMSON, 15, 2,'left',('calibri', 'arial'), True)
        arcade.finish_render

    def on_update(self, delta_time: float):
        if self.game_over == False:
            self.snake.move()
            for food in self.food:
                if arcade.check_for_collision(self.snake, food):
                    self.score = self.snake.eat(food)
                    self.food = []
                    self.init_food()
            for count, part in enumerate(self.snake.body):
                for i in range(count + 1, len(self.snake.body)):
                    if part['x'] == self.snake.body[i]['x'] and part['y'] == self.snake.body[i]['y']:
                        self.game_over = True
            if (
                self.snake.center_x < 0 or self.snake.center_x > 500 or self.snake.center_y < 0
                or self.snake.center_y > 500 or self.score < 0
            ):
                self.game_over = True
           
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        
if __name__ == '__main__':
     game = Game()
     arcade.run()
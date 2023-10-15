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
        self.food = []
        self.init_food()
        self.snake = Snake(self)

    def init_food(self):
        self.food.append(Apple(self))
        self.food.append(Pear(self))
        self.food.append(Shit(self))
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        for food in self.food:
            food.draw()
        self.snake.draw()
        arcade.finish_render

    def on_update(self, delta_time: float):
        self.snake.move()

        for food in self.food:
            if arcade.check_for_collision(self.snake, food):
                self.snake.eat(food)
                self.food = []
                self.init_food()
        # for part in self.snake.body:
        #     if arcade.check_for_collision(part, self.snake):
        #         print('game over')
        if (
            self.snake.center_x < 0 or self.snake.center_x > 500 or self.snake.center_y < 0
            or self.snake.center_y > 500 or self.snake.score < 0
        ):
            self.game_over()
            

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

    def game_over(self):
        # del self.snake
        # self.food =[]
        # arcade.set_background_color(arcade.color.WHITE)
        self.background = arcade.load_texture('15/GameOver.jpg')
        print('GAME OVER 💀')
        
if __name__ == '__main__':
     game = Game()
     arcade.run()
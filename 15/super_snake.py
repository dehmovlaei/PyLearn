import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__('15/apple.png')
        self.width = 33
        self.height = 33
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.change_x = 0
        self.change_y = 0
    

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 35
        self.height = 35
        self.radius = 19
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.GREEN_YELLOW
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self):
        self.score += 1
        

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 500, height = 500, title = 'SUPER SNAKE 🐍 V1')
        arcade.set_background_color(arcade.color.KHAKI)

        self.food = Apple(self)
        self.snake = Snake(self)

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.snake.draw()
        arcade.finish_render

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat()
            print('Score:', self.snake.score)
            del self.food
            self.food = Apple(self)

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
import arcade

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
        self.speed = 2
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
        
        for part in self.body:
            arcade.draw_circle_filled(part['x'], part ['y'], self.radius, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        self.body.append({'x':self.center_x, 'y':self.center_y})
        
        if len(self.body) > self.score:
            self.body.pop(0)

    def eat(self, food):
        del food
        self.score += 1
        print('Score:', self.score)
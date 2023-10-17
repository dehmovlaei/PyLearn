import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 35
        self.height = 35
        self.radius = 19
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.colors = [arcade.color.GREEN_YELLOW, arcade.color.AIR_FORCE_BLUE]
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.score = 0
        self.body = []
        self.body.append({'x':self.center_x, 'y':self.center_y})
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.colors[0])
        
        for count, part in enumerate(self.body):
            arcade.draw_circle_filled(part['x'], part['y'], self.radius, self.colors[(count%2)])


    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        self.body.append({'x':self.center_x, 'y':self.center_y})
        
        if len(self.body) > self.score:
            self.body.pop(0)

    def eat(self,food):
        self.score += food.score
        print('Score:', self.score)
        return self.score
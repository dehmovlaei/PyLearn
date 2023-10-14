import arcade

class Stuff(arcade.Sprite):
    def __init__(self, shape):
        super().__init__(shape)
        self.width = 33
        self.height = 33
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
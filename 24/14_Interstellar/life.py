import arcade

class Life(arcade.Sprite):
    def __init__(self, game):
        super().__init__(':resources:images/space_shooter/playerLife1_blue.png')
        self.center_x = game.x_left + 33
        self.center_y = 33
        self.lose_life_sound = arcade.load_sound(':resources:sounds/lose2.wav',False)
    
    def lose_life(self):
        arcade.play_sound(self.lose_life_sound)
        

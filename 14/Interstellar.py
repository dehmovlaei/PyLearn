import arcade
from spaceship import Spaceship
from enemy import Enemy
from life import Life

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 1280, height = 720, title = 'Interstellar Game 2023')
        self.background = arcade.load_texture('14/NightSky.webp')
        self.score = 0
        self.me = Spaceship(self)
        self.enemies = []
        self.life = []
        self.x_left = 0
        for _ in range(3):
            self.new_life = Life(self)
            self.x_left += 33
            self.life.append(self.new_life)
        
        arcade.schedule(self.add_enemy, 3)

    def add_enemy(self, delta_time: float):
        if self.life:
            self.new_enemies = Enemy(self)
            self.enemies.append(self.new_enemies)

    def game_over(self):
        self.enemies = []
        self.me.bullet_list = []
        arcade.set_background_color(arcade.color.WHITE)
        self.background = arcade.load_texture('14/GameOver.jpg')
        print('GAME OVER 💀')

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        
        for enemy in self.enemies:
            enemy.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()
        
        for life in self.life:
            life.draw()

        arcade.draw_text(f'SCORE:{self.score}', 1155, 22, arcade.color.ALABAMA_CRIMSON, 15, 2,'left',('calibri', 'arial'), True)

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
           
        for enemy in self.enemies:
            enemy.move()

        #collision with spaceship and game over 
        for enemy in self.enemies:
            if arcade.check_for_collision(self.me, enemy):
                 self.me.destruction()
                 self.life = []
                 self.game_over()

        #kill enemy and count score
        for enemy in self.enemies:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    enemy.destruction()
                    self.enemies.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score += 1

        #run enemy and  check for game over
        for enemy in self.enemies:
            if enemy.center_y < 0 and self.life:
                self.enemies.remove(enemy)
                self.new_life.lose_life()
                self.life.pop()
            if not self.life:
                self.game_over()
        
        #remove bullet
        for bullet in self.me.bullet_list:
            if bullet.center_y > 720:
                self.me.bullet_list.remove(bullet)

window = Game()
arcade.run()
import arcade

raw_col = 65
raw_row = 65
l_margin = 35
b_margin = 35

arcade.open_window(650, 650, "DIAMOND")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * raw_col + l_margin
        y = row * raw_row + b_margin
        if column % 2 == 0 and row %2 == 0  or column % 2 == 1 and row %2 == 1:
            arcade.draw_triangle_filled(x - 10,y, x, y + 10,x + 10,y, arcade.color.RED)
            arcade.draw_triangle_filled(x - 10,y, x, y - 10,x + 10,y, arcade.color.RED)           
        if column % 2 == 1 and row % 2 == 0  or column % 2 == 0 and row % 2 == 1:
            arcade.draw_triangle_filled(x - 10,y, x, y + 10,x + 10,y, arcade.color.BLUE)
            arcade.draw_triangle_filled(x - 10,y, x, y - 10,x + 10,y, arcade.color.BLUE)
arcade.finish_render()
arcade.run()
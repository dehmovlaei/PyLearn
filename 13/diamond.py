import arcade

RAW_COL = 65
RAW_ROW = 65
l_margin = 50
b_margin = 50

arcade.open_window(650, 650, "DIAMOND")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * RAW_COL + l_margin
        y = row * RAW_ROW + b_margin
        if column%2==0 and row%2==0  or column%2==1 and row%2==1:
            arcade.draw_triangle_filled(x-7,y, x, y+7,x+7,y, arcade.color.RED)
            arcade.draw_triangle_filled(x-7,y, x, y-7,x+7,y, arcade.color.RED)           
        if column%2==1 and row%2==0  or column%2==0 and row%2==1:
            arcade.draw_triangle_filled(x-7,y, x, y+7,x+7,y, arcade.color.BLUE)
            arcade.draw_triangle_filled(x-7,y, x, y-7,x+7,y, arcade.color.BLUE)
arcade.finish_render()
arcade.run()
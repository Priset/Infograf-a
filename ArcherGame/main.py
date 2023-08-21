import arcade
from game_object import Archer, Target, Arrow

WIDTH = 800
HEIGHT = 600
TITLE = "Archer Game"

class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        self.background = arcade.load_texture("assets/img/background.png")
        self.archer = Archer("assets/img/archer.png", 100, 100)
        self.target = Target("assets/img/target.png", 600, 100)
        self.arrow = None  
        self.draw_line = False
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        self.archer.draw()
        self.target.draw()
        if self.draw_line:
            arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y, arcade.color.BLACK)
        if self.arrow:
            self.arrow.draw()
    
    def on_update(self, delta_time):
        if self.arrow:
            self.arrow.update()
        
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.start_x = x
            self.start_y = y
            self.end_x = x
            self.end_y = y
            self.draw_line = True
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.draw_line:
            self.end_x = x
            self.end_y = y
    
    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.draw_line:
            self.draw_line = False
            self.arrow = Arrow("assets/img/arrow.png", self.archer.center_x, self.archer.center_y, x, y)

def main():
    app = App()
    arcade.run()

if __name__ == "__main__":
    main()

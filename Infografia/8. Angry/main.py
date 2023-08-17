import math

import arcade
import pymunk

from game_object import Bird, Column, Pig

WIDTH = 1800
HEIGHT = 800
TITLE = "Angry birds"


class App(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        self.background = arcade.load_texture("8. Angry/assets/img/background3.png")
        # crear espacio de pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)
        # parametros para el lanzamiento
        self.start_point = ()
        self.end_point = ()
        self.distance = 0
        self.draw_line = False

        # agregar piso
        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, [0, 50], [WIDTH, 50], 0.0)
        floor_shape.friction = 10
        self.space.add(floor_body, floor_shape)

        self.sprites = arcade.SpriteList()
        self.add_columns()
        self.add_pigs()

        self.start_point = ()
        self.end_point = ()
        self.distance = 0
        self.draw_line = False

    def add_columns(self):
        for x in range(WIDTH // 2, WIDTH, 50):
            column = Column(x, 100, self.space)
            self.sprites.append(column)

    def add_pigs(self):
        pig1 = Pig(WIDTH / 2, 100, self.space)
        self.sprites.append(pig1)

    def on_update(self, delta_time: float):
        self.space.step(1 / 60.0)   # actualiza la simulacion de las fisicas
        self.sprites.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.start_point = x, y
            self.end_point = x, y
            self.distance = 0
            self.draw_line = True

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            self.end_point = x, y
            self.distance = math.sqrt((self.start_point[0] - self.end_point[0])**2 + (self.start_point[1] - self.end_point[1])**2)
            self.draw_line = True

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.draw_line = False
            angle = math.atan2(self.end_point[1] - self.start_point[1], self.end_point[0] - self.start_point[0])
            reversed_angle = angle + math.pi
            bird = Bird("8. Angry/assets/img/red-bird3.png", self.distance, reversed_angle, *self.start_point, self.space)
            self.sprites.append(bird)
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        self.sprites.draw()
        if self.draw_line:
            arcade.draw_line(self.start_point[0], self.start_point[1], self.end_point[0], self.end_point[1], arcade.color.BLACK, 3)


def main():
    app = App()
    arcade.run()


if __name__ == "__main__":
    main()
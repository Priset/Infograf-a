#importamos el paquete
import arcade
import math
import cmath

#definición de contantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to arcade"

def draw_circle(x,y,p):
    arcade.draw_circle_filled(x, y, p, arcade.color.ALABAMA_CRIMSON)
    
def draw_columna(x,y,p):
    arcade.draw_texture_rectangle(200, 300, 100, 100, arcade.texture.load_texture, 100, 80, arcade.color.AERO_BLUE)

if __name__ == "__main__":
    #Crear nueva ventana
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    
    #Cambiar el color de fondo
    arcade.set_background_color(arcade.color.RED_ORANGE)
    
    #Iniciar render
    arcade.start_render()
    
    #Funciones para dibujar
    draw_circle(300, 400, 50)
    draw_circle(200, 300, 50)
    
    #Finalizar render
    arcade.finish_render()
    
    #Correr el programa
    arcade.run()
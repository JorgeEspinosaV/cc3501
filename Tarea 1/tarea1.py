import pyglet
import numpy as np

window = pyglet.window.Window(800, 600)
batch = pyglet.graphics.Batch()

sky = pyglet.shapes.Rectangle(0, 0, width=window.width, height=window.height,
color = (0,31,195), batch=batch)

class Nave:
    def __init__(self, x_initial: float, y_initial: float):
        self.x_initial = x_initial
        self.y_initial = y_initial
        self.body_left = pyglet.shapes.Triangle(x = x_initial, y = y_initial, 
                                                x2 = x_initial,y2 = y_initial - 160, 
                                                x3 = x_initial - 25, y3 = y_initial - 105,
                                                batch=batch)

        self.body_right = pyglet.shapes.Triangle(x = x_initial,y = y_initial, 
                                                x2 = x_initial, y2 = y_initial - 160, 
                                                x3 = x_initial + 25,y3 = y_initial - 105,
                                                batch=batch)

        self.wing_left = pyglet.shapes.Triangle(x = x_initial - 35, y = y_initial - 100, 
                                               x2 = x_initial - 5, y2 = y_initial - 110, 
                                               x3 = x_initial - 95, y3  = y_initial - 190,
                                               batch=batch)

        self.wing_right = pyglet.shapes.Triangle(x = x_initial + 35, y = y_initial - 100, 
                                                x2 = x_initial + 5, y2 = y_initial - 110, 
                                                x3 = x_initial + 95, y3  = y_initial - 190,
                                                batch=batch)

        self.propellant_left1 = pyglet.shapes.Triangle(x = x_initial - 22, y = y_initial - 70,
                                                    x2 = x_initial - 27, y2 = y_initial - 180,
                                                    x3 = x_initial - 26, y3 = y_initial - 110,
                                                    batch = batch, color=(160, 170, 255))

        self.propellant_left2 = pyglet.shapes.Triangle(x = x_initial - 22, y = y_initial - 70,
                                                     x2 = x_initial - 27, y2 = y_initial - 180,
                                                     x3 = x_initial - 17, y3 = y_initial - 115,
                                                     batch = batch, color=(160, 170, 255))

        self.propellant_right1 = pyglet.shapes.Triangle(x = x_initial + 22, y = y_initial - 70,
                                                    x2 = x_initial + 27, y2 = y_initial - 180,
                                                    x3 = x_initial + 26, y3 = y_initial - 110,
                                                    batch = batch, color=(160, 170, 255))
                                                    
        self.propellant_right2 = pyglet.shapes.Triangle(x = x_initial + 22, y = y_initial - 70,
                                                     x2 = x_initial + 27, y2 = y_initial - 180,
                                                     x3 = x_initial + 17, y3 = y_initial - 115,
                                                     batch = batch, color=(160, 170, 255))


class Star:
    def __init__(self, x_initial: float, y_initial: float):
        self.x_initial = x_initial
        self.y_initial = y_initial

        self.star = pyglet.shapes.Star(x = x_initial, y = y_initial, outer_radius = 5, inner_radius = 15, num_spikes = 5, batch=batch)


nave = Nave(400, 300)
star = Star(90, 100)

@window.event
def on_draw():
    window.clear()
    batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
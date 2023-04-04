import pyglet
import numpy as np
import random 

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
                                                batch=batch, color=(252, 215, 173))

        self.body_right = pyglet.shapes.Triangle(x = x_initial,y = y_initial, 
                                                x2 = x_initial, y2 = y_initial - 160, 
                                                x3 = x_initial + 25,y3 = y_initial - 105,
                                                batch=batch, color=(252, 215, 173))

        self.wing_left = pyglet.shapes.Triangle(x = x_initial - 35, y = y_initial - 100, 
                                               x2 = x_initial - 5, y2 = y_initial - 110, 
                                               x3 = x_initial - 95, y3  = y_initial - 190,
                                               batch=batch, color=(252, 215, 173))

        self.wing_right = pyglet.shapes.Triangle(x = x_initial + 35, y = y_initial - 100, 
                                                x2 = x_initial + 5, y2 = y_initial - 110, 
                                                x3 = x_initial + 95, y3  = y_initial - 190,
                                                batch=batch, color=(252, 215, 173))

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


numero_estrellas =  random.randint(10,40)


star1 = Star(10, 10)
star2 = Star(15, 220)
star3 = Star(22, 320)
star4 = Star(11, 560)
star5 = Star(90, 14)
star6 = Star(110, 211)
star7 = Star(105, 340)
star8 = Star(120, 590)
star9 = Star(111, 532)
star10 = Star(111, 111)
star11 = Star(120, 222)
star12 = Star(120, 222)
star13 = Star(120, 222)
star14 = Star(120, 222)
star15 = Star(120, 222)
star16 = Star(120, 222)
star17 = Star(120, 222)
star18 = Star(120, 222)
star19 = Star(120, 222)
star20 = Star(120, 222)

estrellas = [star1, star2, star3, star4, star5, star6, star7, star8, star9, star10,
            star11, star12, star13, star14, star15, star16, star17, star18, star19, star20]

nave_lider = Nave(400, 500)    
nave_izq = Nave(250, 250)
nave_der = Nave(550, 250)



@window.event
def on_draw():
    window.clear()
    
    batch.draw()


if __name__ == '__main__':
    
    pyglet.app.run()
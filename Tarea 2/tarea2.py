import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import repo.grafica.transformations as tr
import repo.grafica.basic_shapes as bs
import repo.grafica.scene_graph as sg 
import repo.grafica.easy_shaders as es 
import repo.grafica.performance_monitor as pm

class Controller:
    def __init__(self):
        self.fillPolygon = True
        self.showAxis = True


controller = Controller()

def on_key(window, key, scancode, action, mods):
    if action != glfw.PRESS:
        return

    global controller

    if key == glfw.KEY_SPACE:
        controller.fillPolygon = not controller.fillPolygon
    
    elif key == glfw.KEY_LEFT_CONTROL:
        controller.showAxis = not controller.showAxis

    elif key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)

    else:
        print("Unkown key")

class Nave:
    def __init__(self, x_initial: float, y_initial: float, z_initial: float):
        self.x_initial = x_initial
        self.y_initial = y_initial
        self.z_initial = z_initial
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



import pyglet
from pyglet.window import key
window = pyglet.window.Window()
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

def createCar(pipeline, r, g, b):
    redCube = bs.createColorCube(1,0,0)
    gpuRedCube = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuRedCube)
    gpuRedCube.fillBuffers(redCube.vertices, redCube.indices, GL_STATIC_DRAW)

    chasisCube = bs.createColorCube(r, g, b)
    gpuChasisCube = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuChasisCube)
    gpuChasisCube.fillBuffers(chasisCube.vertices, chasisCube.indices, GL_STATIC_DRAW)

    wheel = sg.SceneGraphNode("wheel")
    wheel.transform = tr.scale(0.2, 0.8, 0.2)
    wheel.childs += [gpuRedCube]

    wheelRotation = sg.SceneGraphNode("wheelRotation")
    wheelRotation.childs += [wheel]

    frontWheel = sg.SceneGraphNode("frontWheel")
    frontWheel.transform = tr.translate(0.3, 0, -0.3)
    frontWheel.childs += [wheelRotation]

    backWheel = sg.SceneGraphNode("backWheel")
    backWheel.transform = tr.translate(0.3, 0, -0.3)
    backWheel.childs += [wheelRotation]

    chasis = sg.SceneGraphNode("chasis")
    chasis.transform = tr.scale(1,0.7,0.5)
    chasis.childs += [gpuChasisCube]

    car = sg.SceneGraphNode("car")
    car.childs += [chasis]
    car.childs += [frontWheel]
    car.childs += [backWheel]

    return car

class Controller(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.fillPolygon=True
        self.showAxis=True
        self.pipeline = es.SimpleShaderProgram()
        self.car = createCar(pipeline, 0.2, 0.2, 0.2)

WIDTH, HEIGHT = 800, 800
controller=Controller(width=WIDTH, height=HEIGHT)



@controller.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        controller.fillPolygon = not controller.fillPolygon
    elif symbol == key.A:
        controller.showAxis = not controller.showAxis
    



@controller.event
def on_draw():
    controller.clear()
    sg.drawSceneGraphNode(controller.car, controller.pipeline, tr.identity())


if __name__ == "__main__":
    pyglet.app.run()




import repo.grafica.basic_shapes as bs
import repo.grafica.easy_shaders as es
import repo.grafica.scene_graph as sg
import repo.grafica.gpu_shape as gs
from repo.grafica.assets_path import getAssetPath

import sys
import os
from OpenGL.GL import *
import pyglet
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

groundRectangle = bs.createColorQuad(0.76, 0.69, 0.5)
gpuGroundRectangle = es.GPUShape().initBuffers()
mvpPipeline = es.SimpleModelViewProjectionShaderProgram()
mvpPipeline.setupVAO(gpuGroundRectangle)
gpuGroundRectangle.fillBuffers(groundRectangle.vertices, groundRectangle.indices, GL_STATIC_DRAW)
graph = sg.SceneGraphNode("graph")
graph.childs += [gpuGroundRectangle]

window = pyglet.window.Window(width=600, height=600)

ASSETS = {
    "tex": getAssetPath("./Aux 4/assets/bricks.jpg")
}

class Controller(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.pipeline = es.SimpleTextureModelViewProjectionShaderProgram()
        self.texture_coords = [1, 1]
        self.ex_shape = gs.createGPUShape(self.pipeline, bs.createTextureCube(*self.texture_coords))
        self.tex_params = [GL_REPEAT, GL_NEAREST]
        self.current_tex = "tex"
        self.ex_shape.texture = es.textureSimpleSetup(ASSETS[self.current_tex], *self.tex_params)

@window.event
def on_draw():
    window.clear()
    sg.drawSceneGraphNode(graph, mvpPipeline, "model")

pyglet.app.run()
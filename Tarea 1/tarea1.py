from pyglet.gl import *
from pyglet.graphics import Batch
from pyglet.graphics.shader import Shader, ShaderProgram


def shader_program():
    vertex_source = """#version 150 core
        in vec2 position;
        in vec4 colors;
        out vec4 vertex_colors;

        uniform mat4 projection;

        void main()
        {
            gl_Position = projection * vec4(position, 0.0, 1.0);
            vertex_colors = colors;
        }
    """

    fragment_source = """#version 150 core
        in vec4 vertex_colors;
        out vec4 final_color;

        void main()
        {
            final_color = vertex_colors;
        }
    """

    vert_shader = Shader(vertex_source, 'vertex')
    frag_shader = Shader(fragment_source, 'fragment')
    program = ShaderProgram(vert_shader, frag_shader)
    return program




class Triangle:
    def __init__(self):
        triangle = Batch()
        program = shader_program()
        self.vertices = program.vertex_list(3, GL_TRIANGLES, batch = triangle,
                                            position=("f", (-0.5, -0.5, 0.5, -0.5, 0.0,0.5)),
                                            colors=("Bn", (0,218, 22)))

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        self.triangle = Triangle()
        
    def on_draw(self):
        self.triangle.vertices.draw(GL_TRIANGLES)
        
if __name__ == "__main__":
    window = MyWindow(1280, 720, "Tarea 1", resizable = True)
    window.on_draw()
    pyglet.app.run()
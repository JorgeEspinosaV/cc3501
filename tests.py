import pyglet
import repo.grafica.transformations as tr

# Crear ventaja
window = pyglet.window.Window()

# Crear modelo 3D
vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]

indices = [0, 1, 2]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]

vertex_shader = """
# version 120

attribute vec3 position;
attribute vec3 color;

varying vec3 outColor;

uniform mat4 transform;

void main()
{
    gl_Position = transform * vec4(position, 1.0);
    outColor = color;
}
"""

fragment_shader = """
# version 120

varying vec3 outColor;

void main()
{
    gl_FragColor = vec4(outColor, 1.0);
}
"""

shader = pyglet.graphics.shader(vertex_shader, fragment_shader)

vbo = pyglet.graphics.vertexbuffer.create_buffer(vertices)
ibo = pyglet.graphics.vertexbuffer.create_index_buffer(indices)
cbo = pyglet.graphics.vertexbuffer.create_color_buffer(colors)

vao = pyglet.graphics.vertexbuffer.create_vao(shader, [vbo, cbo], ibo)

# Definir matríz de transformación para rotar el modelo
rotation = tr.rotationX(0.5)

# Función de dibujo
@window.event
def on_draw():
    window.clear()

    shader.bind()
    shader.uniform_matrixf("transform", rotation)
    vao.render(pyglet.gl.GL_TRIANGLES)
    shader.unbind()

# Bucle principal
pyglet.app.run()
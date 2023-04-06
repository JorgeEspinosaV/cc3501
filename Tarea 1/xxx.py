import pyglet

# Crea la ventana
window = pyglet.window.Window()

# Crea una figura para mover
circle = pyglet.shapes.Circle(x=0, y=window.height / 2, radius=30)

# Define la función para actualizar la posición de la figura
def update(dt):
    circle.x += 100 * dt
    # Si la figura salió de la ventana
    if circle.x > window.width + circle.radius:
        # Colócala de vuelta en la izquierda
        circle.x = 0 - circle.radius

# Añade la función de actualización al bucle de Pyglet
pyglet.clock.schedule_interval(update, 1 / 60)

# Define la función para dibujar la figura en la ventana
@window.event
def on_draw():
    window.clear()
    circle.draw()

# Inicia el programa
pyglet.app.run()


import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

ancho = 640
alto = 480

def dibujarTriangulo():
    glPushMatrix()

    glTranslatef(-0.5, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(1, 0)
    glVertex2f(0.5, 1)
    glEnd()

    glPopMatrix()


def dibujarCuadrado():
    glPushMatrix()

    glTranslatef(-0.5, -0.5, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(1, 0)
    glVertex2f(1, 1)
    glVertex2f(0, 1)
    glEnd()

    glPopMatrix()

def init():
    pygame.init()
    pygame.display.set_mode((ancho, alto), OPENGL | DOUBLEBUF)
    pygame.display.set_caption("Pauta c2")
    # inicializar opengl
    glViewport(0, 0, ancho, alto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, ancho, 0.0, alto)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # definir variables de opengl
    glClearColor(1.0, 1.0, 1.0, 0.0)  # color del fondo
    glShadeModel(GL_SMOOTH)
    glClearDepth(1.0)
    # glDisable(GL_DEPTH_TEST)
    return


def main():
    init()
    glClearColor(1.0, 1.0, 1.0, 0.0)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

        glPushMatrix()
        glTranslate(320, 240, 0)
        glScale(640, 480, 1)

        glColor(1,1,1)
        dibujarCuadrado()
        glPopMatrix()

        glPushMatrix()
        glTranslate(320, 120, 0)
        glScale(640, 240, 1)
        glColor(0.5, 1, 0.5)
        dibujarCuadrado()
        glPopMatrix()

        glPushMatrix()
        glTranslate(320, 60, 0)
        glScale(640, 120, 1)
        glColor(0.0, 0.5, 0.5)
        dibujarCuadrado()
        glPopMatrix()

        glPushMatrix()
        glTranslate(320, 240, 0)
        glScale(640, 150, 1)
        glColor(0.7, 0.7, 1)
        dibujarTriangulo()
        glPopMatrix()

        glPushMatrix()
        glTranslate(200, 240, 0)
        glScale(400, 170, 1)

        dibujarTriangulo()
        glPopMatrix()

        glPushMatrix()
        glTranslate(430, 240, 0)
        glScale(60, 60, 1)
        glColor(1, 1, 0)
        dibujarCuadrado()
        glPopMatrix()

        glPushMatrix()
        glTranslate(430, 240, 0)
        glRotate(30, 0, 0, 1)

        glColor(1, 0.5, 0)

        glPushMatrix()
        glTranslate(-50, 0, 0)
        glScale(60, 30, 1)
        dibujarCuadrado()
        glPopMatrix()

        glPushMatrix()
        glTranslate(50, 0, 0)
        glScale(60, 30, 1)
        dibujarCuadrado()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0, 50, 0)
        glScale(30, 60, 1)
        dibujarCuadrado()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0, -50, 0)
        glScale(30, 60, 1)
        dibujarCuadrado()
        glPopMatrix()

        glPopMatrix()


        pygame.display.flip()
        pygame.time.wait(int(1000 / 30))  # 30 fps

main()

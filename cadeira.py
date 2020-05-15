import numpy as np
import pygame
from glfw import swap_buffers
from pygame.locals import *
from copy import copy

from OpenGL.GL import *
from OpenGL.GLU import *

import keyboard
import math


# _angle = -20.0
_angle = 0.0


class Cadeira:

    def __init__(self):
        self.x_table_chair = 0.0
        self.y_table_chair = 0.0

        self.x_front_right_leg = 0.0
        self.y_front_right_leg = 0.0

        self.x_back_right_leg = 0.0
        self.y_back_right_leg = 0.0

        self.x_front_left_leg = 0.0
        self.y_front_left_leg = 0.0

        self.x_back_left_leg = 0.0
        self.y_back_left_leg = 0.0

        self.x_support_chair_back_front = 0.0
        self.y_support_chair_back_front = 0.0

        self.zy_rotate_chair = 0.0
        self.zx_rotate_chair = 0.0
        self.center_x_rotate_chair = 0.0

        self.textura = None

    def mover_direita(self):
        self.x_table_chair += 0.6
        self.x_front_right_leg += 0.6
        self.x_back_right_leg += 0.6
        self.x_front_left_leg += 0.6
        self.x_back_left_leg += 0.6
        self.x_support_chair_back_front += 0.6

    def mover_esquerda(self):
        self.x_table_chair -= 0.6
        self.x_front_right_leg -= 0.6
        self.x_back_right_leg -= 0.6
        self.x_front_left_leg -= 0.6
        self.x_back_left_leg -= 0.6
        self.x_support_chair_back_front -= 0.6

    def mover_cima(self):
        self.y_table_chair += 0.6
        self.y_front_right_leg += 0.6
        self.y_back_right_leg += 0.6
        self.y_front_left_leg += 0.6
        self.y_back_left_leg += 0.6
        self.y_support_chair_back_front += 0.6

    def mover_baixo(self):
        self.y_table_chair -= 0.6
        self.y_front_right_leg -= 0.6
        self.y_back_right_leg -= 0.6
        self.y_front_left_leg -= 0.6
        self.y_back_left_leg -= 0.6
        self.y_support_chair_back_front -= 0.6

    def girar_vertical_para_frente(self):
        self.zy_rotate_chair += 0.8

    def girar_vertical_para_tras(self):
        self.zy_rotate_chair -= 0.8

    def girar_direita(self):
        self.zx_rotate_chair += 1

    def girar_esquerda(self):
        self.zx_rotate_chair -= 1

    def girar_centro_x_positivo(self):
        self.center_x_rotate_chair += 1

    def girar_centro_x_negativo(self):
        self.center_x_rotate_chair -= 1

    def criarCadeira(self):
        glTranslatef(0.0, 0.0, -14.0)

        glRotatef(self.zy_rotate_chair, 1.0, 0.0, 0.0)
        glRotatef(self.center_x_rotate_chair, 0.0, 0.0, 1.0)
        glRotatef(self.zx_rotate_chair, 0.0, 1.0, 0.0)

        # glColor3fv([1.0, 1.0, 0.0])

        # glBindTexture(GL_TEXTURE_2D, self.textura)

        glBegin(GL_QUADS)

        # TABLE CHAIR:
        glColor3fv([0.5, 1.0, 0.5])

        glNormal3fv([0.0 + self.x_table_chair, 0.0 + self.y_table_chair, 1.0])

        # front
        glVertex3fv([-2.0 + self.x_table_chair, -0.2 + self.y_table_chair, 2.0])
        glVertex3fv([2.0 + self.x_table_chair, -0.2 + self.y_table_chair, 2.0])
        glVertex3fv([2.0 + self.x_table_chair, 0.2 + self.y_table_chair, 2.0])
        glVertex3fv([-2.0 + self.x_table_chair, 0.2 + self.y_table_chair, 2.0])

        # texIndexes = [
        #     (-2.0 + self.x_table_chair, -0.2 + self.y_table_chair),
        #     (2.0 + self.x_table_chair, -0.2 + self.y_table_chair),
        #     (2.0 + self.x_table_chair, 0.2 + self.y_table_chair),
        #     (-2.0 + self.x_table_chair, 0.2 + self.y_table_chair)]
        #
        # for texIndex in texIndexes:
        #     glTexCoord2f(texIndex[0], texIndex[1])

        # Right
        glNormal3fv([1.0, 0.0, 0.0])

        glVertex3fv([2.0 + self.x_table_chair, -0.2 + self.y_table_chair, -2.0])
        glVertex3fv([2.0 + self.x_table_chair, 0.2 + self.y_table_chair, -2.0])
        glVertex3fv([2.0 + self.x_table_chair, 0.2 + self.y_table_chair, 2.0])
        glVertex3fv([2.0 + self.x_table_chair, -0.2 + self.y_table_chair, 2.0])

        # Back
        glNormal3fv([0.0, 0.0, -1.0])

        glVertex3fv([-2.0 + self.x_table_chair, -0.2 + self.y_table_chair, -2.0])
        glVertex3fv([-2.0 + self.x_table_chair, 0.2 + self.y_table_chair, -2.0])
        glVertex3fv([2.0 + self.x_table_chair, 0.2 + self.y_table_chair, -2.0])
        glVertex3fv([2.0 + self.x_table_chair, -0.2 + self.y_table_chair, -2.0])

        # Left
        glNormal3fv([-1.0, 0.0, 0.0])

        glVertex3fv([-2.0 + self.x_table_chair, -0.2 + self.y_table_chair, -2.0])
        glVertex3fv([-2.0 + self.x_table_chair, -0.2 + self.y_table_chair, 2.0])
        glVertex3fv([-2.0 + self.x_table_chair, 0.2 + self.y_table_chair, 2.0])
        glVertex3fv([-2.0 + self.x_table_chair, 0.2 + self.y_table_chair, -2.0])

        # top
        glNormal3fv([0.0, 1.0, 0.0])

        glVertex3fv([2.0 + self.x_table_chair, 0.2 + self.y_table_chair, 2.0])
        glVertex3fv([-2.0 + self.x_table_chair, 0.2 + self.y_table_chair, 2.0])
        glVertex3fv([-2.0 + self.x_table_chair, 0.2 + self.y_table_chair, -2.0])
        glVertex3fv([2.0 + self.x_table_chair, 0.2 + self.y_table_chair, -2.0])

        # bottom
        glNormal3fv([0.0, -1.0, 0.0])

        glVertex3fv([2.0 + self.x_table_chair, -0.2 + self.y_table_chair, 2.0])
        glVertex3fv([-2.0 + self.x_table_chair, -0.2 + self.y_table_chair, 2.0])
        glVertex3fv([-2.0 + self.x_table_chair, -0.2 + self.y_table_chair, -2.0])
        glVertex3fv([2.0 + self.x_table_chair, -0.2 + self.y_table_chair, -2.0])

        # FRONT RIGHT LEG:
        # front
        glColor3fv([1.0, 1.0, 0.0])

        glNormal3fv([0.0, 0.0, 1.0])

        glVertex3fv([1.8 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.6])
        glVertex3fv([1.4 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.6])
        glVertex3fv([1.4 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.6])
        glVertex3fv([1.8 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.6])

        # back
        glNormal3fv([0.0, 0.0, -1.0])

        glVertex3fv([1.8 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.2])
        glVertex3fv([1.4 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.2])
        glVertex3fv([1.4 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.2])
        glVertex3fv([1.8 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.2])

        # right
        glNormal3fv([1.0, 0.0, 0.0])

        glVertex3fv([1.8 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.6])
        glVertex3fv([1.8 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.2])
        glVertex3fv([1.8 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.2])
        glVertex3fv([1.8 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.6])

        # left
        glNormal3fv([-1.0, 0.0, 0.0])

        glVertex3fv([1.4 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.6])
        glVertex3fv([1.4 + self.x_front_right_leg, -0.2 + self.y_front_right_leg, 1.2])
        glVertex3fv([1.4 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.2])
        glVertex3fv([1.4 + self.x_front_right_leg, -3.0 + self.y_front_right_leg, 1.6])

        # BACK RIGHT LEG
        # front
        glNormal3fv([0.0, 0.0, -1.0])

        glVertex3fv([1.8 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.2])
        glVertex3fv([1.4 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.2])
        glVertex3fv([1.4 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.2])
        glVertex3fv([1.8 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.2])

        # back
        glNormal3fv([0.0, 0.0, -1.0])

        glVertex3fv([1.8 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.6])
        glVertex3fv([1.4 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.6])
        glVertex3fv([1.4 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.6])
        glVertex3fv([1.8 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.6])

        # right
        glNormal3fv([1.0, 0.0, 0.0])

        glVertex3fv([1.8 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.6])
        glVertex3fv([1.8 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.2])
        glVertex3fv([1.8 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.2])
        glVertex3fv([1.8 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.6])

        # left
        glNormal3fv([1.0, 0.0, 0.0])

        glVertex3fv([1.4 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.6])
        glVertex3fv([1.4 + self.x_back_right_leg, -0.2 + self.y_back_right_leg, -1.2])
        glVertex3fv([1.4 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.2])
        glVertex3fv([1.4 + self.x_back_right_leg, -3.0 + self.y_back_right_leg, -1.6])

        # FRONT LEFT LEG
        glNormal3fv([0.0, 0.0, 1.0])

        glVertex3fv([-1.8 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.6])
        glVertex3fv([-1.4 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.6])
        glVertex3fv([-1.4 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.6])
        glVertex3fv([-1.8 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.6])

        # back
        glNormal3fv([0.0, 0.0, -1.0])

        glVertex3fv([-1.8 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.2])
        glVertex3fv([-1.4 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.2])
        glVertex3fv([-1.4 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.2])
        glVertex3fv([-1.8 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.2])

        # right
        glNormal3fv([1.0, 0.0, 0.0])

        glVertex3fv([-1.8 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.6])
        glVertex3fv([-1.8 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.2])
        glVertex3fv([-1.8 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.2])
        glVertex3fv([-1.8 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.6])

        # left
        glNormal3fv([-1.0, 0.0, 0.0])

        glVertex3fv([-1.4 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.6])
        glVertex3fv([-1.4 + self.x_front_left_leg, -0.2 + self.y_front_left_leg, 1.2])
        glVertex3fv([-1.4 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.2])
        glVertex3fv([-1.4 + self.x_front_left_leg, -3.0 + self.y_front_left_leg, 1.6])

        # BACK LEFT LEG
        # front
        glNormal3fv([0.0, 0.0, -1.0])

        glVertex3fv([-1.8 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.2])
        glVertex3fv([-1.4 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.2])
        glVertex3fv([-1.4 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.2])
        glVertex3fv([-1.8 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.2])

        # back
        glNormal3fv([0.0, 0.0, -1.0])

        glVertex3fv([-1.8 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.6])
        glVertex3fv([-1.4 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.6])
        glVertex3fv([-1.4 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.6])
        glVertex3fv([-1.8 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.6])

        # right
        glNormal3fv([1.0, 0.0, 0.0])

        glVertex3fv([-1.8 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.6])
        glVertex3fv([-1.8 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.2])
        glVertex3fv([-1.8 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.2])
        glVertex3fv([-1.8 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.6])

        # left
        glNormal3fv([-1.0, 0.0, 0.0])

        glVertex3fv([-1.4 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.6])
        glVertex3fv([-1.4 + self.x_back_left_leg, -0.2 + self.y_back_left_leg, -1.2])
        glVertex3fv([-1.4 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.2])
        glVertex3fv([-1.4 + self.x_back_left_leg, -3.0 + self.y_back_left_leg, -1.6])

        # SUPPORT CHAIR BACK FRONT
        glColor3fv([0, 0, 1])

        glNormal3fv([-1.0, 0.0, 0.0])

        glVertex3fv([-1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -1.8])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -1.8])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -1.8])
        glVertex3fv([-1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -1.8])

        # back
        glNormal3fv([-1.0, 0.0, 0.0])

        glVertex3fv([-1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([-1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -2.0])

        glNormal3fv([-1.0, 0.0, 0.0])

        glVertex3fv([-1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([-1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([-1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -1.8])
        glVertex3fv([-1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -1.8])

        glVertex3fv([1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -1.8])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 0.2 + self.y_support_chair_back_front, -1.8])

        glVertex3fv([-1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -2.0])
        glVertex3fv([-1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -1.8])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -1.8])
        glVertex3fv([1.8 + self.x_support_chair_back_front, 3.5 + self.y_support_chair_back_front, -2.0])

        glEnd()

import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

from cadeira_trabalho.cadeira import Cadeira

_angle = -20.0


# right = true or false
def move_target(eye, target, right):
    # translada a câmera para a origem
    t0 = target - eye

    # Ignora a componente Y
    t0[1] = 0

    # Calcula o raio do círculo
    r = math.sqrt(t0[0] * t0[0] + t0[2] * t0[2])

    # Calcula o seno e o cosseno e a tangente do ângulo que o vetor faz com o eixo X
    sin_alfa = t0[2] / r
    cos_alfa = t0[0] / r
    if cos_alfa == 0:
        if sin_alfa == 1:
            alfa = math.pi / 2
        else:
            alfa = - math.pi / 2
    else:
        tg_alfa = sin_alfa / cos_alfa

        # Calcula o arco cuja tangente é calculada no passo anterior
        alfa = np.arctan(tg_alfa)

        # Como o retorno de arctan varia somente entre -pi/2 e pi/2, testar o cosseno para
        # calcular o ângulo correto
        if cos_alfa < 0:
            alfa = alfa - math.pi

    if right:
        signal = 1
    else:
        signal = -1

    # Varia o ângulo do alvo (target)
    alfa = alfa + 0.1 * signal

    # Calcula o novo alvo (sobre o eixo Y)
    t0[0] = r * math.cos(alfa)
    t0[2] = r * math.sin(alfa)

    n_target = eye + t0

    return n_target


# ahead = true or false
def move_can(eye, target, ahead):
    # equação paramétrica
    a = np.zeros(3)
    delta = 0.1
    p0 = eye
    p1 = target
    a = p1 - p0
    print('------------------------')
    print(p1)
    print(p0)
    print(a)

    if ahead:
        signal = 1
    else:
        signal = -1
    p0 = p0 + delta * a * signal
    # p1 = p1 + delta * a * signal

    # Câmera sobre o plano (X, Z)
    # p0[1] = 0

    return p0, p1


def loadTexture(image_file):
    textureSurface = pygame.image.load(image_file)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)
    print(texid)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def main():
    # Translação do cubo verde
    tx = 0
    ty = 0

    # criar objeto cadeira para ser manipulado na tela.
    cadeira1 = Cadeira()

    # UP vector angle = Pi/2 (90o)
    up_angle = 3.1415 / 2

    wireframe = False

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluPerspective(45, (display[0] / display[1]), 0.5, 20.0)

    # eye = (0, 0, 10)
    eye = np.zeros(3)
    eye[0] = 1.6
    eye[1] = 1.6
    eye[2] = 0
    # eye[1] = 10

    # target = (0, 0, 0)
    target = np.zeros(3)
    target[0] = 1.6
    target[1] = 1.6
    target[2] = 0

    # up = (1, 0, 0)
    up = np.zeros(3)
    up[0] = 0
    up[1] = 0
    up[2] = 0

    # up[1] = math.sin(up_angle)
    # up[0] = math.cos(up_angle)

    # t_table_cadeira = loadTexture('textura_cadeira.jpeg')

    # cadeira1.textura = t_table_cadeira
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Movimentação do cubo
                if event.key == K_w:
                    # ty = ty + 0.5
                    cadeira1.mover_cima()
                elif event.key == K_s:
                    # ty = ty - 0.5
                    cadeira1.mover_baixo()
                elif event.key == K_a:
                    # tx = tx - 0.5
                    cadeira1.mover_esquerda()
                elif event.key == K_d:
                    # tx = tx + 0.5
                    cadeira1.mover_direita()
                elif event.key == K_UP:  # girar para baixo
                    cadeira1.girar_vertical_para_frente()
                elif event.key == K_DOWN:  # girar ara cima
                    cadeira1.girar_vertical_para_tras()
                elif event.key == K_RIGHT:
                    cadeira1.girar_direita()
                elif event.key == K_LEFT:
                    cadeira1.girar_esquerda()
                elif event.key == K_PERIOD:
                    cadeira1.girar_centro_x_negativo()
                elif event.key == K_COMMA:
                    cadeira1.girar_centro_x_positivo()

                # Movimentação da direção da câmera
                # nos eixos X e Y (olho)
                # elif event.key == K_UP:
                #     target[1] = target[1] + 0.5
                # elif event.key == K_DOWN:
                #     target[1] = target[1] - 0.5

                # move_target(eye, target, right):
                # elif event.key == K_m:
                #     target = move_target(eye, target, True)
                # elif event.key == K_n:
                #     target = move_target(eye, target, False)

                elif event.key == K_PAGEUP:
                    # Mover para frente
                    eye, target = move_can(eye, target, True)
                    # eye[2] = eye[2] - 0.5
                elif event.key == K_PAGEDOWN:
                    # Mover para trás
                    eye, target = move_can(eye, target, False)
                    # eye[2] = eye[2] + 0.5
                #
                # elif event.key == K_t:
                #     eye[0] = eye[0] - 0.5
                # elif event.key == K_g:
                #     eye[0] = eye[0] + 0.5

                # Movimentação da parte de cima da câmera (UP vector)
                # elif event.key == K_PERIOD:
                #     up_angle += 0.05
                #     up[1] = math.sin(up_angle)
                #     up[0] = math.cos(up_angle)
                # elif event.key == K_COMMA:
                #     up_angle -= 0.05
                #     up[1] = math.sin(up_angle)
                #     up[0] = math.cos(up_angle)

                # Wireframe
                elif event.key == K_SPACE:
                    wireframe = not wireframe

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Habilitar teste de profundidade
        glEnable(GL_DEPTH_TEST)

        # glPushMatrix()
        #
        # gluLookAt(eye[0], eye[1], eye[2],
        #           target[0], target[1], target[2],
        #           up[0], up[1], up[2])
        #
        glPushMatrix()

        cadeira1.criarCadeira()

        glPopMatrix()
        # glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

# VER MOVIMENTO DA CÂMERA COM A CADEIRA NA CENA

main()

# ***********************************************************************************
#       main.py
#       Classe principal do projeto, responsável pela visualização dos objetos em 2d
#       Autor do código original (C++): Márcio Sarroglia Pinho
#       pinho@pucrs.br
#       Autor da versão em python: Luís Lima
#       luis.lima97@edu.pucrs.br
# ***********************************************************************************

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from poligono import *
from instancia import *
from ponto import *
from temporizador import *
from utils import *
from functools import reduce
import os

# Limites lógicos da área de desenho
min_ = Ponto()
max_ = Ponto()

t = Temporizador()

personagens = [Instancia() for i in range(10)]
quadrado = Poligono()

# Objeto que guarda alguns valores comuns
utils  = Utils()
curva1 = []

def calcula_bezier3(pc: List[Ponto], t) -> Ponto:
    p = Ponto()
    calc = 1 - t
    p = pc[0] * float(pow(calc, 2)) + pc[1] * 2 * calc * t + pc[2] * float(pow(t, 2)) # ver isso

    return p

def traca_bezier_3pontos():
    t = 0.0
    delta_t = 1.0/17

    glBegin(GL_LINE_STRIP)
    while(t < 1.0):
        p = calcula_bezier3(curva1, t)
        glVertex2f(p.x, p.y);
        t += delta_t
    p = calcula_bezier3(curva1, 1.0)
    glVertex2f(p.x, p.y);
    glEnd()

def init():
    glClearColor(0.0, 0.0, 1.0, 1.0)

    quadrado.le_poligono("Retangulo.txt")

    # Populando os limites lógicos da área de desenho
    min_.x = -20
    min_.y = -20
    max_.x = 20
    max_.y = 20

    personagens[0].posicao = Ponto(0,0)
    personagens[0].direcao = Ponto(1,0)

    utils.tempo = 10 # Esse valor significa o tempo que demora para completar a animação

    personagens[0].velocidade.x = (max_.x - min_.x)/utils.tempo
    personagens[0].velocidade.y = (max_.y - min_.y)/utils.tempo

    curva1.append(Ponto(-20,0))
    curva1.append(Ponto(-15,30))
    curva1.append(Ponto(0, 0))

def avanca_mru(dt: float):
    if personagens[0].posicao.x >= max_.x:
        utils.animando = False
        print(f"Tempo de animação: {utils.tempo_da_animacao} segundos")
        personagens[0].posicao(Ponto(0,0))

    deslocamento = Ponto()
    deslocamento.x = dt * personagens[0].velocidade.x * personagens[0].direcao.x
    deslocamento.y = dt * personagens[0].velocidade.y * personagens[0].direcao.y
    personagens[0].posicao = personagens[0].posicao + deslocamento


def avanca_com_bezier():
    t = utils.tempo_da_animacao/utils.tempo

    if t > 1.0:
        utils.animando = False
        print(f"Tempo de animação: {utils.tempo_da_animacao} segundos")
        personagens[0].posicao = Ponto(0,0)
    else:
        personagens[0].posicao = calcula_bezier3(curva1, t)

def avanca_personagens():
    avanca_com_bezier()

def animate():
    dt = t.get_delta()
    utils.acumula_delta_t += dt
    utils.tempo_total += dt
    utils.n_frames += 1

    if utils.acumula_delta_t > 1.0/30:
        utils.acumula_delta_t = 0
        glutPostRedisplay()

    if utils.tempo_total > 5.0:
        print(f"Tempo acumulado: {utils.tempo_total:.2f} segundos")
        print(f"Nros de frames sem desenho: {utils.n_frames}")
        print(f"FPS (sem desenho): {utils.n_frames/utils.tempo_total}")
        utils.tempo_total = 0
        utils.n_frames  = 0

    if utils.animando:
        avanca_personagens()
        utils.tempo_da_animacao += dt

def reshape(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glViewport(0, 0, w, h)
    glOrtho(min_.x, max_.x, min_.y, max_.y, 0, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def desenha_eixos():
    meio = Ponto()
    meio.x = (max_.x + min_.x)/2
    meio.y = (max_.y + min_.y)/2
    meio.z = (max_.z + min_.z)/2

    glBegin(GL_LINES)
    glVertex2f(min_.x, meio.y)
    glVertex2f(max_.x, meio.y)

    glVertex2f(meio.x, min_.y)
    glVertex2f(meio.x, max_.y)

    glEnd()

def rotaciona_ao_redor_de_um_ponto(alfa, p):
    glTranslatef(p.x, p.y, p.z)
    glRotatef(alfa, 0, 0, 1)
    glTranslatef(-p.x, -p.y, -p.z)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glLineWidth(3)
    glColor3f(1,1,1)
    desenha_eixos()

    glPushMatrix()
    glColor3f(1, 0, 0)
    metade = Ponto()

    metade.x = (quadrado.max.x - quadrado.min.x)/2
    metade.y = (quadrado.max.y - quadrado.min.y)/2
    metade.z = (quadrado.max.z - quadrado.min.z)/2

    glTranslatef(-metade.x, -metade.y, -metade.z)

    glTranslatef(personagens[0].posicao.x,
                    personagens[0].posicao.y,
                    personagens[0].posicao.z)

    quadrado.desenha_poligono()

    glPopMatrix()

    glColor3f(1,0,0)
    glPointSize(3)
    traca_bezier_3pontos()


    glutSwapBuffers()

def keyboard(*args):
    if args[0] == b'1':
        utils.animando = True
        utils.tempo_da_animacao = 0
        personagens[0].posicao = Ponto(min_.x, 0)
        personagens[0].direcao = Ponto(1, 0)
        print(f"Posicao inicial: {personagens[0].posicao.x}")
    if args[0] == b'\x1b': # fechar quando apertar ESC
        os._exit(0)

if __name__ == "__main__":
    glutInit(sys.argv)    
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(500, 500)
    wind = glutCreateWindow("Animacao")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    # glutSpecialFunc(arrow_keys)

    try:
        glutMainLoop()
    except SystemExit:
        pass
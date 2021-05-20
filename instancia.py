# ***********************************************************************************
#       instancia.py
#       Autor do código original (C++): Márcio Sarroglia Pinho
#       pinho@pucrs.br
#       Autor da versão em python: Luís Lima
#       luis.lima97@edu.pucrs.br
# ***********************************************************************************

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from ponto import *

class Instancia:

    def __init__(self):
        self.posicao: Ponto = Ponto()
        self.escala: Ponto = Ponto()
        self.direcao: Ponto = Ponto()
        self.velocidade: Ponto = Ponto()
        self.rotacao: float = 0.0
        self.modelo: int = 0

    # def __instancia_ponto(self):
    #     # modelview = (GLfloat * 16)()
    #     # mvm = GL.glGetFloatv(GL.GL_MODELVIEW_MATRIX, modelview)

    # def desenha(self):
    #     glPushMatrix()
    #     glTranslatef(self.posicao.x, self.posicao.y, 0)
    #     glRotatef(self.rotacao, 0, 0, 1)
        
    #     glPopMatrix()

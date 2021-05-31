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


    @staticmethod
    def calcula_ponto(p): 
        # Esse método calcula a posicao do ponto mesmo após sofrer translação, escala ou rotação
        # É um método estático, para usar: Personagem().calcula_ponto(Ponto(1, 0, 0))
        ponto_novo = []
        matriz_gl = glGetFloatv(GL_MODELVIEW_MATRIX)
        for i in range(4):
            ponto_novo.append(
                                matriz_gl[0][i] * p.x +
                                matriz_gl[1][i] * p.y +
                                matriz_gl[2][i] * p.z +
                                matriz_gl[3][i]
                            )
        
        return Ponto(ponto_novo[0], ponto_novo[1], ponto_novo[2])
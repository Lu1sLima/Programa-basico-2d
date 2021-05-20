# ***********************************************************************************
#       poligono.py
#       Autor do código original (C++): Márcio Sarroglia Pinho
#       pinho@pucrs.br
#       Autor da versão em python: Luís Lima
#       luis.lima97@edu.pucrs.br
# ***********************************************************************************

from typing import List
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ponto import *

class Poligono:

    def __init__(self):
        self.vertices: Ponto = []
        self.min = None
        self.max = None

    def insere_vertice(self, p):
        self.vertices.append(p)
        if len(self.vertices) > 1:
            self.min = Ponto.obtem_minimo(p, self.min)
            self.max = Ponto.obtem_maximo(p, self.max)
        else:
            self.min = p
            self.max = p
            

    def get_vertices(self) -> List[Ponto]:
        return self.vertices

    def desenha_poligono(self):
        glBegin(GL_LINE_LOOP)
        for ponto in self.vertices:
            glVertex3f(ponto.x, ponto.y, ponto.z)
        glEnd()
    
    def desenha_vertices(self):
        glBEgin(GL_POINTS)
        for ponto in self.vertices:
            glVertex3f(ponto.x, ponto.y, ponto.z)
        glEnd()

    def le_poligono(self, filename):
            path = os.path.join(os.getcwd(), filename)
            infile = open(path)
            num_arestas = infile.readline()

            for line in infile:
                words = line.split() # Separa as palavras na linha
                x = float (words[0])
                y = float (words[1])
                self.insere_vertice(Ponto(x, y))
            
            infile.close()


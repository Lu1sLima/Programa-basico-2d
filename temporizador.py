# ***********************************************************************************
#       temporizador.py
#       Classe que representa um ponto no plano cartesiano
#       Autor do código original (C++): Márcio Sarroglia Pinho
#       pinho@pucrs.br
#       Autor da versão em python: Luís Lima
#       luis.lima97@edu.pucrs.br
# ***********************************************************************************

import time

class Temporizador:

    def __init__(self):
        self.start = time.time()

    def get_delta(self):
        end_time = time.time()
        dt = (end_time - self.start)
        self.start = end_time
        return dt
# ***********************************************************************************
#       ponto.py
#       Classe que representa um ponto no plano cartesiano
#       Autor do código original (C++): Márcio Sarroglia Pinho
#       pinho@pucrs.br
#       Autor da versão em python: Luís Lima
#       luis.lima97@edu.pucrs.br
# ***********************************************************************************

class Ponto:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def multiplica(self, x, y, z=0):
        self.x *= x
        self.y *= y
        self.z *= z

    def soma(self, x, y, z=0):
        self.x += x
        self.y += y
        self.z += z

    @staticmethod
    def obtem_minimo(p1, p2):
        menor = lambda x, y: x if x < y else y
        p_min = Ponto()   

        p_min.x = menor(p2.x, p1.x)
        p_min.y = menor(p2.y, p1.y)
        p_min.z = menor(p2.z, p1.z)

        return p_min

    @staticmethod
    def obtem_maximo(p1, p2):
        maior = lambda x, y: y if x < y else x
        p_max = Ponto()

        p_max.x = maior(p2.x, p1.x)
        p_max.y = maior(p2.y, p1.y)
        p_max.z = maior(p2.z, p1.z)

        return p_max

    def __add__(self, p2):
        x = self.x + p2.x
        y = self.y + p2.y
        z = self.z + p2.z

        return Ponto(x, y, z)

    def __sub__(self, p2):
        x = self.x - p2.x
        y = self.y - p2.y
        z = self.z - p2.z

        return Ponto(x, y, z)

    def __mul__(self, k: float):
        x = self.x * k
        y = self.y * k
        z = self.z * k

        return Ponto(x, y, z)

    @staticmethod
    def opera_sub2(p1):
        return p1 * -1
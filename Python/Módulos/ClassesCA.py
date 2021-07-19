class FiguraPlana:

    def __init__(self, base=False, altura=False, Dzao=False,
                 Dzinho=False, Bzao=False, Bzinho=False, raio=False):
        self.__base = base
        self.__altura = altura
        self.__Dzao = Dzao
        self.__Dzinho = Dzinho
        self.__Bzao = Bzao
        self.__Bzinho = Bzinho
        self.__raio = raio

    def Quadrado(self):
        area = self.__base ** 2
        return area

    def Triangulo(self):
        area = (self.__base * self.__altura) / 2
        return area

    def Circulo(self, pi: float):
        area = pi * (self.__raio * self.__raio)
        return area

    def Losango(self):
        area = (self.__Dzao * self.__Dzinho) / 2
        return area

    def Trapezio(self):
        area = ((self.__Bzinho + self.__Bzao) * self.__altura) / 2
        return area


class FiguraEspacial:

    def __init__(self, base=False, raio=False):
        self.__base = base
        self.__raio = raio

    def Cubo(self):
        area = (self.__base ** 2) * 6
        return area

    def Esfera(self, pi):
        area = 4 * pi * (self.__raio ** 2)
        return area


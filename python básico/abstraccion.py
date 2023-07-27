# Script de abstracción
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio**2


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
print("Área del círculo:", circulo.area())
print("Área del rectángulo:", rectangulo.area())

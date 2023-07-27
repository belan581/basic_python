# Script de herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


perro = Perro("Firulais")
gato = Gato("Garfield")
print(perro.nombre, perro.hacer_sonido())
print(gato.nombre, gato.hacer_sonido())

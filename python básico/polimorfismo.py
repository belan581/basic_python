# Script de polimorfismo
class Animal:
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


def hacer_ruido(animal):
    return animal.hacer_sonido()


perro = Perro()
gato = Gato()
print(hacer_ruido(perro))
print(hacer_ruido(gato))

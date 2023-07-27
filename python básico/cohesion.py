# Script de cohesión
class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


calculadora = Calculadora()
print(calculadora.suma(5, 3))
print(calculadora.resta(5, 3))
print(calculadora.multiplicacion(5, 3))
print(calculadora.division(5, 3))

# Script de encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad


persona = Persona("Juan", 30)
print(persona.get_nombre(), persona.get_edad())
persona.set_nombre("María")
persona.set_edad(25)
print(persona.get_nombre(), persona.get_edad())

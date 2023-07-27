# Script de acoplamiento
class Motor:
    def encender(self):
        return "Motor encendido"


class Automovil:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        return self.motor.encender()


auto = Automovil()
print(auto.arrancar())

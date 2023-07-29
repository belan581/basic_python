# Ejemplo 1: Función sin parámetros que imprime un mensaje
def saludar():
    print("¡Hola, bienvenido!")


# Ejemplo 2: Función con un parámetro que imprime el mensaje de saludo
def saludar_a(nombre):
    print(f"¡Hola, {nombre}!")


# Ejemplo 3: Función con dos parámetros que suma dos números
def suma(a, b):
    return a + b


# Ejemplo 4: Función con un parámetro que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0


# Ejemplo 5: Función sin parámetros que genera un número aleatorio entre 1 y 10
import random


def generar_numero_aleatorio():
    return random.randint(1, 10)


# Ejemplo 6: Función con un parámetro que calcula el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Ejemplo 7: Función con un parámetro que convierte una lista de números a una lista de cuadrados
def cuadrados(lista):
    return [x**2 for x in lista]


# Ejemplo 8: Función con un parámetro que verifica si una palabra es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]


# Ejemplo 9: Función sin parámetros que devuelve la fecha y hora actual
from datetime import datetime


def obtener_fecha_hora_actual():
    return datetime.now()


# Ejemplo 10: Función con un parámetro que calcula el área de un círculo
import math


def area_circulo(radio):
    return math.pi * radio**2

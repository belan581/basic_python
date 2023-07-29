# Definición de un decorador simple
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función.")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función.")
        return resultado

    return wrapper


# Uso del decorador
@decorador
def funcion_ejemplo():
    print("¡Esta es una función de ejemplo!")


# Llamada a la función decorada
funcion_ejemplo()


# Decorador con argumentos
def decorador_con_argumentos(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(mensaje)
            resultado = func(*args, **kwargs)
            return resultado

        return wrapper

    return decorador


# Uso del decorador con argumentos
@decorador_con_argumentos("¡Hola desde el decorador!")
def funcion_saludo():
    print("¡Hola, esta es una función de saludo!")


# Llamada a la función decorada con argumentos
funcion_saludo()


# Decorador con parámetros variables
def decorador_con_parametros(parametro):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"El parámetro recibido es: {parametro}")
            resultado = func(*args, **kwargs)
            return resultado

        return wrapper

    return decorador


# Uso del decorador con parámetros variables
@decorador_con_parametros("Parámetro Ejemplo")
def funcion_con_parametros():
    print("Función con parámetros.")


# Llamada a la función decorada con parámetros variables
funcion_con_parametros()


# Decorador con argumentos y parámetros
def decorador_con_argumentos_y_parametros(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(mensaje)
            resultado = func(*args, **kwargs)
            return resultado

        return wrapper

    return decorador


# Uso del decorador con argumentos y parámetros
@decorador_con_argumentos_y_parametros("¡Hola desde el decorador con argumentos!")
def funcion_con_argumentos():
    print("Función con argumentos.")


# Llamada a la función decorada con argumentos y parámetros
funcion_con_argumentos()

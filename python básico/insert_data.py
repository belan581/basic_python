import psycopg2
import random

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
     host="127.0.0.1",
    database="prueb",
    user="postgres",
    password="1234",

)
cursor = conn.cursor()

# Lista de datos aleatorios para los campos 'nombre', 'creditos' y 'profesor'
nombres = ['Matemáticas I', 'Historia del Arte', 'Programación en Python', 'Economía Avanzada', 'Inglés Conversacional', 'Química Orgánica']
creditos = [3, 4, 5]
profesores = ['Dr. Smith', 'Prof. Johnson', 'Dra. Martinez', 'Dr. Brown', 'Prof. Lopez']

# Generar e insertar 20 registros aleatorios en la tabla 'cursos'
for _ in range(20):
    nombre = random.choice(nombres)
    credito = random.choice(creditos)
    profesor = random.choice(profesores)
    
    sql = f"INSERT INTO cursos (nombre, creditos, profesor) VALUES (%s, %s, %s)"
    data = (nombre, credito, profesor)
    cursor.execute(sql, data)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="prueba",
    user="postgres",
    password="1234",
)
# create a cursor
cur = conn.cursor()

# vendor_name = "Carlos Ivan"
estudiante_name = "Chiyon"
estudiante_edad = 30
estudiante_carrera = "MTI"

# sql = """INSERT INTO vendors(vendor_name)
# VALUES(%s) RETURNING vendor_id;"""


sql = """INSERT INTO estudiantes(nombre, edad, carrera)
             VALUES(%s,%s,%s) RETURNING id;"""

cur.execute(sql, (estudiante_name, estudiante_edad, estudiante_carrera))
# get the generated id back
vendor_id = cur.fetchone()[0]

# commit the changes to the database
conn.commit()

# close the communication with the PostgreSQL
cur.close()

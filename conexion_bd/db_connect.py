import psycopg2

# Se crea el objeto que hace la conexión a la bd
conn = psycopg2.connect(
    host="127.0.0.1",
    database="prueba",
    user="postgres",
    password="1234",
)
# create a cursor
cur = conn.cursor()

# execute a statement
print("PostgreSQL database version:")
query = "SELECT version()"
cur.execute(query)

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)

# close the communication with the PostgreSQL
cur.close()

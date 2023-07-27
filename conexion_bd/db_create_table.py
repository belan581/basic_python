import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="prueba",
    user="postgres",
    password="1234",)
# create a cursor
cur = conn.cursor()

# create table
cur.execute('''CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )''')

conn.commit()
# close the communication with the PostgreSQL
cur.close()

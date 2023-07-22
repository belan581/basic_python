import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="prueba",
    user="postgres",
    password="1234",)
# create a cursor
cur = conn.cursor()

vendor_name = "Carlos Ivan"

sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""

cur.execute(sql, (vendor_name,))
# get the generated id back
vendor_id = cur.fetchone()[0]

# commit the changes to the database
conn.commit()

# close the communication with the PostgreSQL
cur.close()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la conexión a la base de datos PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "prueba"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
Base = declarative_base()


# Definición de la tabla Contacto
class Contacto(Base):
    __tablename__ = "contactos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    telefono = Column(String)


# Crea las tablas en la base de datos
Base.metadata.create_all(engine)


# Crear un registro en la tabla Contacto
def crear_contacto(nombre, telefono):
    Session = sessionmaker(bind=engine)
    session = Session()
    contacto = Contacto(nombre=nombre, telefono=telefono)
    session.add(contacto)
    session.commit()
    session.close()


# Leer un registro de la tabla Contacto por ID
def leer_contacto_por_id(contacto_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    contacto = session.query(Contacto).filter_by(id=contacto_id).first()
    session.close()
    return contacto


# Leer varios registros de la tabla Contacto
def leer_todos_los_contactos():
    Session = sessionmaker(bind=engine)
    session = Session()
    contactos = session.query(Contacto).all()
    session.close()
    return contactos


# Actualizar un registro de la tabla Contacto por ID
def actualizar_contacto(contacto_id, nombre, telefono):
    Session = sessionmaker(bind=engine)
    session = Session()
    contacto = session.query(Contacto).filter_by(id=contacto_id).first()
    if contacto:
        contacto.nombre = nombre
        contacto.telefono = telefono
        session.commit()
    session.close()


# Eliminar un registro de la tabla Contacto por ID
def eliminar_contacto(contacto_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    contacto = session.query(Contacto).filter_by(id=contacto_id).first()
    if contacto:
        session.delete(contacto)
        session.commit()
    session.close()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos contactos
    crear_contacto("Juan Perez", "123456789")
    crear_contacto("Maria Lopez", "987654321")

    # Leer un registro por ID
    contacto_id = 1
    contacto = leer_contacto_por_id(contacto_id)
    if contacto:
        print(f"Contacto {contacto_id}: {contacto.nombre}, {contacto.telefono}")
    else:
        print(f"No se encontró el contacto con ID {contacto_id}")

    # Leer todos los contactos
    contactos = leer_todos_los_contactos()
    print("Lista de contactos:")
    for contacto in contactos:
        print(f"{contacto.id}: {contacto.nombre}, {contacto.telefono}")

    # Actualizar un contacto
    contacto_id = 1
    nuevo_nombre = "Juanita Perez"
    nuevo_telefono = "111111111"
    actualizar_contacto(contacto_id, nuevo_nombre, nuevo_telefono)
    contacto_actualizado = leer_contacto_por_id(contacto_id)
    if contacto_actualizado:
        print(
            f"Contacto {contacto_id} actualizado: {contacto_actualizado.nombre}, {contacto_actualizado.telefono}"
        )

    # Eliminar un contacto
    contacto_id = 2
    eliminar_contacto(contacto_id)
    contactos_actualizados = leer_todos_los_contactos()
    print("Lista de contactos actualizada:")
    for contacto in contactos_actualizados:
        print(f"{contacto.id}: {contacto.nombre}, {contacto.telefono}")

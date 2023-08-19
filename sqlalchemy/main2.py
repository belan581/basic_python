from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Configura la conexión a la base de datos PostgreSQL
DB_USER = "tu_usuario"
DB_PASSWORD = "tu_contraseña"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "tu_base_de_datos"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
Base = declarative_base()


# Definición de las tablas
class Contacto(Base):
    __tablename__ = "contactos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    telefono = Column(String)

    def __repr__(self):
        return f"Contacto(id={self.id}, nombre='{self.nombre}', telefono='{self.telefono}')"


class Grupo(Base):
    __tablename__ = "grupos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

    def __repr__(self):
        return f"Grupo(id={self.id}, nombre='{self.nombre}')"


class ContactoGrupo(Base):
    __tablename__ = "contacto_grupo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contacto_id = Column(Integer, ForeignKey("contactos.id"))
    grupo_id = Column(Integer, ForeignKey("grupos.id"))

    contacto = relationship("Contacto", back_populates="grupos")
    grupo = relationship("Grupo", back_populates="contactos")

    def __repr__(self):
        return f"ContactoGrupo(id={self.id}, contacto_id={self.contacto_id}, grupo_id={self.grupo_id})"


Contacto.grupos = relationship(
    "ContactoGrupo", order_by=ContactoGrupo.id, back_populates="contacto"
)
Grupo.contactos = relationship(
    "ContactoGrupo", order_by=ContactoGrupo.id, back_populates="grupo"
)

# Crea las tablas en la base de datos
Base.metadata.create_all(engine)

# Ejemplo de consultas
if __name__ == "__main__":
    # Crear algunos contactos y grupos
    Session = sessionmaker(bind=engine)
    session = Session()

    grupo1 = Grupo(nombre="Amigos")
    grupo2 = Grupo(nombre="Familia")
    grupo3 = Grupo(nombre="Trabajo")

    contacto1 = Contacto(nombre="Juan Perez", telefono="123456789")
    contacto2 = Contacto(nombre="Maria Lopez", telefono="987654321")
    contacto3 = Contacto(nombre="Carlos Ramirez", telefono="111111111")

    contacto1.grupos.append(ContactoGrupo(grupo=grupo1))
    contacto1.grupos.append(ContactoGrupo(grupo=grupo3))
    contacto2.grupos.append(ContactoGrupo(grupo=grupo1))
    contacto3.grupos.append(ContactoGrupo(grupo=grupo2))

    session.add_all([grupo1, grupo2, grupo3, contacto1, contacto2, contacto3])
    session.commit()

    # Ejemplo de consulta con JOIN
    print("Ejemplo de consulta con JOIN:")
    contactos_grupos = (
        session.query(Contacto, Grupo)
        .join(ContactoGrupo, ContactoGrupo.contacto_id == Contacto.id)
        .join(Grupo, ContactoGrupo.grupo_id == Grupo.id)
        .all()
    )
    for contacto, grupo in contactos_grupos:
        print(f"Contacto: {contacto.nombre}, Grupo: {grupo.nombre}")

    # Ejemplo de consulta con WHERE
    print("\nEjemplo de consulta con WHERE:")
    contactos_familia = (
        session.query(Contacto)
        .join(ContactoGrupo, ContactoGrupo.contacto_id == Contacto.id)
        .join(Grupo, ContactoGrupo.grupo_id == Grupo.id)
        .filter(Grupo.nombre == "Familia")
        .all()
    )
    for contacto in contactos_familia:
        print(f"Contacto en el grupo Familia: {contacto.nombre}")

    # Ejemplo de consulta con GROUP BY y HAVING
    print("\nEjemplo de consulta con GROUP BY y HAVING:")
    grupos_con_mas_de_un_contacto = (
        session.query(Grupo, Contacto)
        .join(ContactoGrupo, ContactoGrupo.grupo_id == Grupo.id)
        .join(Contacto, ContactoGrupo.contacto_id == Contacto.id)
        .group_by(Grupo.id)
        .having(func.count(Grupo.id) > 1)
        .all()
    )
    for grupo, contacto in grupos_con_mas_de_un_contacto:
        print(f"Grupo: {grupo.nombre}, Contacto: {contacto.nombre}")

    # Ejemplo de consulta con ORDER BY
    print("\nEjemplo de consulta con ORDER BY:")
    contactos_ordenados = session.query(Contacto).order_by(Contacto.nombre.desc()).all()
    for contacto in contactos_ordenados:
        print(f"Contacto: {contacto.nombre}")

    # Ejemplo de consulta con LIMIT
    print("\nEjemplo de consulta con LIMIT:")
    primeros_contactos = session.query(Contacto).limit(2).all()
    for contacto in primeros_contactos:
        print(f"Contacto: {contacto.nombre}")

    session.close()
